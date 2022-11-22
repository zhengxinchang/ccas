#!/usr/bin/Rscript
suppressMessages({
library(dplyr)
library(tibble)
library(GSVA)
library(GSEABase)

})


arg <- commandArgs(T)

if (length(arg) != 5){
message("Error: Wrapper need 1: exp 2: outdir 3:jobid 4: mappingfile 5: gmtfile")
quit()
}

#input<-read.table('exp.tsv',sep='\t',header=F)
input<-read.table(arg[1],sep='\t',header=F)
outdir<-arg[2]
jobid<-arg[3]
mapingFile <-arg[4]
gmtFile<- arg[5]

ens2sym<-read.table(mapingFile,header=F);
sel_gmt<-getGmt(gmtFile);
sets=as.list(sel_gmt)

colnames(ens2sym)<-c('ens','symbol')
ens2sym$ens=substring(ens2sym$ens,1,15) #delete version ENSG{\d..15}.1 => ENSG{\d..15}

colnames(input)<-c('ens','tpm')
input$ens=substring(input$ens,1,15) #delete version ENSG{\d..15}.1 => ENSG{\d..15}

input<-merge(ens2sym,input,by='ens')[,2:3]

df<-input %>% distinct(symbol,.keep_all=T)
rownames(df)<-df$symbol
df <- subset(df, select = c(tpm))
#df<-df[!apply(df,1,sum)==0,]

logTPM <- log2(df+1)
ssgsea <- gsva(as.matrix(logTPM), sets,method='ssgsea',kcdf='Gaussian',abs.ranking=TRUE)
ssgsea.1 <- ssgsea

for (i in colnames(ssgsea)) { #noramlization
 ssgsea.1[,i] <- (ssgsea[,i] -min(ssgsea[,i]))/(max(ssgsea[,i] )-min(ssgsea[,i] ))
}

outputPrefix <- paste0(outdir,"/",jobid)

ssgsea.1 <- as.data.frame(ssgsea.1) %>% rownames_to_column("name") %>% arrange(desc(tpm)) %>% head(100)
ssgsea <- as.data.frame(ssgsea) %>% rownames_to_column("name") %>% arrange(desc(tpm)) %>% head(100)
write.table(ssgsea.1, paste0(outputPrefix,".ssGSEA.normalize.txt"),quote=FALSE,row.names=F)
write.table(ssgsea, paste0(outputPrefix,".ssGSEA.raw.txt"),quote=FALSE,row.names=F)