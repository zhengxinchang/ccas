
from sys import stderr
import myutils
import subprocess
import myconfig
import os
from collections import OrderedDict
import logging
import json
import multiprocessing
import processSNV_Mutsig

import pandas as pd
import os
import numpy as np


def convert(filepath,filetype,outfile,refver):


    vcf_head = ["##fileformat=VCFv4.2"]
    
    if refver == "hg19":
        vcf_head.append("""##contig=<ID=chr10,length=135534747>
##contig=<ID=chr11,length=135006516>
##contig=<ID=chr11_gl000202_random,length=40103>
##contig=<ID=chr12,length=133851895>
##contig=<ID=chr13,length=115169878>
##contig=<ID=chr14,length=107349540>
##contig=<ID=chr15,length=102531392>
##contig=<ID=chr16,length=90354753>
##contig=<ID=chr17_ctg5_hap1,length=1680828>
##contig=<ID=chr17,length=81195210>
##contig=<ID=chr17_gl000203_random,length=37498>
##contig=<ID=chr17_gl000204_random,length=81310>
##contig=<ID=chr17_gl000205_random,length=174588>
##contig=<ID=chr17_gl000206_random,length=41001>
##contig=<ID=chr18,length=78077248>
##contig=<ID=chr18_gl000207_random,length=4262>
##contig=<ID=chr19,length=59128983>
##contig=<ID=chr19_gl000208_random,length=92689>
##contig=<ID=chr19_gl000209_random,length=159169>
##contig=<ID=chr1,length=249250621>
##contig=<ID=chr1_gl000191_random,length=106433>
##contig=<ID=chr1_gl000192_random,length=547496>
##contig=<ID=chr20,length=63025520>
##contig=<ID=chr21,length=48129895>
##contig=<ID=chr21_gl000210_random,length=27682>
##contig=<ID=chr22,length=51304566>
##contig=<ID=chr2,length=243199373>
##contig=<ID=chr3,length=198022430>
##contig=<ID=chr4_ctg9_hap1,length=590426>
##contig=<ID=chr4,length=191154276>
##contig=<ID=chr4_gl000193_random,length=189789>
##contig=<ID=chr4_gl000194_random,length=191469>
##contig=<ID=chr5,length=180915260>
##contig=<ID=chr6_apd_hap1,length=4622290>
##contig=<ID=chr6_cox_hap2,length=4795371>
##contig=<ID=chr6_dbb_hap3,length=4610396>
##contig=<ID=chr6,length=171115067>
##contig=<ID=chr6_mann_hap4,length=4683263>
##contig=<ID=chr6_mcf_hap5,length=4833398>
##contig=<ID=chr6_qbl_hap6,length=4611984>
##contig=<ID=chr6_ssto_hap7,length=4928567>
##contig=<ID=chr7,length=159138663>
##contig=<ID=chr7_gl000195_random,length=182896>
##contig=<ID=chr8,length=146364022>
##contig=<ID=chr8_gl000196_random,length=38914>
##contig=<ID=chr8_gl000197_random,length=37175>
##contig=<ID=chr9,length=141213431>
##contig=<ID=chr9_gl000198_random,length=90085>
##contig=<ID=chr9_gl000199_random,length=169874>
##contig=<ID=chr9_gl000200_random,length=187035>
##contig=<ID=chr9_gl000201_random,length=36148>
##contig=<ID=chrM,length=16571>
##contig=<ID=chrUn_gl000211,length=166566>
##contig=<ID=chrUn_gl000212,length=186858>
##contig=<ID=chrUn_gl000213,length=164239>
##contig=<ID=chrUn_gl000214,length=137718>
##contig=<ID=chrUn_gl000215,length=172545>
##contig=<ID=chrUn_gl000216,length=172294>
##contig=<ID=chrUn_gl000217,length=172149>
##contig=<ID=chrUn_gl000218,length=161147>
##contig=<ID=chrUn_gl000219,length=179198>
##contig=<ID=chrUn_gl000220,length=161802>
##contig=<ID=chrUn_gl000221,length=155397>
##contig=<ID=chrUn_gl000222,length=186861>
##contig=<ID=chrUn_gl000223,length=180455>
##contig=<ID=chrUn_gl000224,length=179693>
##contig=<ID=chrUn_gl000225,length=211173>
##contig=<ID=chrUn_gl000226,length=15008>
##contig=<ID=chrUn_gl000227,length=128374>
##contig=<ID=chrUn_gl000228,length=129120>
##contig=<ID=chrUn_gl000229,length=19913>
##contig=<ID=chrUn_gl000230,length=43691>
##contig=<ID=chrUn_gl000231,length=27386>
##contig=<ID=chrUn_gl000232,length=40652>
##contig=<ID=chrUn_gl000233,length=45941>
##contig=<ID=chrUn_gl000234,length=40531>
##contig=<ID=chrUn_gl000235,length=34474>
##contig=<ID=chrUn_gl000236,length=41934>
##contig=<ID=chrUn_gl000237,length=45867>
##contig=<ID=chrUn_gl000238,length=39939>
##contig=<ID=chrUn_gl000239,length=33824>
##contig=<ID=chrUn_gl000240,length=41933>
##contig=<ID=chrUn_gl000241,length=42152>
##contig=<ID=chrUn_gl000242,length=43523>
##contig=<ID=chrUn_gl000243,length=43341>
##contig=<ID=chrUn_gl000244,length=39929>
##contig=<ID=chrUn_gl000245,length=36651>
##contig=<ID=chrUn_gl000246,length=38154>
##contig=<ID=chrUn_gl000247,length=36422>
##contig=<ID=chrUn_gl000248,length=39786>
##contig=<ID=chrUn_gl000249,length=38502>
##contig=<ID=chrX,length=155270560>
##contig=<ID=chrY,length=59373566>""")
    else:
        vcf_head.append("""##contig=<ID=chr1,length=248956422>
##contig=<ID=chr10,length=133797422>
##contig=<ID=chr11,length=135086622>
##contig=<ID=chr11_KI270721v1_random,length=100316>
##contig=<ID=chr12,length=133275309>
##contig=<ID=chr13,length=114364328>
##contig=<ID=chr14,length=107043718>
##contig=<ID=chr14_GL000009v2_random,length=201709>
##contig=<ID=chr14_GL000225v1_random,length=211173>
##contig=<ID=chr14_KI270722v1_random,length=194050>
##contig=<ID=chr14_GL000194v1_random,length=191469>
##contig=<ID=chr14_KI270723v1_random,length=38115>
##contig=<ID=chr14_KI270724v1_random,length=39555>
##contig=<ID=chr14_KI270725v1_random,length=172810>
##contig=<ID=chr14_KI270726v1_random,length=43739>
##contig=<ID=chr15,length=101991189>
##contig=<ID=chr15_KI270727v1_random,length=448248>
##contig=<ID=chr16,length=90338345>
##contig=<ID=chr16_KI270728v1_random,length=1872759>
##contig=<ID=chr17,length=83257441>
##contig=<ID=chr17_GL000205v2_random,length=185591>
##contig=<ID=chr17_KI270729v1_random,length=280839>
##contig=<ID=chr17_KI270730v1_random,length=112551>
##contig=<ID=chr18,length=80373285>
##contig=<ID=chr19,length=58617616>
##contig=<ID=chr1_KI270706v1_random,length=175055>
##contig=<ID=chr1_KI270707v1_random,length=32032>
##contig=<ID=chr1_KI270708v1_random,length=127682>
##contig=<ID=chr1_KI270709v1_random,length=66860>
##contig=<ID=chr1_KI270710v1_random,length=40176>
##contig=<ID=chr1_KI270711v1_random,length=42210>
##contig=<ID=chr1_KI270712v1_random,length=176043>
##contig=<ID=chr1_KI270713v1_random,length=40745>
##contig=<ID=chr1_KI270714v1_random,length=41717>
##contig=<ID=chr2,length=242193529>
##contig=<ID=chr20,length=64444167>
##contig=<ID=chr21,length=46709983>
##contig=<ID=chr22,length=50818468>
##contig=<ID=chr22_KI270731v1_random,length=150754>
##contig=<ID=chr22_KI270732v1_random,length=41543>
##contig=<ID=chr22_KI270733v1_random,length=179772>
##contig=<ID=chr22_KI270734v1_random,length=165050>
##contig=<ID=chr22_KI270735v1_random,length=42811>
##contig=<ID=chr22_KI270736v1_random,length=181920>
##contig=<ID=chr22_KI270737v1_random,length=103838>
##contig=<ID=chr22_KI270738v1_random,length=99375>
##contig=<ID=chr22_KI270739v1_random,length=73985>
##contig=<ID=chr2_KI270715v1_random,length=161471>
##contig=<ID=chr2_KI270716v1_random,length=153799>
##contig=<ID=chr3,length=198295559>
##contig=<ID=chr3_GL000221v1_random,length=155397>
##contig=<ID=chr4,length=190214555>
##contig=<ID=chr4_GL000008v2_random,length=209709>
##contig=<ID=chr5,length=181538259>
##contig=<ID=chr5_GL000208v1_random,length=92689>
##contig=<ID=chr6,length=170805979>
##contig=<ID=chr7,length=159345973>
##contig=<ID=chr8,length=145138636>
##contig=<ID=chr9,length=138394717>
##contig=<ID=chr9_KI270717v1_random,length=40062>
##contig=<ID=chr9_KI270718v1_random,length=38054>
##contig=<ID=chr9_KI270719v1_random,length=176845>
##contig=<ID=chr9_KI270720v1_random,length=39050>
##contig=<ID=chr1_KI270762v1_alt,length=354444>
##contig=<ID=chr1_KI270766v1_alt,length=256271>
##contig=<ID=chr1_KI270760v1_alt,length=109528>
##contig=<ID=chr1_KI270765v1_alt,length=185285>
##contig=<ID=chr1_GL383518v1_alt,length=182439>
##contig=<ID=chr1_GL383519v1_alt,length=110268>
##contig=<ID=chr1_GL383520v2_alt,length=366580>
##contig=<ID=chr1_KI270764v1_alt,length=50258>
##contig=<ID=chr1_KI270763v1_alt,length=911658>
##contig=<ID=chr1_KI270759v1_alt,length=425601>
##contig=<ID=chr1_KI270761v1_alt,length=165834>
##contig=<ID=chr2_KI270770v1_alt,length=136240>
##contig=<ID=chr2_KI270773v1_alt,length=70887>
##contig=<ID=chr2_KI270774v1_alt,length=223625>
##contig=<ID=chr2_KI270769v1_alt,length=120616>
##contig=<ID=chr2_GL383521v1_alt,length=143390>
##contig=<ID=chr2_KI270772v1_alt,length=133041>
##contig=<ID=chr2_KI270775v1_alt,length=138019>
##contig=<ID=chr2_KI270771v1_alt,length=110395>
##contig=<ID=chr2_KI270768v1_alt,length=110099>
##contig=<ID=chr2_GL582966v2_alt,length=96131>
##contig=<ID=chr2_GL383522v1_alt,length=123821>
##contig=<ID=chr2_KI270776v1_alt,length=174166>
##contig=<ID=chr2_KI270767v1_alt,length=161578>
##contig=<ID=chr3_JH636055v2_alt,length=173151>
##contig=<ID=chr3_KI270783v1_alt,length=109187>
##contig=<ID=chr3_KI270780v1_alt,length=224108>
##contig=<ID=chr3_GL383526v1_alt,length=180671>
##contig=<ID=chr3_KI270777v1_alt,length=173649>
##contig=<ID=chr3_KI270778v1_alt,length=248252>
##contig=<ID=chr3_KI270781v1_alt,length=113034>
##contig=<ID=chr3_KI270779v1_alt,length=205312>
##contig=<ID=chr3_KI270782v1_alt,length=162429>
##contig=<ID=chr3_KI270784v1_alt,length=184404>
##contig=<ID=chr4_KI270790v1_alt,length=220246>
##contig=<ID=chr4_GL383528v1_alt,length=376187>
##contig=<ID=chr4_KI270787v1_alt,length=111943>
##contig=<ID=chr4_GL000257v2_alt,length=586476>
##contig=<ID=chr4_KI270788v1_alt,length=158965>
##contig=<ID=chr4_GL383527v1_alt,length=164536>
##contig=<ID=chr4_KI270785v1_alt,length=119912>
##contig=<ID=chr4_KI270789v1_alt,length=205944>
##contig=<ID=chr4_KI270786v1_alt,length=244096>
##contig=<ID=chr5_KI270793v1_alt,length=126136>
##contig=<ID=chr5_KI270792v1_alt,length=179043>
##contig=<ID=chr5_KI270791v1_alt,length=195710>
##contig=<ID=chr5_GL383532v1_alt,length=82728>
##contig=<ID=chr5_GL949742v1_alt,length=226852>
##contig=<ID=chr5_KI270794v1_alt,length=164558>
##contig=<ID=chr5_GL339449v2_alt,length=1612928>
##contig=<ID=chr5_GL383530v1_alt,length=101241>
##contig=<ID=chr5_KI270796v1_alt,length=172708>
##contig=<ID=chr5_GL383531v1_alt,length=173459>
##contig=<ID=chr5_KI270795v1_alt,length=131892>
##contig=<ID=chr6_GL000250v2_alt,length=4672374>
##contig=<ID=chr6_KI270800v1_alt,length=175808>
##contig=<ID=chr6_KI270799v1_alt,length=152148>
##contig=<ID=chr6_GL383533v1_alt,length=124736>
##contig=<ID=chr6_KI270801v1_alt,length=870480>
##contig=<ID=chr6_KI270802v1_alt,length=75005>
##contig=<ID=chr6_KB021644v2_alt,length=185823>
##contig=<ID=chr6_KI270797v1_alt,length=197536>
##contig=<ID=chr6_KI270798v1_alt,length=271782>
##contig=<ID=chr7_KI270804v1_alt,length=157952>
##contig=<ID=chr7_KI270809v1_alt,length=209586>
##contig=<ID=chr7_KI270806v1_alt,length=158166>
##contig=<ID=chr7_GL383534v2_alt,length=119183>
##contig=<ID=chr7_KI270803v1_alt,length=1111570>
##contig=<ID=chr7_KI270808v1_alt,length=271455>
##contig=<ID=chr7_KI270807v1_alt,length=126434>
##contig=<ID=chr7_KI270805v1_alt,length=209988>
##contig=<ID=chr8_KI270818v1_alt,length=145606>
##contig=<ID=chr8_KI270812v1_alt,length=282736>
##contig=<ID=chr8_KI270811v1_alt,length=292436>
##contig=<ID=chr8_KI270821v1_alt,length=985506>
##contig=<ID=chr8_KI270813v1_alt,length=300230>
##contig=<ID=chr8_KI270822v1_alt,length=624492>
##contig=<ID=chr8_KI270814v1_alt,length=141812>
##contig=<ID=chr8_KI270810v1_alt,length=374415>
##contig=<ID=chr8_KI270819v1_alt,length=133535>
##contig=<ID=chr8_KI270820v1_alt,length=36640>
##contig=<ID=chr8_KI270817v1_alt,length=158983>
##contig=<ID=chr8_KI270816v1_alt,length=305841>
##contig=<ID=chr8_KI270815v1_alt,length=132244>
##contig=<ID=chr9_GL383539v1_alt,length=162988>
##contig=<ID=chr9_GL383540v1_alt,length=71551>
##contig=<ID=chr9_GL383541v1_alt,length=171286>
##contig=<ID=chr9_GL383542v1_alt,length=60032>
##contig=<ID=chr9_KI270823v1_alt,length=439082>
##contig=<ID=chr10_GL383545v1_alt,length=179254>
##contig=<ID=chr10_KI270824v1_alt,length=181496>
##contig=<ID=chr10_GL383546v1_alt,length=309802>
##contig=<ID=chr10_KI270825v1_alt,length=188315>
##contig=<ID=chr11_KI270832v1_alt,length=210133>
##contig=<ID=chr11_KI270830v1_alt,length=177092>
##contig=<ID=chr11_KI270831v1_alt,length=296895>
##contig=<ID=chr11_KI270829v1_alt,length=204059>
##contig=<ID=chr11_GL383547v1_alt,length=154407>
##contig=<ID=chr11_JH159136v1_alt,length=200998>
##contig=<ID=chr11_JH159137v1_alt,length=191409>
##contig=<ID=chr11_KI270827v1_alt,length=67707>
##contig=<ID=chr11_KI270826v1_alt,length=186169>
##contig=<ID=chr12_GL877875v1_alt,length=167313>
##contig=<ID=chr12_GL877876v1_alt,length=408271>
##contig=<ID=chr12_KI270837v1_alt,length=40090>
##contig=<ID=chr12_GL383549v1_alt,length=120804>
##contig=<ID=chr12_KI270835v1_alt,length=238139>
##contig=<ID=chr12_GL383550v2_alt,length=169178>
##contig=<ID=chr12_GL383552v1_alt,length=138655>
##contig=<ID=chr12_GL383553v2_alt,length=152874>
##contig=<ID=chr12_KI270834v1_alt,length=119498>
##contig=<ID=chr12_GL383551v1_alt,length=184319>
##contig=<ID=chr12_KI270833v1_alt,length=76061>
##contig=<ID=chr12_KI270836v1_alt,length=56134>
##contig=<ID=chr13_KI270840v1_alt,length=191684>
##contig=<ID=chr13_KI270839v1_alt,length=180306>
##contig=<ID=chr13_KI270843v1_alt,length=103832>
##contig=<ID=chr13_KI270841v1_alt,length=169134>
##contig=<ID=chr13_KI270838v1_alt,length=306913>
##contig=<ID=chr13_KI270842v1_alt,length=37287>
##contig=<ID=chr14_KI270844v1_alt,length=322166>
##contig=<ID=chr14_KI270847v1_alt,length=1511111>
##contig=<ID=chr14_KI270845v1_alt,length=180703>
##contig=<ID=chr14_KI270846v1_alt,length=1351393>
##contig=<ID=chr15_KI270852v1_alt,length=478999>
##contig=<ID=chr15_KI270851v1_alt,length=263054>
##contig=<ID=chr15_KI270848v1_alt,length=327382>
##contig=<ID=chr15_GL383554v1_alt,length=296527>
##contig=<ID=chr15_KI270849v1_alt,length=244917>
##contig=<ID=chr15_GL383555v2_alt,length=388773>
##contig=<ID=chr15_KI270850v1_alt,length=430880>
##contig=<ID=chr16_KI270854v1_alt,length=134193>
##contig=<ID=chr16_KI270856v1_alt,length=63982>
##contig=<ID=chr16_KI270855v1_alt,length=232857>
##contig=<ID=chr16_KI270853v1_alt,length=2659700>
##contig=<ID=chr16_GL383556v1_alt,length=192462>
##contig=<ID=chr16_GL383557v1_alt,length=89672>
##contig=<ID=chr17_GL383563v3_alt,length=375691>
##contig=<ID=chr17_KI270862v1_alt,length=391357>
##contig=<ID=chr17_KI270861v1_alt,length=196688>
##contig=<ID=chr17_KI270857v1_alt,length=2877074>
##contig=<ID=chr17_JH159146v1_alt,length=278131>
##contig=<ID=chr17_JH159147v1_alt,length=70345>
##contig=<ID=chr17_GL383564v2_alt,length=133151>
##contig=<ID=chr17_GL000258v2_alt,length=1821992>
##contig=<ID=chr17_GL383565v1_alt,length=223995>
##contig=<ID=chr17_KI270858v1_alt,length=235827>
##contig=<ID=chr17_KI270859v1_alt,length=108763>
##contig=<ID=chr17_GL383566v1_alt,length=90219>
##contig=<ID=chr17_KI270860v1_alt,length=178921>
##contig=<ID=chr18_KI270864v1_alt,length=111737>
##contig=<ID=chr18_GL383567v1_alt,length=289831>
##contig=<ID=chr18_GL383570v1_alt,length=164789>
##contig=<ID=chr18_GL383571v1_alt,length=198278>
##contig=<ID=chr18_GL383568v1_alt,length=104552>
##contig=<ID=chr18_GL383569v1_alt,length=167950>
##contig=<ID=chr18_GL383572v1_alt,length=159547>
##contig=<ID=chr18_KI270863v1_alt,length=167999>
##contig=<ID=chr19_KI270868v1_alt,length=61734>
##contig=<ID=chr19_KI270865v1_alt,length=52969>
##contig=<ID=chr19_GL383573v1_alt,length=385657>
##contig=<ID=chr19_GL383575v2_alt,length=170222>
##contig=<ID=chr19_GL383576v1_alt,length=188024>
##contig=<ID=chr19_GL383574v1_alt,length=155864>
##contig=<ID=chr19_KI270866v1_alt,length=43156>
##contig=<ID=chr19_KI270867v1_alt,length=233762>
##contig=<ID=chr19_GL949746v1_alt,length=987716>
##contig=<ID=chr20_GL383577v2_alt,length=128386>
##contig=<ID=chr20_KI270869v1_alt,length=118774>
##contig=<ID=chr20_KI270871v1_alt,length=58661>
##contig=<ID=chr20_KI270870v1_alt,length=183433>
##contig=<ID=chr21_GL383578v2_alt,length=63917>
##contig=<ID=chr21_KI270874v1_alt,length=166743>
##contig=<ID=chr21_KI270873v1_alt,length=143900>
##contig=<ID=chr21_GL383579v2_alt,length=201197>
##contig=<ID=chr21_GL383580v2_alt,length=74653>
##contig=<ID=chr21_GL383581v2_alt,length=116689>
##contig=<ID=chr21_KI270872v1_alt,length=82692>
##contig=<ID=chr22_KI270875v1_alt,length=259914>
##contig=<ID=chr22_KI270878v1_alt,length=186262>
##contig=<ID=chr22_KI270879v1_alt,length=304135>
##contig=<ID=chr22_KI270876v1_alt,length=263666>
##contig=<ID=chr22_KI270877v1_alt,length=101331>
##contig=<ID=chr22_GL383583v2_alt,length=96924>
##contig=<ID=chr22_GL383582v2_alt,length=162811>
##contig=<ID=chrX_KI270880v1_alt,length=284869>
##contig=<ID=chrX_KI270881v1_alt,length=144206>
##contig=<ID=chr19_KI270882v1_alt,length=248807>
##contig=<ID=chr19_KI270883v1_alt,length=170399>
##contig=<ID=chr19_KI270884v1_alt,length=157053>
##contig=<ID=chr19_KI270885v1_alt,length=171027>
##contig=<ID=chr19_KI270886v1_alt,length=204239>
##contig=<ID=chr19_KI270887v1_alt,length=209512>
##contig=<ID=chr19_KI270888v1_alt,length=155532>
##contig=<ID=chr19_KI270889v1_alt,length=170698>
##contig=<ID=chr19_KI270890v1_alt,length=184499>
##contig=<ID=chr19_KI270891v1_alt,length=170680>
##contig=<ID=chr1_KI270892v1_alt,length=162212>
##contig=<ID=chr2_KI270894v1_alt,length=214158>
##contig=<ID=chr2_KI270893v1_alt,length=161218>
##contig=<ID=chr3_KI270895v1_alt,length=162896>
##contig=<ID=chr4_KI270896v1_alt,length=378547>
##contig=<ID=chr5_KI270897v1_alt,length=1144418>
##contig=<ID=chr5_KI270898v1_alt,length=130957>
##contig=<ID=chr6_GL000251v2_alt,length=4795265>
##contig=<ID=chr7_KI270899v1_alt,length=190869>
##contig=<ID=chr8_KI270901v1_alt,length=136959>
##contig=<ID=chr8_KI270900v1_alt,length=318687>
##contig=<ID=chr11_KI270902v1_alt,length=106711>
##contig=<ID=chr11_KI270903v1_alt,length=214625>
##contig=<ID=chr12_KI270904v1_alt,length=572349>
##contig=<ID=chr15_KI270906v1_alt,length=196384>
##contig=<ID=chr15_KI270905v1_alt,length=5161414>
##contig=<ID=chr17_KI270907v1_alt,length=137721>
##contig=<ID=chr17_KI270910v1_alt,length=157099>
##contig=<ID=chr17_KI270909v1_alt,length=325800>
##contig=<ID=chr17_JH159148v1_alt,length=88070>
##contig=<ID=chr17_KI270908v1_alt,length=1423190>
##contig=<ID=chr18_KI270912v1_alt,length=174061>
##contig=<ID=chr18_KI270911v1_alt,length=157710>
##contig=<ID=chr19_GL949747v2_alt,length=729520>
##contig=<ID=chr22_KB663609v1_alt,length=74013>
##contig=<ID=chrX_KI270913v1_alt,length=274009>
##contig=<ID=chr19_KI270914v1_alt,length=205194>
##contig=<ID=chr19_KI270915v1_alt,length=170665>
##contig=<ID=chr19_KI270916v1_alt,length=184516>
##contig=<ID=chr19_KI270917v1_alt,length=190932>
##contig=<ID=chr19_KI270918v1_alt,length=123111>
##contig=<ID=chr19_KI270919v1_alt,length=170701>
##contig=<ID=chr19_KI270920v1_alt,length=198005>
##contig=<ID=chr19_KI270921v1_alt,length=282224>
##contig=<ID=chr19_KI270922v1_alt,length=187935>
##contig=<ID=chr19_KI270923v1_alt,length=189352>
##contig=<ID=chr3_KI270924v1_alt,length=166540>
##contig=<ID=chr4_KI270925v1_alt,length=555799>
##contig=<ID=chr6_GL000252v2_alt,length=4604811>
##contig=<ID=chr8_KI270926v1_alt,length=229282>
##contig=<ID=chr11_KI270927v1_alt,length=218612>
##contig=<ID=chr19_GL949748v2_alt,length=1064304>
##contig=<ID=chr22_KI270928v1_alt,length=176103>
##contig=<ID=chr19_KI270929v1_alt,length=186203>
##contig=<ID=chr19_KI270930v1_alt,length=200773>
##contig=<ID=chr19_KI270931v1_alt,length=170148>
##contig=<ID=chr19_KI270932v1_alt,length=215732>
##contig=<ID=chr19_KI270933v1_alt,length=170537>
##contig=<ID=chr19_GL000209v2_alt,length=177381>
##contig=<ID=chr3_KI270934v1_alt,length=163458>
##contig=<ID=chr6_GL000253v2_alt,length=4677643>
##contig=<ID=chr19_GL949749v2_alt,length=1091841>
##contig=<ID=chr3_KI270935v1_alt,length=197351>
##contig=<ID=chr6_GL000254v2_alt,length=4827813>
##contig=<ID=chr19_GL949750v2_alt,length=1066390>
##contig=<ID=chr3_KI270936v1_alt,length=164170>
##contig=<ID=chr6_GL000255v2_alt,length=4606388>
##contig=<ID=chr19_GL949751v2_alt,length=1002683>
##contig=<ID=chr3_KI270937v1_alt,length=165607>
##contig=<ID=chr6_GL000256v2_alt,length=4929269>
##contig=<ID=chr19_GL949752v1_alt,length=987100>
##contig=<ID=chr6_KI270758v1_alt,length=76752>
##contig=<ID=chr19_GL949753v2_alt,length=796479>
##contig=<ID=chr19_KI270938v1_alt,length=1066800>
##contig=<ID=chrM,length=16569>
##contig=<ID=chrUn_KI270302v1,length=2274>
##contig=<ID=chrUn_KI270304v1,length=2165>
##contig=<ID=chrUn_KI270303v1,length=1942>
##contig=<ID=chrUn_KI270305v1,length=1472>
##contig=<ID=chrUn_KI270322v1,length=21476>
##contig=<ID=chrUn_KI270320v1,length=4416>
##contig=<ID=chrUn_KI270310v1,length=1201>
##contig=<ID=chrUn_KI270316v1,length=1444>
##contig=<ID=chrUn_KI270315v1,length=2276>
##contig=<ID=chrUn_KI270312v1,length=998>
##contig=<ID=chrUn_KI270311v1,length=12399>
##contig=<ID=chrUn_KI270317v1,length=37690>
##contig=<ID=chrUn_KI270412v1,length=1179>
##contig=<ID=chrUn_KI270411v1,length=2646>
##contig=<ID=chrUn_KI270414v1,length=2489>
##contig=<ID=chrUn_KI270419v1,length=1029>
##contig=<ID=chrUn_KI270418v1,length=2145>
##contig=<ID=chrUn_KI270420v1,length=2321>
##contig=<ID=chrUn_KI270424v1,length=2140>
##contig=<ID=chrUn_KI270417v1,length=2043>
##contig=<ID=chrUn_KI270422v1,length=1445>
##contig=<ID=chrUn_KI270423v1,length=981>
##contig=<ID=chrUn_KI270425v1,length=1884>
##contig=<ID=chrUn_KI270429v1,length=1361>
##contig=<ID=chrUn_KI270442v1,length=392061>
##contig=<ID=chrUn_KI270466v1,length=1233>
##contig=<ID=chrUn_KI270465v1,length=1774>
##contig=<ID=chrUn_KI270467v1,length=3920>
##contig=<ID=chrUn_KI270435v1,length=92983>
##contig=<ID=chrUn_KI270438v1,length=112505>
##contig=<ID=chrUn_KI270468v1,length=4055>
##contig=<ID=chrUn_KI270510v1,length=2415>
##contig=<ID=chrUn_KI270509v1,length=2318>
##contig=<ID=chrUn_KI270518v1,length=2186>
##contig=<ID=chrUn_KI270508v1,length=1951>
##contig=<ID=chrUn_KI270516v1,length=1300>
##contig=<ID=chrUn_KI270512v1,length=22689>
##contig=<ID=chrUn_KI270519v1,length=138126>
##contig=<ID=chrUn_KI270522v1,length=5674>
##contig=<ID=chrUn_KI270511v1,length=8127>
##contig=<ID=chrUn_KI270515v1,length=6361>
##contig=<ID=chrUn_KI270507v1,length=5353>
##contig=<ID=chrUn_KI270517v1,length=3253>
##contig=<ID=chrUn_KI270529v1,length=1899>
##contig=<ID=chrUn_KI270528v1,length=2983>
##contig=<ID=chrUn_KI270530v1,length=2168>
##contig=<ID=chrUn_KI270539v1,length=993>
##contig=<ID=chrUn_KI270538v1,length=91309>
##contig=<ID=chrUn_KI270544v1,length=1202>
##contig=<ID=chrUn_KI270548v1,length=1599>
##contig=<ID=chrUn_KI270583v1,length=1400>
##contig=<ID=chrUn_KI270587v1,length=2969>
##contig=<ID=chrUn_KI270580v1,length=1553>
##contig=<ID=chrUn_KI270581v1,length=7046>
##contig=<ID=chrUn_KI270579v1,length=31033>
##contig=<ID=chrUn_KI270589v1,length=44474>
##contig=<ID=chrUn_KI270590v1,length=4685>
##contig=<ID=chrUn_KI270584v1,length=4513>
##contig=<ID=chrUn_KI270582v1,length=6504>
##contig=<ID=chrUn_KI270588v1,length=6158>
##contig=<ID=chrUn_KI270593v1,length=3041>
##contig=<ID=chrUn_KI270591v1,length=5796>
##contig=<ID=chrUn_KI270330v1,length=1652>
##contig=<ID=chrUn_KI270329v1,length=1040>
##contig=<ID=chrUn_KI270334v1,length=1368>
##contig=<ID=chrUn_KI270333v1,length=2699>
##contig=<ID=chrUn_KI270335v1,length=1048>
##contig=<ID=chrUn_KI270338v1,length=1428>
##contig=<ID=chrUn_KI270340v1,length=1428>
##contig=<ID=chrUn_KI270336v1,length=1026>
##contig=<ID=chrUn_KI270337v1,length=1121>
##contig=<ID=chrUn_KI270363v1,length=1803>
##contig=<ID=chrUn_KI270364v1,length=2855>
##contig=<ID=chrUn_KI270362v1,length=3530>
##contig=<ID=chrUn_KI270366v1,length=8320>
##contig=<ID=chrUn_KI270378v1,length=1048>
##contig=<ID=chrUn_KI270379v1,length=1045>
##contig=<ID=chrUn_KI270389v1,length=1298>
##contig=<ID=chrUn_KI270390v1,length=2387>
##contig=<ID=chrUn_KI270387v1,length=1537>
##contig=<ID=chrUn_KI270395v1,length=1143>
##contig=<ID=chrUn_KI270396v1,length=1880>
##contig=<ID=chrUn_KI270388v1,length=1216>
##contig=<ID=chrUn_KI270394v1,length=970>
##contig=<ID=chrUn_KI270386v1,length=1788>
##contig=<ID=chrUn_KI270391v1,length=1484>
##contig=<ID=chrUn_KI270383v1,length=1750>
##contig=<ID=chrUn_KI270393v1,length=1308>
##contig=<ID=chrUn_KI270384v1,length=1658>
##contig=<ID=chrUn_KI270392v1,length=971>
##contig=<ID=chrUn_KI270381v1,length=1930>
##contig=<ID=chrUn_KI270385v1,length=990>
##contig=<ID=chrUn_KI270382v1,length=4215>
##contig=<ID=chrUn_KI270376v1,length=1136>
##contig=<ID=chrUn_KI270374v1,length=2656>
##contig=<ID=chrUn_KI270372v1,length=1650>
##contig=<ID=chrUn_KI270373v1,length=1451>
##contig=<ID=chrUn_KI270375v1,length=2378>
##contig=<ID=chrUn_KI270371v1,length=2805>
##contig=<ID=chrUn_KI270448v1,length=7992>
##contig=<ID=chrUn_KI270521v1,length=7642>
##contig=<ID=chrUn_GL000195v1,length=182896>
##contig=<ID=chrUn_GL000219v1,length=179198>
##contig=<ID=chrUn_GL000220v1,length=161802>
##contig=<ID=chrUn_GL000224v1,length=179693>
##contig=<ID=chrUn_KI270741v1,length=157432>
##contig=<ID=chrUn_GL000226v1,length=15008>
##contig=<ID=chrUn_GL000213v1,length=164239>
##contig=<ID=chrUn_KI270743v1,length=210658>
##contig=<ID=chrUn_KI270744v1,length=168472>
##contig=<ID=chrUn_KI270745v1,length=41891>
##contig=<ID=chrUn_KI270746v1,length=66486>
##contig=<ID=chrUn_KI270747v1,length=198735>
##contig=<ID=chrUn_KI270748v1,length=93321>
##contig=<ID=chrUn_KI270749v1,length=158759>
##contig=<ID=chrUn_KI270750v1,length=148850>
##contig=<ID=chrUn_KI270751v1,length=150742>
##contig=<ID=chrUn_KI270752v1,length=27745>
##contig=<ID=chrUn_KI270753v1,length=62944>
##contig=<ID=chrUn_KI270754v1,length=40191>
##contig=<ID=chrUn_KI270755v1,length=36723>
##contig=<ID=chrUn_KI270756v1,length=79590>
##contig=<ID=chrUn_KI270757v1,length=71251>
##contig=<ID=chrUn_GL000214v1,length=137718>
##contig=<ID=chrUn_KI270742v1,length=186739>
##contig=<ID=chrUn_GL000216v2,length=176608>
##contig=<ID=chrUn_GL000218v1,length=161147>
##contig=<ID=chrX,length=156040895>
##contig=<ID=chrY,length=57227415>
##contig=<ID=chrY_KI270740v1_random,length=37240>""")
    vcf_head.append("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT")
    assert os.path.exists(filepath)
    vcfOut = []
    if str(filetype).lower() == "maf":
        with open(filepath) as inf:
            for line in inf:
                linestrip = line.strip()
                if linestrip.startswith("#"):
                    continue
                if linestrip.startswith("version"):
                    continue
                if linestrip.startswith("Hugo_Symbol"):
                    continue
                lineList = linestrip.split("\t")
                
                lineOut = "\t".join(lineList[4:6]) +'\t.\t' + lineList[10] +'\t' + lineList[12] +'\t.\t.\t.\tGT:AD:AF:ALT_F1R2:ALT_F2R1:FOXOG:QSS:REF_F1R2:REF_F2R1'
                if not lineOut.upper().startswith("CHR"):
                    vcfOut.append("chr"+ lineOut)
                else:
                    vcfOut.append(lineOut)
        with open(outfile,"w") as outf:
            outf.write(
                "\n".join(vcf_head) +"\n"+ "\n".join(vcfOut)
            )
    elif str(filetype).lower() == "5coltsv":
        with open(filepath) as inf:
            for line in inf:
                if line.strip().startswith("#"):
                    continue
                lineList = line.strip().split("\t")
                
                lineOut = "\t".join(lineList[0:2]) +'\t.\t' + lineList[3] +'\t' + lineList[4] +'\t.\t.\t.\tGT:AD:AF:ALT_F1R2:ALT_F2R1:FOXOG:QSS:REF_F1R2:REF_F2R1'
                if not lineOut.upper().startswith("CHR"):
                    vcfOut.append("chr"+ lineOut)
                else:
                    vcfOut.append(lineOut)
        with open(outfile,"w") as outf:
            outf.write(
                "\n".join(vcf_head) +"\n"+ "\n".join(vcfOut)
            )                    



# def convert(input, out,type):
#     if os.path.exists(input):
#         if type=="5coltsv":
#             vcfdata = pd.read_csv(input, sep='\t', header=0)
#             vcfdata = vcfdata.drop(columns=vcfdata.columns[2])
#             # vcfdata.insert(vcfdata.shape[1],'ID','.')
#             vcfdata = vcfdata.reindex(columns=[
#                                       'Chromosome', 'Start_Position', 'Reference_Allele', 'Tumor_Seq_Allele2', 'dbSNP_RS'], fill_value='.')
#             tumor_meta = "0/1:0,0:0.00"
#             vcfdata.insert(vcfdata.shape[1], 'tumor_meta', tumor_meta)
#         elif type=="maf":
#             with open(input) as inf:
#                 content = []
#                 for line in inf:
#                     if line.startswith("#"):
#                         continue
#                     content.append(line.strip("\n").split("\t"))
#             data = pd.DataFrame(content[1:], columns=content[0])
#             index_list = [4, 5, 10, 12, 13]
#             vcfdata = data.iloc[:, index_list]
#             vcfdata.iloc[:, 4] = data.iloc[:, 13].replace('', '.', regex=True)
#             t_ref = data['t_ref_count'].astype("int")
#             t_alt = data['t_alt_count'].astype("int")
#             af = []
#             for a,b in zip(t_alt, t_ref):
#                 try:
#                     ttt = round(a / b, 2)
#                     af.append(ttt)
#                 except:
#                     af.append(0)
#             tumor_meta = []
#             for i in range(data.shape[0]):
#                 ad = ",".join([data['t_ref_count'][i], data['t_alt_count'][i]])
#                 meta = "0/1:"+ad+":"+str(af[i])
#                 tumor_meta.append(meta)
#             vcfdata.insert(vcfdata.shape[1], 'tumor_meta', tumor_meta)

#         else:
#             raise TypeError('File type error!')
#         # vcfdata['Start_Position']=vcfdata['Start_Position'].astype("str")
#         qual = '.'
#         filter = 'PASS'
#         info = '.'
#         format = 'GT:AD:AF'
#         normal = "0/0:0,0:0.00"
#         vcfdata.insert(vcfdata.shape[1], 'qual', qual)
#         vcfdata.insert(vcfdata.shape[1], 'filter', filter)
#         vcfdata.insert(vcfdata.shape[1], 'info', info)
#         vcfdata.insert(vcfdata.shape[1], 'format', format)
#         vcfdata.insert(vcfdata.shape[1], 'normal', normal)
#         vcf_head = []
#         vcf_head.append("##fileformat=VCFv4.2")
#         vcf_head.append(
#             "##FILTER=<ID=PASS,Description=\"Site filtered because more than two alt alleles pass tumor LOD\">")
#         # vcf_head.append(
#         #     "##INFO=<ID=DB,Number=0,Type=Flag,Description=\"dbSNP Membership\">")
#         vcf_head.append(
#             "##FORMAT=<ID=GT,Number=1,Type=String,Description=\"Genotype\">")
#         vcf_head.append(
#             "##FORMAT=<ID=AD,Number=.,Type=Integer,Description=\"Allelic depths for the ref and alt alleles in the order listed\">")
#         vcf_head.append(
#             "##FORMAT=<ID=AF,Number=1,Type=Float,Description=\"Allele fraction of the event in the tumor\">")
#         vcf_head.append("##contig=<ID=chr1,length=248956422>\n##contig=<ID=chr2,length=242193529>\n##contig=<ID=chr3,length=198295559>\n##contig=<ID=chr4,length=190214555>\n##contig=<ID=chr5,length=181538259>\n##contig=<ID=chr6,length=170805979>\n##contig=<ID=chr7,length=159345973>\n##contig=<ID=chr8,length=145138636>\n##contig=<ID=chr9,length=138394717>\n##contig=<ID=chr10,length=133797422>\n##contig=<ID=chr11,length=135086622>\n##contig=<ID=chr12,length=133275309>\n##contig=<ID=chr13,length=114364328>\n##contig=<ID=chr14,length=107043718>\n##contig=<ID=chr15,length=101991189>\n##contig=<ID=chr16,length=90338345>\n##contig=<ID=chr17,length=83257441>\n##contig=<ID=chr18,length=80373285>\n##contig=<ID=chr19,length=58617616>\n##contig=<ID=chr20,length=64444167>\n##contig=<ID=chr21,length=46709983>\n##contig=<ID=chr22,length=50818468>\n##contig=<ID=chrX,length=156040895>\n##contig=<ID=chrY,length=57227415>")
#         meta = "\n".join(vcf_head)
#         vcf_header = ["#CHROM", "POS", "ID", "REF", "ALT",
#                       "QUAL", "FILTER", "INFO", "FORMAT", "NORMAL", "TUMOR"]
#         data_vcf = {vcf_header[0]: vcfdata.loc[:, 'Chromosome'], vcf_header[1]: vcfdata.loc[:, 'Start_Position'].astype(
#             "int"), vcf_header[2]: vcfdata.loc[:, 'dbSNP_RS'], vcf_header[3]: vcfdata.loc[:, 'Reference_Allele'], vcf_header[4]: vcfdata.loc[:, 'Tumor_Seq_Allele2'], vcf_header[5]: vcfdata.loc[:, 'qual'], vcf_header[6]: vcfdata.loc[:, 'filter'], vcf_header[7]: vcfdata.loc[:, 'info'], vcf_header[8]: vcfdata.loc[:, 'format'], vcf_header[9]: vcfdata.loc[:, 'normal'], vcf_header[10]: vcfdata.loc[:, 'tumor_meta']}
#         vcf_data = pd.DataFrame(data_vcf)
#         chrom = ["chr"+str(n) for n in range(1, 23)]
#         chrom.extend(['chrX', 'chrY'])
#         vcf_data['#CHROM'] = vcf_data['#CHROM'].astype('category')
#         vcf_data['#CHROM'].cat.reorder_categories(chrom, inplace=True)
#         vcf_data.sort_values(by=['#CHROM', 'POS'], ascending=[
#                              True, True], inplace=True)
#         # vcf_data = pd.concat(
#         #     [vcf_data_sub, pd.DataFrame(columns=vcf_header[5:])], sort=False)
#         with open(out, 'w') as outf:
#             outf.write(meta+"\n")
#         vcf_data.to_csv(out, mode='a', sep='\t', index=False, header=True)
#         return True
#     else:
#         return False





global null_str
null_str = "NULL"

class myVariantObj():

    def __init__(self,varlist):
        '''
        common procedure:
            1. parse info to kv
            2. clean and statistic (if there is a need)
        '''
        self.varlist = varlist

        self.out = OrderedDict()
        # origin chr pos ..
        self.originblock = self.__parse_origin(self.varlist) #OrderedDict

        # parse INFO into dict 
        self.INFO_Dict = self.__parse_INFO2Dict(varlist[7]) # parse INFO to dict and check format. all other steps are based on this dict

        # parse DOCM 
        self.DOCMblock = self.__parse_docm(self.INFO_Dict)
        logging.debug("parse the DOCM block : {}".format(json.dumps(self.DOCMblock)))

        # parse vep 
        self.vepblock = self.__parse_vep(self.INFO_Dict)

        # parse annoar
        self.annovarblock = self.__parse_annovar(self.INFO_Dict)

        # parse cosmic coding
        self.cosmic_coding = self.__parse_cosmic_coding(self.INFO_Dict)

        # parse cosmic non coding 
        self.cosmic_non_coding = self.__parse_cosmic_noncoding(self.INFO_Dict)

        # parse civic
        self.civic = self.__parse_civic(self.INFO_Dict)
        
        # parse cancerhotspots 
        self.cancerhotspots = self.__parse_cancerhotspots(self.INFO_Dict)

        # parse cgi
        self.cgi  = self.__parse_cgi(self.INFO_Dict)

        self.out["origin"] = self.originblock
        self.out['vep'] = self.vepblock
        self.out['annovar'] = self.annovarblock
        self.out['DOCM'] = self.DOCMblock
        self.out['cosmic_coding'] = self.cosmic_coding
        self.out['cosmic_non_coding'] = self.cosmic_non_coding
        self.out['civic'] = self.civic
        self.out['cancerhotspots'] = self.cancerhotspots
        self.out['cgi'] = self.cgi

    def get_jsonObj(self):
        return(self.out)

    def __parse_INFO2Dict(self,INFO):
        """
        parse INFO字段到字典，过滤不是k=v的结构。
        """

        InfoDict = OrderedDict()
        if " " in INFO:
            logging.error("witespace in INFO field")
            exit(1)
        for info in INFO.strip("\n").split(";"):
            if "=" not in info:
                logging.warning("the item ' {} ' in INFO field is not valid".format(info))
                continue
            else:
                listinfo = info.strip().split("=")
                if len(listinfo) ==2:
                    k,v = listinfo
                else: # the length must larger than 2
                    k = listinfo[0]
                    v = "".join(listinfo[1:])
                    logging.info(info)
                InfoDict[k] = v
        return(InfoDict)
  
    def __parse_origin(self,varlist):
        ''' return origin sub block'''
        origin_subblock = OrderedDict()
        origin_subblock['chrom'] = varlist[0]
        origin_subblock['pos'] =   varlist[1]
        origin_subblock['ID'] =    varlist[2]
        origin_subblock['REF'] =   varlist[3]
        origin_subblock['ALT'] =   varlist[4]
        origin_subblock['QUAL'] =  varlist[5]
        origin_subblock['FLT'] =   varlist[6]
        return(origin_subblock)

    # def __parse_uniqmeta(self,varlist):
    #     pass

    def __parse_docm(self,InfoDict):
        """
            {
                "MeSH": {
                    "D002292": {
                        "ID": "D002292",
                        "effect": {
                            "Likely_pathogenic": ["PMID:26619011"]
                        }
                    },
                    "D001943": {
                        "ID": "D001943",
                        "effect": {
                            "Likely_pathogenic": ["PMID:26619011"]
                        }
                    }	
                },
                "UMLS": {
                    "C0278701": {
                        "ID": "C0278701",
                        "effect": {
                            "Likely_pathogenic": ["PMID:26619011"]
                        }
                    },
                    "C0153574": {
                        "ID": "C0153574",
                        "effect": {
                            "Likely_pathogenic": ["PMID:26619011"]
                        }
                    }
                }
            }
            summary的格式是下列的格式,
            {
                "DOXX":{
                    "source":MESH,
                    PMID:[],
                    "effect":[]
                }
            }
        """
        
        out = {"MeSH":{},"UMLS":{}}

        DOCM_DiseaseAndClinicalSignificance = InfoDict.get("DOCM_DiseaseAndClinicalSignificance",False)
        # logging.debug(DOCM_DiseaseAndClinicalSignificance)
        if DOCM_DiseaseAndClinicalSignificance:
           docmlist = DOCM_DiseaseAndClinicalSignificance.split("&&")
           logging.debug(docmlist)
           for it in docmlist:
                db,ID,effect,PMIDs = it.split("|")

                if db.strip() == "MeSH":
                    if ID not in out["MeSH"].keys():
                        out["MeSH"][ID] = {
                                "ID":ID,
                                "effect":{
                                    effect:[i.strip() for i in PMIDs.split(",")]
                                }
                            }
                    else:
                        aeffect = out["MeSH"][ID]["effect"].copy()
                        if effect not in aeffect.keys():
                            aeffect[effect] = [i.strip() for i in PMIDs.split(",")]
                        else:
                            xeffect = aeffect[effect].copy()
                            xeffect.extend([i.strip() for i in PMIDs.split(",")])
                            xeffect = list(set(xeffect))
                            aeffect[effect] =xeffect
                        out["MeSH"][ID]["effect"] =  aeffect
                elif   db.strip() == "UMLS":       
                    if ID not in out["UMLS"].keys():
                        out["UMLS"][ID] = {
                                "ID":ID,
                                "effect":{
                                    effect:[i.strip() for i in PMIDs.split(",")]
                                }
                            }
                    else:
                        aeffect = out["UMLS"][ID]["effect"].copy()
                        if effect not in aeffect.keys():
                            aeffect[effect] = [i.strip() for i in PMIDs.split(",")]
                        else:
                            xeffect = aeffect[effect].copy()
                            xeffect.extend([i.strip() for i in PMIDs.split(",")])
                            xeffect = list(set(xeffect))
                            aeffect[effect] =xeffect
                        out["UMLS"][ID]["effect"] =  aeffect
        return(out)

    def __parse_vep(self,INFOdict):
        """
        parse vep in INFO
        data schema:
        [
            {
                k:v
            },
            {

            }
        ]
        
        """

        def parse_one_record_in_vep(record):
            out = {}
            headline = ["Allele", "Consequence", "IMPACT", "SYMBOL",
            "Gene", "Feature_type", "Feature", "BIOTYPE", "EXON", 
            "INTRON", "HGVSc", "HGVSp", "cDNA_position", "CDS_position",
            "Protein_position", "Amino_acids", "Codons", "Existing_variation", 
            "DISTANCE", "STRAND", "FLAGS", "VARIANT_CLASS", "SYMBOL_SOURCE",
            "HGNC_ID", "CANONICAL", "MANE_SELECT", "MANE_PLUS_CLINICAL", "TSL",
            "APPRIS", "CCDS", "ENSP", "SWISSPROT", "TREMBL", "UNIPARC",
            "UNIPROT_ISOFORM", "GENE_PHENO", "SIFT", "PolyPhen", "DOMAINS", 
            "miRNA", "HGVS_OFFSET", "AF", "AFR_AF", "AMR_AF", "EAS_AF", "EUR_AF",
            "SAS_AF", "AA_AF", "EA_AF", "gnomAD_AF", "gnomAD_AFR_AF", "gnomAD_AMR_AF",
            "gnomAD_ASJ_AF", "gnomAD_EAS_AF", "gnomAD_FIN_AF", "gnomAD_NFE_AF", 
            "gnomAD_OTH_AF", "gnomAD_SAS_AF", "MAX_AF", "MAX_AF_POPS", "CLIN_SIG", 
            "SOMATIC", "PHENO", "PUBMED", "MOTIF_NAME", "MOTIF_POS", "HIGH_INF_POS", 
            "MOTIF_SCORE_CHANGE", "TRANSCRIPTION_FACTORS"]
            recordlist = record.split("|")
            for k,r in enumerate(recordlist):
                if r.strip() != "":
                    out[headline[k]] = r
                else:
                    out[headline[k]] = null_str
            logging.debug(out)
            return(out)
        
        dat = INFOdict['CSQ']
        datlist =[i.strip(" ") for i in  dat.strip("\n").split(",")]
        out = []
        logging.debug(datlist)
        for record in datlist:
            out.append(parse_one_record_in_vep(record))
        return(out)

    def __parse_annovar(self,INFOdict):
        """
        parse annovar into dict
        """
        out = {}
        headline =  ["Func.refGene", "Gene.refGene", "GeneDetail.refGene", "ExonicFunc.refGene", 
        "AAChange.refGene", "Func.ensGene", "Gene.ensGene", "GeneDetail.ensGene", 
        "ExonicFunc.ensGene", "AAChange.ensGene", "Func.knownGene", "Gene.knownGene", 
        "GeneDetail.knownGene", "ExonicFunc.knownGene", "AAChange.knownGene", "cytoBand", 
        "avsnp150", "DamagePredCount", "SIFT_pred", "SIFT4G_pred", "Polyphen2_HDIV_pred", 
        "Polyphen2_HVAR_pred", "LRT_pred", "MutationTaster_pred", "MutationAssessor_pred", 
        "FATHMM_pred", "PROVEAN_pred", "VEST4_score", "MetaSVM_pred", "MetaLR_pred", "M-CAP_pred", 
        "REVEL_score", "MutPred_score", "MVP_score", "MPC_score", "PrimateAI_pred", "DEOGEN2_pred", 
        "BayesDel_addAF_pred", "BayesDel_noAF_pred", "ClinPred_pred", "LIST-S2_pred", "CADD_raw", 
        "CADD_phred", "DANN_score", "fathmm-MKL_coding_pred", "fathmm-XF_coding_pred", 
        "Eigen-raw_coding", "Eigen-phred_coding", "Eigen-PC-raw_coding", "Eigen-PC-phred_coding", 
        "GenoCanyon_score", "integrated_fitCons_score", "GM12878_fitCons_score", "H1-hESC_fitCons_score", 
        "HUVEC_fitCons_score", "LINSIGHT", "GERP++_NR", "GERP++_RS", "phyloP100way_vertebrate", 
        "phyloP30way_mammalian", "phyloP17way_primate", "phastCons100way_vertebrate", 
        "phastCons30way_mammalian", "phastCons17way_primate", "bStatistic", "Interpro_domain", 
        "GTEx_V8_gene", "GTEx_V8_tissue", "CLNALLELEID", "CLNDN", "CLNDISDB", "CLNREVSTAT", 
        "CLNSIG", "1000g2015aug_all", "1000g2015aug_afr", "1000g2015aug_eas", "1000g2015aug_eur","1000g2015aug_sas", "1000g2015aug_amr",
        "AF", "AF_raw", "AF_male", "AF_female", "AF_afr", "AF_ami", "AF_amr", "AF_asj", "AF_eas", 
        "AF_fin", "AF_nfe", "AF_oth", "AF_sas", "ExAC_ALL", "ExAC_AFR", "ExAC_AMR", "ExAC_EAS", 
        "ExAC_FIN", "ExAC_NFE", "ExAC_OTH", "ExAC_SAS"]

        for k in headline:
            tmpk = INFOdict.get(k,null_str)
            if tmpk == ".":
                tmpk = null_str
            out[k] =tmpk
            
        logging.debug(out)
        return(out)


    def __parse_cosmic_coding(self,INFOdict):
        """
        parse cosmic coding into dict
        """
        out = {}
        headline =   ["COS_CODING_ID","COS_CODING_Gene_name","COS_CODING_Primary_site","COS_CODING_Primary_histology",
        "COS_CODING_Resistance_Mutation","COS_CODING_Pubmed_PMID","COS_CODING_Age","COS_CODING_Tier","COS_CODING_HGVSC",
        "COS_CODING_HGVSG","COS_CODING_HGNC_ID","COS_CODING_Sample_name","COS_CODING_ID_sample"]

        for k in headline:
            tmpk = INFOdict.get(k,null_str)
            if tmpk == ".":
                tmpk = null_str
            out[k] =tmpk
            
        logging.debug(out)
        return(out)

    def __parse_cosmic_noncoding(self,INFOdict):
        """
        parse cosmic non coding into dict
        """
        out = {}
        headline =   ["COS_NCODING_ID","COS_NCODING_Gene_name","COS_NCODING_Primary_site","COS_NCODING_Primary_histology",
        "COS_NCODING_Resistance_Mutation","COS_NCODING_Pubmed_PMID","COS_NCODING_Age","COS_NCODING_HGVSC","COS_NCODING_HGVSG",
        "COS_NCODING_HGNC_ID","COS_NCODING_Sample_name","COS_NCODING_ID_sample"]

        for k in headline:
            tmpk = INFOdict.get(k,null_str)
            if tmpk == ".":
                tmpk = null_str
            out[k] =tmpk
            
        logging.debug(out)
        return(out)

    def __parse_cancerhotspots(self,INFOdict):
        """
        parse cancerhotspot into dict
        """
        out = {}
        headline = ["CancerHotposts_count","CancerHotposts_TumorsCount","CancerHotposts_Amino_Acid_Change","CancerHotposts_HGNC_ID",
                    "CancerHotposts_Feature","CancerHotposts_Gene","CancerHotposts_HGVSc","CancerHotposts_HGVSp","CancerHotposts_Hugo_Symbol",
                    "CancerHotposts_Entrez_Gene_Id","CancerHotposts_dbSNP_RS","CancerHotposts_Exon_Number","CancerHotposts_SWISSPROT",
                    "CancerHotposts_UNIPARC"]

        for k in headline:
            tmpk = INFOdict.get(k,null_str)
            if tmpk == ".":
                tmpk = null_str
            out[k] =tmpk
            
        logging.debug(out)
        return(out)

    def __parse_civic(self,INFOdict):
        """
        parse civic into dict
        """

        def parse_one_record_in_civic(record):
            out = {}
            headline = ["Allele","Consequence","SYMBOL","Entrez_Gene_ID","Feature_type","Feature","HGVSc","HGVSp",
            "CIViC_Variant_Name","CIViC_Variant_ID","CIViC_Variant_Aliases","CIViC_HGVS","Allele_Registry_ID",
            "ClinVar_IDs","CIViC_Variant_Evidence_Score","CIViC_Entity_Type","CIViC_Entity_ID","CIViC_Entity_URL",
            "CIViC_Entity_Source","CIViC_Entity_Variant_Origin","CIViC_Entity_Status","CIViC_Entity_Clinical_Significance",
            "CIViC_Entity_Direction","CIViC_Entity_Disease","CIViC_Entity_Drugs","CIViC_Entity_Drug_Interaction_Type",
            "CIViC_Evidence_Phenotypes","CIViC_Evidence_Level","CIViC_Evidence_Rating","CIViC_Assertion_ACMG_Codes",
            "CIViC_Assertion_AMP_Category","CIViC_Assertion_NCCN_Guideline","CIVIC_Assertion_Regulatory_Approval",
            "CIVIC_Assertion_FDA_Companion_Test"]
            recordlist = record.split("|")
            for k,r in enumerate(recordlist):
                if r.strip() != "":
                    out[headline[k]] = r
                else:
                    out[headline[k]] = null_str
            logging.debug(out)
            return(out)

        
        if "CIVIC_CSQ" in  INFOdict.keys():
            dat = INFOdict['CIVIC_CSQ']
            datlist =[i.strip(" ") for i in  dat.strip("\n").split(",")]
            myout = []
            logging.debug(datlist)
            for record in datlist:
                myout.append(parse_one_record_in_civic(record))
            return(myout)
        else:
            return([])
    

    def __parse_cgi(self,INFOdict):
        """
        parse cgi database
        """
        out = {}
        headline = ['CGI_Association',
                        'CGI_Biomarker',
                        'CGI_Drug',
                        'CGI_Drug_family',
                        'CGI_Drug_full_name',
                        'CGI_Drug_status',
                        'CGI_Evidence_level',
                        'CGI_Gene',
                        'CGI_Primary_Tumor_type',
                        'CGI_Source',
                        'CGI_cDNA',
                        'CGI_gDNA',
                        'CGI_individual_mutation',
                        'CGI_transcript']

        for k in headline:
            tmpk = INFOdict.get(k,null_str)
            if tmpk == ".":
                tmpk = null_str
            out[k] =tmpk
            
        logging.debug(out)
        return(out)        

def build_gene_block(variant_block):
    
    """
            gene:{
                geneID:{ 
                    ENSG:,
                    SYMBOL:,
                    HGNCID:,
                    ENSP:,
                    variantID:[
                    ]
            }
        }
    the classification of variants in vep are:
    """
    noncodingblock = OrderedDict()
    geneblock = OrderedDict()
    for id,var in variant_block.items():
        varlist = var.get("vep",null_str)
        for onevep in varlist:
            tmp_ENSG = onevep.get("Gene",null_str)
            if tmp_ENSG == null_str :
                noncodingblock[id] = var
                #continue # here we filter out the intergenic variants and lncRNA variants annotation, those intergenic variants will be placed to another object
            else:
                GENEID = "GENEID:"+str(tmp_ENSG)
                if GENEID not in geneblock.keys():
                    geneblock[GENEID] = {
                        "ENSG":tmp_ENSG,
                        "patient_snvindel_list":[var]
                    }
                else:
                    geneblock[GENEID]["patient_snvindel_list"].append(var)
    return((geneblock,noncodingblock))

def convertvcf2json(invcf) :
    variantblock = OrderedDict()
    count = 0
    with open(invcf) as fvcf:
        for onevar in fvcf:
            # skip annotation lines
            if onevar.strip().startswith("#"):
                continue
            count += 1
            # split variant into list
            varlist = [i.strip() for i in onevar.rstrip("\n").split("\t")]
            varobj = myVariantObj(varlist=varlist)
            eachdata = varobj.get_jsonObj()
            variantblock["VariantID:"+str(count)] = eachdata # build variant block
    geneblock,noncodingblock = build_gene_block(variantblock)
    return  (geneblock,noncodingblock)


def processsnvindel(snvindel,snvindeltype,refver,outdir,jobid):
    try:
        annoVariantScript = myconfig.config.get("snv",{}).get("variant_level_annotation_sciript",None)
        if snvindeltype.strip().lower() == "maf":
            vcfpath = os.path.join(outdir,jobid+".input.snv.convert.vcf")
            convert(snvindel,snvindeltype,vcfpath,refver=refver)
        elif snvindeltype.strip().lower() == "5coltsv":
            vcfpath = os.path.join(outdir,jobid+".input.snv.convert.vcf")
            convert(snvindel,snvindeltype,vcfpath,refver=refver) 
        elif snvindeltype.strip().lower() == "vcf":
            vcfpath = snvindel

        


        if annoVariantScript is not None:
            if os.path.exists(annoVariantScript):
                # anync calculate  outdir,jobid,refver,VCF
                pmutsig = multiprocessing.Process(target=processSNV_Mutsig.runSignatureCal,args=(outdir,jobid,refver,vcfpath,))
                pmutsig.start() # join this process before return
                print("Start to annotate vcf...")
                cmd = f" bash {annoVariantScript} {vcfpath} {outdir} {refver} {jobid} &> {outdir}/{jobid}.SNV.run.log  "
                print(cmd)
                p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE) # stdout=subprocess.PIPE, stderr=subprocess.PIPE 不需要返回
                p.wait()

                ## 这里处理输出，如果发现有问题，那么就直接Raise Exception

                #stdout,stderr = p.communicate()
                #print(stdout.decode())
                annotatedVCF = os.path.join(outdir,jobid+"."+refver+"_multianno.vcfanno.vcf")
                pmutsig.join()
                if os.path.exists(annotatedVCF):
                    geneblock,noncodingblock = convertvcf2json(annotatedVCF)
                    return({
                        "status":True,
                        "geneblock":geneblock,
                        "noncodingblock":noncodingblock
                    })
                else:
                    return({
                        "status":False,
                        "geneblock":None,
                        "noncodingblock":None
                    })
            else:
                pass # 处理viariantScriptb
                return ({
                        "status":False,
                        "geneblock":None,
                        "noncodingblock":None
                    })
        return ({
                        "status":False,
                        "geneblock":None,
                        "noncodingblock":None
                    }) 
    except:
        myutils.addGlobalError("Process SNV/Indel data failed. Please double check your SNV/Indel file and SNV/Indel type.")
        
        raise Exception
        return ({
                        "status":False,
                        "geneblock":None,
                        "noncodingblock":None
                    }) # 这里不返回{} 因为必须要有SNV才可以

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format="[%(levelname)s - %(asctime)s] %(message)s")

    processsnvindel(
        snvindel="/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/demo/test.vcf",
        snvindeltype="vcf",
        refver="hg19",
        outdir="/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/demo",
        jobid="test_snv",

    )
