from unicodedata import name
import uuid
import webGlobal
import os 
import datetime

def getJobID():
    u = uuid.uuid4()
    this_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + "_"+str(u)

    return str(this_id)

def calPageStart(pagenumber,pagesize):
    return (int(pagenumber-1))*int(pagesize)-1

def  create_job_dir(jobid,rootPath=None):
    if rootPath is None:
        thisPath = os.path.join(webGlobal.workspaceRoot,jobid)
    else:
        thisPath = os.path.join(rootPath,jobid)
    os.mkdir(thisPath)
    return thisPath


if __name__ == "__main__":
    print(getJobID())