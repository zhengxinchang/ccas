#!/bin/bash

# this script is a modified version from https://blog.csdn.net/H2677lucy/article/details/120920053

set -e  # When the command of any line is executed incorrectly (for example, the command is written incorrectly), exit directly and do not continue to execute
set -o pipefail
#=====================


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

${vt} decompose ${invcf} -o ${outprefix}.decompose.vcf -s && echo "left_normalize:OK" || echo "left_normalize:crash"



# split multi-allelic variants

${vt} normalize   ${outprefix}.decompose.vcf   -r ${refdb} -o ${outprefix}.decompose.normalize.vcf -n && echo "split multi-allelic variants:OK" || echo "split multi-allelic variants:crash"


# add chr prefix 
#perl -lane 'if(/^#/){print}elsif(/^\d/){print "chr".$_}else{print}'  ${outprefix}.decompose.normalize.vcf  > ${outprefix}.decompose.normalize.addchr.vcf && logstep
perl -lane 'if(/^#/){print}else{if(/^chr/){print} else{print "chr".$_}}'  ${outprefix}.decompose.normalize.vcf  > ${outprefix}.decompose.normalize.addchr.vcf  && echo "add chr prefix:OK" || echo "add chr prefix:crash"

# ==========================================#
#                                           #
#                   VEP                     #
#                                           #
# ==========================================#


if [[ ${genomever} == "hg19" ]] ;then 
vep --assembly GRCh37  -i ${outprefix}.decompose.normalize.addchr.vcf -o ${outprefix}.decompose.normalize.vep.vcf --cache --cache_version 104 --offline  --force_overwrite --vcf --dir_cache /canceranno/zhengxc/canceranno/vep/humanCache --everything --pick && echo "vep:OK" || echo "vep:crash" 
else 
vep --assembly GRCh38  -i ${outprefix}.decompose.normalize.addchr.vcf -o ${outprefix}.decompose.normalize.vep.vcf --cache --cache_version 104 --offline  --force_overwrite --vcf --dir_cache /canceranno/zhengxc/canceranno/vep/humanCache --everything --pick && echo "vep:OK" || echo "vep:crash" 
fi


# ==========================================#
#                                           #   
#                   ANNOVAR                 #
#                                           #
# ==========================================#
# 2. annotation by ANNOVAR

if [[ ${genomever} == "hg19" ]] ;then 
${annovar}  ${outprefix}.decompose.normalize.vep.vcf  ${annovardb} -buildver ${genomever} -out ${outspace}/${outprefix} -remove \
-protocol refGene,ensGene,knownGene,cytoBand,avsnp150,dbnsfp41a,clinvar_20210123,1000g2015aug_all,1000g2015aug_afr,1000g2015aug_eas,1000g2015aug_eur,1000g2015aug_sas,1000g2015aug_amr,gnomad211_genome,exac03  \
-operation g,g,g,r,f,f,f,f,f,f,f,f,f,f,f  \
-nastring . -vcfinput -polish   && echo "annovar:OK" || echo "annovar:crash"
else 
${annovar}  ${outprefix}.decompose.normalize.vep.vcf  ${annovardb} -buildver ${genomever} -out ${outspace}/${outprefix} -remove \
-protocol refGene,ensGene,knownGene,cytoBand,avsnp150,dbnsfp41a,clinvar_20210123,1000g2015aug_all,1000g2015aug_afr,1000g2015aug_eas,1000g2015aug_eur,1000g2015aug_sas,1000g2015aug_amr,gnomad30_genome,exac03  \
-operation g,g,g,r,f,f,f,f,f,f,f,f,f,f,f  \
-nastring . -vcfinput -polish   && echo "annovar:OK" || echo "annovar:crash"
fi

# ==========================================#
#                                           #
#                   VCFANNO                 #
#                                           #
# ==========================================#

# 3. annotation by VCFANNO
bgzip  -f ${outspace}/${outprefix}.${genomever}_multianno.vcf && echo "bgZip compression:OK" || echo "bgZip compression:crash"
tabix -p vcf  ${outspace}/${outprefix}.${genomever}_multianno.vcf.gz && echo "tabix indexing:OK" || echo "tabix indexing:crash"

if [[ ${genomever} == "hg19" ]] ;then 

${vcfanno}    ${vcfannodb}/conf.hg19.toml  ${outspace}/${outprefix}.${genomever}_multianno.vcf.gz >${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf  \
 && echo "vcfAnno:OK" || echo "vcfAnno:crash"

else 

${vcfanno}    ${vcfannodb}/conf.hg38.toml  ${outspace}/${outprefix}.${genomever}_multianno.vcf.gz >${outspace}/${outprefix}.${genomever}_multianno.vcfanno.vcf   \
 && echo "vcfAnno:OK" || echo "vcfAnno:crash"

fi


