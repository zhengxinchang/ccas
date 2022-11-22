import logging
import os
from types import GeneratorType
import myconfig
import subprocess
import myutils
import json 



def ConvertssGSEAToJson(ssGSEAPATH,ssGSEAJSONPath):
    res= []
    try:
        with open(ssGSEAPATH) as inf:
            next(inf)
            for x in inf:
                xlist = x.strip().split(" ")
                res.append({
                    "Name":xlist[0],
                    "Value":xlist[1],
                })
        json.dump(res,open(ssGSEAJSONPath,"w"))
        return True
    except:
        return False


def runSSGSEA(exp,outdir,jobid):
    print("Start to run ssGSEA...")

    cmd2 = f" { myconfig.config['exp']['ssGSEA']['cmd']} {exp} {outdir} {jobid} {myconfig.config['exp']['ssGSEA']['mappingFile']} {myconfig.config['exp']['ssGSEA']['gmtFile']} "

    p2 = subprocess.Popen(cmd2,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2.wait()
    stdout,stderr = p2.communicate()
    if "Execution halted" in  stderr.decode():
        return {"status":False,
            "msg":f"ssGSEA failed, please check Expression file. reason:{stderr.decode()}",
            "data":{
                "NormalizedFile":None,
                "RawFile":None
                }
            }
    else:
        try:
            NormalizedFilePath = os.path.join(outdir,jobid+".ssGSEA.normalize.txt")
            NormalizedJsonFilePath = os.path.join(outdir,jobid+".ssGSEA.normalize.json")
            ConvertssGSEAToJson(NormalizedFilePath,NormalizedJsonFilePath)

            RawFilePath = os.path.join(outdir,jobid+".ssGSEA.raw.txt")
            RawFileJsonPath = os.path.join(outdir,jobid+".ssGSEA.raw.json")
            ConvertssGSEAToJson(RawFilePath,RawFileJsonPath)
            return {"status":True,
            "msg":"OK",
            "data":{
                "NormalizedFile":NormalizedJsonFilePath,
                "RawFile":RawFileJsonPath
                }
            }
        except:
            return {"status":False,
            "msg":"Convert ssGSEA files to json failed.",
            "data":{
                "NormalizedFile":None,
                "RawFile":None
                }
            }

def process(exp,refver,jobid,outdir,exptype="gene"):
    """ 这里直接修改为"""

    try:
        expret =myutils.ProcessCNVAndMethlation.process(refver=refver,jobid=jobid,outdir=outdir,f=os.path.abspath(exp),ft=exptype,omic_type="exp")
        
        if exptype =="gene":

            ret = runSSGSEA(exp,outdir=outdir,jobid=jobid)
        
        elif exptype == "region":
            geneexp =    os.path.join(outdir,jobid+".input."+exptype+".gene.txt")
            ret = runSSGSEA(geneexp,outdir=outdir,jobid=jobid)
        logging.info(ret)
        return expret
    except:
        myutils.addGlobalError("Process Expression data failed. Please double check your expression file and expression type.")
        return {}


if __name__ == "__main__":

    runSSGSEA("./demo/exp.tsv",outdir="./demo",jobid="test_exp")