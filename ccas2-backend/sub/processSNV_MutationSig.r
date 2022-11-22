.libPaths("/canceranno/zhengxc/canceranno/R/R-3.6.1/library")
library(deconstructSigs)


arg <- commandArgs(T)

inputTable = arg[1]
refver = arg[2]
outdir=arg[3]
jobid=arg[4]

sample.mut.ref<-read.table(inputTable,sep = "\t",header = T)

if( refver =="hg19"){

library(BSgenome.Hsapiens.UCSC.hg19)
sigs.input <- mut.to.sigs.input(mut.ref = sample.mut.ref, sample.id = "Sample", chr = "chr", pos = "pos", ref = "ref", alt = "alt",bsg=BSgenome.Hsapiens.UCSC.hg19)
}else{

library(BSgenome.Hsapiens.UCSC.hg38)
sigs.input <- mut.to.sigs.input(mut.ref = sample.mut.ref, sample.id = "Sample", chr = "chr", pos = "pos", ref = "ref", alt = "alt",bsg=BSgenome.Hsapiens.UCSC.hg38)
}

mysignatures <- whichSignatures(tumor.ref = sigs.input,  signatures.ref = signatures.cosmic,  sample.id = jobid,contexts.needed = T)

# write the mutation signatures 
similarity <-as.data.frame(t(mysignatures$weights))
similarity$Signature <- rownames(similarity)
names(similarity)<- c("Similarity","Signature")
pathPrefix = paste0(outdir,"/",jobid)
write.table(x = similarity,file =paste0(pathPrefix,".CosmicSigSimilarity.txt"),sep="\t",quote = F,row.names = F)


# write the mutation pattern 
tumorSig <- as.data.frame(t(mysignatures$tumor))
tumorSig$Pattern <- rownames(tumorSig)
names(tumorSig)<- c("Percent","Pattern")
write.table(x = tumorSig,file =paste0(pathPrefix,".TumorSignature.txt"),sep="\t",quote = F,row.names = F)



