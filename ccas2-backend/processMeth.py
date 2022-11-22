import myutils 
def processmeth(meth,methtype,refver,jobid,outdir):
    try:
        ret = myutils.ProcessCNVAndMethlation.process(
            f=meth,
            ft=methtype, # gene,region
            refver=refver,
            jobid=jobid,
            outdir=outdir,
            omic_type="meth"
        )

        return ret
    except:
        myutils.addGlobalError("Process Methylation failed. Please double check your Methylation file and Methylation type.")
        return {}