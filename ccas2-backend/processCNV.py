import myutils 
def processcnv(cnv,cnvtype,refver,jobid,outdir):

    try:
        ret = myutils.ProcessCNVAndMethlation.process(
            f=cnv,
            ft=cnvtype, # gene,region
            refver=refver,
            jobid=jobid,
            outdir=outdir,
            omic_type="cnv"
        )

        return ret
    except:
        myutils.addGlobalError("Process CNV failed. Please double check your CNV file and CNV type.")
        return {}
