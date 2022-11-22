#/usr/bin/env python3
import argparse
import logging
import subprocess
import datetime
import automail
import os
import json
import myconfig
import dbAnnotation
import processExp  
import processCNV
import processMeth
import processSNV
import dumpToDisk
import myutils
import traceback
import sys

from  webDBmanager import webMysqlUtil 



logging.basicConfig(level=logging.INFO,format="[%(levelname)s - %(asctime)s] %(message)s")


"""
process* 都是为了到gene level，最终转化为基因的水平，统一的去注释
"""

def runPipeline(snvindel,snvindeltype,exp,meth,methtype,cnv,cnvtype,doid,jobid,outdir,refver,jobtitle,email):
    this_log = os.path.join(outdir,jobid+".CCASPipe.toUser.log")
    current_time = datetime.datetime.now()
    logging.info("\n\nStart CCAS2.0 pipeline\n\n\n")

    if not os.path.exists(outdir):
        logging.error(f"Output dir {outdir} does not exists!")
        exit(1)
    if refver.strip().lower() not in ["hg19","hg38"]:
        logging.error(f"refversion shoud be one of 'hg19' or 'hg38', but {refver} found")
        exit(1)
    webDbUtils = webMysqlUtil()

    def MyExceptionHandler(excType,excValue,traceBack):
        webDbUtilsExcetion = webMysqlUtil()
        ExceptionMessage = traceback.format_exception(excType, excValue, traceBack)
        
        # 记录那几个步骤没有运行成功，返回给用户看的信息，加上本地输出的实际错误
        errfilePath = os.path.join(outdir,jobid+".CCASPipe.toDeveloper.log.txt")

        outerr = open(this_log,"w")
        outerr.write("\n".join(myconfig.globalError) +"\n")
        outerr.close()

        mailText = f"Dear CCAS user,\nWe are very sorry to mail you that your submission is Failed with unexcepted reasons.\nJob id: '{jobid}'\nJob title: '{jobtitle}'\nPlease try it later.\nThis is usually caused by incorrect input file format\nIf you still get this email, please feel free to contact zhenxinchang@big.ac.cn."
        automail.auto_mail(mailText,"CCAS auto",email)
        webDbUtilsExcetion.updateJobStatus(jobid=jobid,status="3:crashed")

        innerouterr = open(errfilePath,"w")
        Msg = [x.rstrip("\n") for x in ExceptionMessage]
        Msg = "\n".join(Msg)
        innerouterr.write(Msg)
        innerouterr.close()
        # Msg = str(StackTraceBack.getCallerInfo()) + " &%& " +Msg
        # update batchlogdb run status

    sys.excepthook = MyExceptionHandler


    # init the log file to workingdir + progress.log
    logging.basicConfig(level=logging.INFO,format="[%(levelname)s - %(asctime)s] %(message)s")
    
    if meth != "None" and methtype != "None":
        methret = processMeth.processmeth(meth=os.path.abspath(meth),methtype=methtype,refver=refver,jobid=jobid,outdir=outdir)
    else:
        methret = {}
    if cnv != "None" and cnvtype != "None":
        cnvret = processCNV.processcnv(cnv=os.path.abspath(cnv),cnvtype=cnvtype,refver=refver,jobid=jobid,outdir=outdir)
    else:

        cnvret = {}

    if exp != "None":

        expret =processExp.process(exp=os.path.abspath(exp),refver=refver,jobid=jobid,outdir=outdir)
    else:
        expret ={}  

    snvret = processSNV.processsnvindel(snvindel=os.path.abspath(snvindel),snvindeltype=snvindeltype,refver=refver,outdir=outdir,jobid=jobid)
    

    # 这里判断 multianno.vcfanno.vcf是不是合法的vcf文件：
        # 如果是，则往下走，如果不是，则报错
    multianno_vcfnanno_vcf_path = os.path.join(outdir,jobid+"."+refver+"_multianno.vcfanno.vcf")
    
    
    if os.path.exists(multianno_vcfnanno_vcf_path) and myutils.checkVcfIsOK(multianno_vcfnanno_vcf_path):
        combine = myutils.combineMultiOmicsJson(snvret['geneblock'],expret,cnvret,methret)
        combineAddIDs =  myutils.addIDsToCombinedOmicsData(combine=combine)
        dbAnnotatedResult = dbAnnotation.annotateVariantByDatabase(combineAddIDs,DOID=doid)

        json.dump(dbAnnotatedResult,open(os.path.join(outdir,jobid+".dbAnnotated.json"),"w"))    
        res = dumpToDisk.dump2Disk(outdir,jobid,dbAnnotatedResult)
        finished_time = datetime.datetime.now()
        elapse_seconds = (finished_time - current_time).seconds
        elapse_min = round((float(elapse_seconds)/60),4)
        toUserLog = open(this_log,"w")
        toUserLog.write("\n".join(myconfig.globalError) +"\n")
        toUserLog.write(f"Elapsed time is:{str(elapse_min)} min")
        toUserLog.close()

        # SNV成功了，注释可以执行，这里发送邮件给用户，然后有提示信息
        try:
            mailText = f"""
            Dear CCAS user,
            Your submission is Finished.
            Job id: '{jobid}'
            Job title: '{jobtitle}'
            Elapse time: {elapse_min} minutes
            """
            if len(myconfig.globalError) >0:
                mailText = mailText + f"Some errors has occured in the annotation pipeline:\n" + '\n'.join(myconfig.globalError)
            automail.auto_mail(mailText,"CCAS auto",email)
        except:
            logging.info(f"Send email to {email} failed")
        webDbUtils.updateJobStatus(jobid=jobid,status="2:finished")
        webDbUtils.close()
        return {"status":True,"elapse_time":elapse_min}
    else: 
        # snv注释失败了，表明任务无法运行，下边应该联系用户。
        finished_time = datetime.datetime.now()
        elapse_seconds = (finished_time - current_time).seconds
        elapse_min = round((float(elapse_seconds)/60),4)

        toUserLog = open(this_log,"w")
        toUserLog.write("\n".join(myconfig.globalError) +"\n")
        toUserLog.write(f"Elapsed time is:{str(elapse_min)} min")
        toUserLog.close()
        
        mailText = f"Dear CCAS user,\nYour submission is Failed.\nJob id: '{jobid}'\nJob title: '{jobtitle}'\n"
        if len(myconfig.globalError) >0:
            mailText = mailText + f"Some errors has occured in the annotation pipeline:\n " +'\n'.join(myconfig.globalError)
            automail.auto_mail(mailText,"CCAS auto",email)
        webDbUtils.updateJobStatus(jobid=jobid,status="3:crashed")
        webDbUtils.close()
        return {"status":False,"elapse_time":elapse_min}
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="CCAS2.0 pipeline")

    parser.add_argument("--snvindel",help="vcf file",required=True)
    parser.add_argument("--snvindeltype",help="vcf file type: [ vcf, maf, 5coltsv ]",required=True)
    parser.add_argument("--exp",help="expression file,two Column, e.g. Ensembl_gene_name\texpression_value",required=False,default="None")
    parser.add_argument("--meth",help="methylation file,format is ID\tvalue",required=False,default="None")
    parser.add_argument("--methtype",help="methylation file type: [ gene, region ]",required=False,default="None")
    parser.add_argument("--cnv",help="cnv file, format is ID\tvalue",required=False,default="None")
    parser.add_argument("--cnvtype",help="cnv file type: [ gene, region ] ",required=False,default="None")
    parser.add_argument("--doid",help="Disease ontology id",required=True)
    parser.add_argument("--jobid",help="Jobid",required=True)
    parser.add_argument("--outdir",help="output dir (absolute path)",required=True)
    parser.add_argument("--refver",help="reference version",required=True)
    parser.add_argument("--jobtitle",help="jobtitle",required=True,default="None")
    parser.add_argument("--email",help="email",required=True,default="None")

    args = parser.parse_args()     
    
    ret =  runPipeline(args.snvindel,args.snvindeltype,args.exp,args.meth,args.methtype,args.cnv,args.cnvtype,args.doid,args.jobid,args.outdir,args.refver,args.jobtitle,args.email)
