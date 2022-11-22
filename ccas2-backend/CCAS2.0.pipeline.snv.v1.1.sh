#!/bin/bash

# this script is a modified version from https://blog.csdn.net/H2677lucy/article/details/120920053

set -e  # When the command of any line is executed incorrectly (for example, the command is written incorrectly), exit directly and do not continue to execute
set -o pipefail
#=====================

# version 3.9


# ==========================================#
#                                           #   
#             variant annotation            #
#                                           #
# ==========================================#

#if [ $# -ne 6 ] ;then
#echo "usage: sh script.sh invcf outdir refversion[hg19/hg38] outprefix "
#	exit 1
#fi

# ==========================================#
#                                           #   
#               configuration               #
#                                           #
# ==========================================#     

# cmd variables
invcf=${1}
# outputdir
outspace=${2}
# reference version
genomever=${3}
# output directory
outprefix=${4}
# doid

# env variables
workspace=/canceranno/zhengxc/canceranno
# pipeline dir
pipelinedir=/canceranno/zhengxc/canceranno/pipeline/pipeline3
# logf
log=./${outprefix}.snv.status.log



#=====================

this_step=1
message=""

function logstep() {
 ((this_step++));
}

#Actual tasks
function _start {
  echo "Start execution..."




# ==========================================#
#                                           #   
#               configuration               #
#                                           #
# ==========================================#     

cd ${outspace}
#rm $log
#touch $log
#date +"STARTTIME:%Y/%m/%d %H:%M:%S" >> $log
#echo "REFVER:${genomever}" >> $log
# gatk
gatk=${workspace}/gatk/gatk-4.2.0.0/gatk
# annovar
annovar=${workspace}/annovar/annovar/table_annovar.pl
annovardb=${workspace}/annovar/annovar/humandb/
#vcfanno
vcfanno=${workspace}/vcfanno/vcfanno_linux64
vcfannodb=${workspace}/pipeline/pipeline3
# referencedb
#refdb=${workspace}/reference/${genomever}/${genomever}.fa
refdb=${workspace}/reference/${genomever}/${genomever}.fa
#source activate 
source /home/zhengxc/miniconda3/etc/profile.d/conda.sh
conda activate canceranno
 
# vt
vt=${workspace}/vt-0.5772/vt

# ==========================================#
#                                           #   
#                preprocessing              #
#                                           #
# ==========================================#


# send job id to user

#message="email to user"
#python3 ${pipelinedir}/sendEmailBeforeRunning.py  ${email} ${outprefix} ${outspace}   && logstep



# left normalize
message="left normalize" 
${vt} decompose ${invcf} -o ${outprefix}.decompose.vcf -s && logstep



# split multi-allelic variants
message="split multi-allelic variants"
${vt} normalize   ${outprefix}.decompose.vcf   -r ${refdb} -o ${outprefix}.decompose.normalize.vcf -n && logstep


# add chr prefix 
message="add chr prefix"
#perl -lane 'if(/^#/){print}elsif(/^\d/){print "chr".$_}else{print}'  ${outprefix}.decompose.normalize.vcf  > ${outprefix}.decompose.normalize.addchr.vcf && logstep
perl -lane 'if(/^#/){print}else{if(/^chr/){print} else{print "chr".$_}}'  ${outprefix}.decompose.normalize.vcf  > ${outprefix}.decompose.normalize.addchr.vcf && logstep

# ==========================================#
#                                           #
#                   VEP                     #
#                                           #
# ==========================================#

message="Vep annotation"
if [[ ${genomever} == "hg19" ]] ;then 
vep --assembly GRCh37  -i ${outprefix}.decompose.normalize.addchr.vcf -o ${outprefix}.decompose.normalize.vep.vcf --cache --cache_version 104 --offline  --force_overwrite --vcf --dir_cache /canceranno/zhengxc/canceranno/vep/humanCache --everything --pick && logstep 
else 
vep --assembly GRCh38  -i ${outprefix}.decompose.normalize.addchr.vcf -o ${outprefix}.decompose.normalize.vep.vcf --cache --cache_version 104 --offline  --force_overwrite --vcf --dir_cache /canceranno/zhengxc/canceranno/vep/humanCache --everything --pick && logstep 
fi


# ==========================================#
#                                           #   
#                   ANNOVAR                 #
#                                           #
# ==========================================#
# 2. annotation by ANNOVAR
message="Annovar annotation"
if [[ ${genomever} == "hg19" ]] ;then 
${annovar}  ${outprefix}.decompose.normalize.vep.vcf  ${annovardb} -buildver ${genomever} -out ${outspace}/${outprefix} -remove \
-protocol refGene,ensGene,knownGene,cytoBand,avsnp150,dbnsfp41a,clinvar_20210123,1000g2015aug_all,1000g2015aug_afr,1000g2015aug_eas,1000g2015aug_eur,1000g2015aug_sas,1000g2015aug_amr,gnomad211_genome,exac03  \
-operation g,g,g,r,f,f,f,f,f,f,f,f,f,f,f  \
-nastring . -vcfinput -polish   && logstep
else 
${annovar}  ${outprefix}.decompose.normalize.vep.vcf  ${annovardb} -buildver ${genomever} -out ${outspace}/${outprefix} -remove \
-protocol refGene,ensGene,knownGene,cytoBand,avsnp150,dbnsfp41a,clinvar_20210123,1000g2015aug_all,1000g2015aug_afr,1000g2015aug_eas,1000g2015aug_eur,1000g2015aug_sas,1000g2015aug_amr,gnomad30_genome,exac03  \
-operation g,g,g,r,f,f,f,f,f,f,f,f,f,f,f  \
-nastring . -vcfinput -polish   && logstep
fi

# ==========================================#
#                                           #
#                   VCFANNO                 #
#                                           #
# ==========================================#
# 3. annotation by VCFANNO
message="bgZip compression"
bgzip  -f ${outspace}/${outprefix}.${genomever}_multianno.vcf  && logstep
message="tabix indexing"
tabix -p vcf  ${outspace}/${outprefix}.${genomever}_multianno.vcf.gz && logstep

message="vcfAnno annotation"
if [[ ${genomever} == "hg19" ]] ;then 

${vcfanno}    ${vcfannodb}/conf.hg19.toml  ${outspace}/${outprefix}.${genomever}_multianno.vcf.gz >${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf  \
 && logstep

else 

${vcfanno}    ${vcfannodb}/conf.hg38.toml  ${outspace}/${outprefix}.${genomever}_multianno.vcf.gz >${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf   \
 && logstep

fi


## ==========================================#
##                                           #
##          convert vcf to json              #
##                                           #
## ==========================================#
## 4. conversion from annotated vcf to json
#python3  ${pipelinedir}/ConvertVcf2Json.py --invcf ${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf --outjson ${outspace}/${outprefix}.${genomever}_origin.json --meta=DO=${doid} && echo "STEP:vcf2json:good" >> ${log} || echo "STEP:vcf2json:bad" >>${log}
#
#
## ==========================================#
##                                           #
##          annotate database                #
##                                           #
## ==========================================#
## 5. annotation database
#python3 ${pipelinedir}/AnnotateByDatabaseInfo.py --injson ${outspace}/${outprefix}.${genomever}_origin.json  --outjson ${outspace}/${outprefix}.${genomever}_annotated.json && echo "STEP:annotation database:good" >> ${log} || echo "STEP:annotation database:bad" >>${log}
#
#
## ==========================================#
##                                           #
##       mutation signature analysis         #
##                                           #
## ==========================================#
## 6. mutation signature analysis
#python3 ${pipelinedir}/ConvertVcf2Maf.py  --invcf ${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf    --outtable ${outspace}/${outprefix}.Mut.table.for.signatures.txt && echo "STEP:vcf2maf:good" >> ${log} || echo "STEP:vcf2maf:bad" >>${log}
#/canceranno/zhengxc/canceranno/R/R-3.6.1/bin/Rscript ${pipelinedir}/MutSigRun.r  ${outspace}/${outprefix}.Mut.table.for.signatures.txt  ${genomever}   && echo "STEP:mutation signature:good" >> ${log} || echo "STEP:mutation signature:bad" >>${log}
#python3 ${pipelinedir}/ConvertSigPattern2Json.py  --intable ${outspace}/SignatureTumorPatternMatrix.txt  --outjson ${outspace}/SignatureTumorPatternMatrix.json && echo "STEP:signature pattern to json:good" >> ${log} || echo "STEP:signature pattern to json:bad" >>${log}
#python3 ${pipelinedir}/ConvertSimilarity2Json.py  --intable ${outspace}/SignatureSimilarityMatrix.txt  --outjson ${outspace}/SignatureSimilarityMatrix.json && echo "STEP:signature similarity to json:good" >> ${log} || echo "STEP:signature similarity to json:bad" >>${log}
#
#
##
#
## ==========================================#
##                                           #
##       mutation distribution analysis      #
##                                           #
## ==========================================#
## 7. mutation distribution
#python3 ${pipelinedir}/ConvertVcf2MutDistr.py  --invcf ${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf   --outjson ${outspace}/MutDistribution.json && echo "STEP:mutation distribution:good" >> ${log} || echo "STEP:mutation distribution:bad" >>${log}
#
#
#
## ==========================================#
##                                           #
##               summarize data              #
##                                           #
## ==========================================#
## 8. summarize data
#python3 ${pipelinedir}/SummarizeData.py --injson ${outspace}/${outprefix}.${genomever}_annotated.json   --mutsig   ${outspace}/SignatureSimilarityMatrix.json   --outdir ${outspace} && echo "STEP:summarize data:good" >> ${log} || echo "STEP:summarize data:bad" >>${log}
#
## ==========================================#
##                                           #
##               summarize data              #
##                                           #
## ==========================================#
## 9. sendemail to user
#python3 ${pipelinedir}/sendEmail.py  ${email} ${outprefix} ${outspace}   && "STEP:email to user:good" >> ${log} || echo "STEP:email to user:bad" >>${log}
#
#
#date +"ENDTIME:%Y/%m/%d %H:%M:%S" >> $log
#
#echo "STATUS:All finished" >>${log}



	  printf "status:ALLDONE;step:${this_step};step_name:${message}\n";
	  printf "status:ALLDONE;step:${this_step};step_name:${message}\n" > ${log}

  
}


#Method of handling exit
function _exit {
  #Mark of successful execution
  is_exec_succ=$?
  if [ "A$execption" != 0 ]
  then
    if [ "A$is_exec_succ" != "A0" ]
    then
      echo "The script execution is interrupted abnormally, and the program operation is terminated!";
	  printf "status:crash;step:${this_step};step_name:${message}\n";
	  printf "status:crash;step:${this_step};step_name:${message}\n" > ${log}
	  echo 1
      exit 1
    else
      _success
    fi
  fi
}


#Method of handling failure
#function _fail {
#  execption=0
#  echo "handles the logic of failure"
#  exit 1
#}
 
#Method of handling success
function _success {
  echo "The script was executed successfully..."
	  printf "status:OK;step:${this_step};step_name:${message}\n";
	  printf "status:OK;step:${this_step};step_name:${message}\n" > ${log}
  echo 0
}
 

 
#Exception = 0 indicates that the program handles the abnormal exit
#Exception = - 1 indicates that the interrupt is abnormal or the execution is successful
execption=-1

#Capture exit action
trap _exit EXIT
_start

