
from csv import excel_tab
import json
import os
import subprocess
from sys import stderr
from token import EXACT_TOKEN_TYPES
import myconfig
def ConvertVCF2Table(invcf,samplename,outtable):
    out = []
    with open(invcf) as inf:
        for line in inf:
            if line.startswith("#"):
                continue
            ll = line.strip("\n").split("\t")
            ref = ll[3]
            alt = ll[4]
            if len(ref) != 1 or ref.strip() =="-":
                continue
                
            if len(alt) != 1 or alt.strip() =="-":
                continue
            out.append("\t".join([samplename,ll[0],ll[1],ref,alt]))
    with open(outtable,'w') as myoutf:
        myoutf.write("\t".join(["Sample","chr","pos","ref","alt"])+"\n")
        for k in out:
            myoutf.write(k+"\n")


def ConvertTumorSigTableToJson(intable,outjson):
    
    keylist = ['C>A',"C>G","C>T","T>A","T>C","T>G"]
    with open(intable) as inf:
        inf.readline()
        out = []
        for k in inf:
            klist = k.strip('\n').split("\t")
            pattern = klist[1]
            percent = klist[0]
            for m in keylist:
                if m in pattern:
                    z = pattern.replace(m,"*")
                    out.append([z,m,round(float(percent),4)])
            # out.append(["Signature",klist[1].replace("Signature.","S"),float(klist[0])])
    with open(outjson,'w') as outf:
        json.dump(out,outf)

def ConvertCosmicSimilarityTableToJson(intable,outjson):
    with open(intable) as inf:
        inf.readline()
        out = []
        for k in inf:
            klist = k.strip('\n').split("\t")
            klist[1].replace("Signature.","S")
            out.append(["Signature",klist[1].replace("Signature.","S"),float(klist[0])])
    with open(outjson,'w') as outf:
        json.dump(out,outf)



def runSignatureCal(outdir,jobid,refver,VCF):
    print("Start to calculate mutation signature...")
    convertedMAF= os.path.join(outdir,jobid+"."+refver+"_multianno.vcfanno.converted.maf")
    ConvertVCF2Table(VCF,jobid,convertedMAF)
    
    # Calculate Mutsig 
    cmd2 = f" { myconfig.config['snv']['mutsigcal']}  {convertedMAF}  {refver}  {outdir} {jobid} "
    # print(cmd2

    p2 = subprocess.Popen(cmd2,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2.wait()
    stdout,stderr = p2.communicate()

    if "Execution halted" in  stderr.decode():
        return {"status":False,
            "msg":f"Calcualte signatures failed, please check reference version or base of the VCF. reason:{stderr.decode()}",
            "data":{
                "cosmicSimilarity":None,
                "tumorSignature":None
                }
            }
    else:
        try:
            TumorSigPath = os.path.join(outdir,jobid+".TumorSignature.txt")
            TumorSigJsonPath = os.path.join(outdir,jobid+".TumorSignature.json")
            ConvertTumorSigTableToJson(TumorSigPath,TumorSigJsonPath)

            cosmicSigSimilarityPath = os.path.join(outdir,jobid+".CosmicSigSimilarity.txt")
            cosmicSigSimilarityJsonPath = os.path.join(outdir,jobid+".CosmicSigSimilarity.json")
            ConvertCosmicSimilarityTableToJson(cosmicSigSimilarityPath,cosmicSigSimilarityJsonPath)
            return {"status":True,
            "msg":"OK",
            "data":{
                "cosmicSimilarity":cosmicSigSimilarityJsonPath,
                "tumorSignature":TumorSigJsonPath
                }
            }
        except:
            return {"status":False,
            "msg":"Convert singature files to json failed.",
            "data":{
                "cosmicSimilarity":None,
                "tumorSignature":None
                }
            }


if __name__ == "__main__":

    ret = runSignatureCal("./demo","test_snv","hg38","/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/demo/snv.vcf")
    print(ret)