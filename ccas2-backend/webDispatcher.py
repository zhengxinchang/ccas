import logging
from typing import Optional
from xmlrpc.client import boolean
from fastapi import FastAPI, File, UploadFile,BackgroundTasks
import webGlobal
from webGlobal import BASE_URL
import webDBmanager
import os
import webUtils
import json
import re
import datetime
import subprocess
import automail
from starlette.responses import FileResponse


webGlobal.appname
app = FastAPI(
openapi_url=f"/{webGlobal.appname}/api/data_manger.json",
docs_url=f"/{webGlobal.appname}/api/docs",
redoc_url=f"/{webGlobal.appname}/api/redoc"
)


# notused
@app.post(BASE_URL+"/api/hello")
def hello():

    return("hello")    

# notused
@app.post(BASE_URL  + "/api/get_cancer_type" )
def getCancertype():
    ThisMysqlUtils = webDBmanager.webMysqlUtil()
    res = ThisMysqlUtils.getCancertype()
    ThisMysqlUtils.close()
    return res

# 分页返回基因表格，不包含data数据
@app.post(BASE_URL +"/api/get_gene_anno_table_by_page")
def getGeneAnnoTableByPage(jobid:str,pageNumber:int,pageSize:int):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"sqlite3 database not found","data":None}
    else:

        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)

        sql = """select 
        geneid, symbol, entrezid, ucscid, 
        uniprotids, name, locus_type, location, 
        genefamily, numofsnvindel, numofcnv, numofexp, 
        numofmeth, numofpaper, numofdruginteraction, 
        numofdpathway, numofcancer  
        from gene limit ?,? ;"""
        dat = sqliteUtil.execute_fetchAll(sql,(webUtils.calPageStart(pagenumber=pageNumber,pagesize=pageSize),pageSize,))

        try:
            if len(dat[1]) == 0:
                return {"status":"dataNotFound","msg":"can not query gene","data":None}
            else:
                return {"status":"ok","msg":"retrevial data successfully","data":dat[1]}
        except:
            return {"status":"failed","msg":"sqlite database crash","data":None}


@app.post(BASE_URL +"/api/get_gene_anno_table_by_page_filters")
def getGeneAnnoTableByPageFilters(
    jobid:str,pageNumber:int,pageSize:int,
    ENSGID:Optional[str]=None,SYMBOL:Optional[str]=None,
    LOUCSTYPE:Optional[str]=None,ORDERBY:Optional[str]=None,
    ORDERDESC:Optional[bool]=False,NAME:Optional[str]=None,
    IS_FILTER_SNV:Optional[bool]=False,IS_FILTER_CNV:Optional[bool]=False,IS_FILTER_METH:Optional[bool]=False,IS_FILTER_EXP:Optional[bool]=False,
    FILTER_SNV_CUTOFF:Optional[str]=None,FILTER_CNV_CUTOFF:Optional[str]=None,FILTER_EXP_CUTOFF:Optional[str]=None,FILTER_METH_CUTOFF:Optional[str]=None
    ):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"sqlite3 database not found","data":None}
    else:

        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)

        filterSQLList = []
        if ENSGID is not None:
            filterSQLList.append(f"geneid like '%{ENSGID}%'")
        if SYMBOL is not None:
            filterSQLList.append(f"symbol like '%{SYMBOL}%'")
        if NAME is not None:
            filterSQLList.append(f"name like '%{NAME}%'")
        if LOUCSTYPE is not None:
            filterSQLList.append(f"locus_type = '{LOUCSTYPE}'")

        if IS_FILTER_SNV == True:
            filterSQLList.append(f"numofsnvindel > 0")
            
            if FILTER_SNV_CUTOFF is not None:
                SNVFiltersCriteria = json.loads(FILTER_SNV_CUTOFF)

                # if SNVFiltersCriteria['IMPACT'].get("HIGH") ==False:
                #     filterSQLList.append(f"HIGH = 0")
                # if SNVFiltersCriteria['IMPACT'].get("LOW") ==False:
                #     filterSQLList.append(f"LOW = 0")
                # if SNVFiltersCriteria['IMPACT'].get("MODERATE") ==False:
                #     filterSQLList.append(f"MODERATE = 0")
                # if SNVFiltersCriteria['IMPACT'].get("MODIFIER") ==False:
                #     filterSQLList.append(f"MODIFIER = 0")
                
                consquenceSQLList = []
                
                for impact,impactval in SNVFiltersCriteria['IMPACT'].items():
                    for consequence,consequenceval in impactval['consequence'].items():
                        if consequenceval['value'] ==True:
                            consquenceSQLList.append(f"{consequence} > 0")

                if len(consquenceSQLList) > 0: 
                    consquenceSQLListStr  = " ( " + " OR ".join(consquenceSQLList) +" ) "
                    filterSQLList.append(consquenceSQLListStr)


        if IS_FILTER_EXP == True:
            filterSQLList.append(f"numofexp > 0")

            ExpFiltersCriteria = json.loads(FILTER_EXP_CUTOFF)

            if not (ExpFiltersCriteria[0] == 0 and ExpFiltersCriteria[1] == 0):
                filterSQLList.append(f" ( exp_value >= {ExpFiltersCriteria[0]} and exp_value <= {ExpFiltersCriteria[1]} ) ")

        if IS_FILTER_CNV == True:
            filterSQLList.append(f"numofcnv > 0")
            CNVFiltersCriteria = json.loads(FILTER_CNV_CUTOFF)

            if not (CNVFiltersCriteria[0] == 0 and CNVFiltersCriteria[1] == 0):
                filterSQLList.append(f" ( cnv_value >= {CNVFiltersCriteria[0]} and cnv_value <= {CNVFiltersCriteria[1]} ) ")            

        if IS_FILTER_METH == True:
            filterSQLList.append(f"numofmeth > 0")
            MethFiltersCriteria = json.loads(FILTER_METH_CUTOFF)

            if not (MethFiltersCriteria[0] == 0 and MethFiltersCriteria[1] == 0):
                filterSQLList.append(f" ( meth_value >= {MethFiltersCriteria[0]} and meth_value <= {MethFiltersCriteria[1]} ) ")            


        if len(filterSQLList) > 0 :
            subSQL = " and " + " and ".join(filterSQLList)
        else:
            subSQL = ""
        OrderByDict = {
            "symbol":"symbol",
            "geneid":"geneid",
            "name":"name",
            "locus_type":"locus_type",
            "genefamily":"genefamily",
            "numofsnvindel":"numofsnvindel",
            "numofcnv":"numofcnv",
            "numofexp":"numofexp",
            "numofmeth":"numofmeth",
            "numofpaper":"numofpaper",
            "numofdruginteraction":"numofdruginteraction",
            "numofdpathway":"numofdpathway",
            "numofpaper":"numofpaper",
            "numofcancer":"numofcancer",
            "location":"location",
        }

        if ORDERBY in OrderByDict.keys():
            if ORDERDESC:
                subSQL +=  f" ORDER BY {OrderByDict[ORDERBY]} DESC"
            else:
                subSQL +=  f" ORDER BY {OrderByDict[ORDERBY]} "
        

        subSQL.replace(";","")
        sql = f"""
        select 
            geneid,
            symbol,
            entrezid,
            ucscid,
            uniprotids,
            name,
            locus_type,
            location,
            genefamily,
            numofsnvindel,
            numofcnv,
            numofexp,
            numofmeth,
            numofpaper,
            numofdruginteraction,
            numofdpathway,
            numofcancer,
            cnv_value,
            exp_value,
            meth_value,
            HIGH ,
            LOW ,
            MODERATE ,
            MODIFIER ,
            consequence_transcript_ablation ,
            consequence_splice_acceptor_variant ,
            consequence_splice_donor_variant ,
            consequence_stop_gained ,
            consequence_frameshift_variant ,
            consequence_stop_lost ,
            consequence_start_lost ,
            consequence_transcript_amplification ,
            consequence_inframe_insertion ,
            consequence_inframe_deletion ,
            consequence_missense_variant ,
            consequence_protein_altering_variant ,
            consequence_splice_region_variant ,
            consequence_incomplete_terminal_codon_variant ,
            consequence_start_retained_variant ,
            consequence_stop_retained_variant ,
            consequence_synonymous_variant ,
            consequence_coding_sequence_variant ,
            consequence_mature_miRNA_variant ,
            consequence_5_prime_UTR_variant ,
            consequence_3_prime_UTR_variant ,
            consequence_non_coding_transcript_exon_variant ,
            consequence_intron_variant ,
            consequence_NMD_transcript_variant ,
            consequence_non_coding_transcript_variant ,
            consequence_upstream_gene_variant ,
            consequence_downstream_gene_variant ,
            consequence_TFBS_ablation ,
            consequence_TFBS_amplification ,
            consequence_TF_binding_site_variant ,
            consequence_regulatory_region_ablation ,
            consequence_regulatory_region_amplification ,
            consequence_feature_elongation ,
            consequence_regulatory_region_variant ,
            consequence_feature_truncation ,
            consequence_intergenic_variant 
        from gene where 1=1 {subSQL} limit ?,? ;"""
        
        dat = sqliteUtil.execute_fetchAll(sql,(webUtils.calPageStart(pagenumber=pageNumber,pagesize=pageSize),pageSize,))
        print(sql)

        sqlLength = f"""select 
        count(*) as count  
        from gene where 1=1 {subSQL}"""
        tatalDatLength = sqliteUtil.execute_fetchOne(sqlLength)

        sqlUniqLocusType = f"""select 
        DISTINCT locus_type as unique_locus_type  
        from gene where 1=1 """
        UniqLocusTypeData = sqliteUtil.execute_fetchAll(sqlUniqLocusType)
        print(UniqLocusTypeData)
        UniqLocusTypeData2=  [x['unique_locus_type']  for x in UniqLocusTypeData[1]] 


        sqlMaxMin = f"""
        select 
            max(cnv_value) as max_cnv_value ,
            min(cnv_value) as min_cnv_value ,
            max(exp_value) as max_exp_value ,
            min(exp_value) as min_exp_value ,
            max(meth_value) as max_meth_value ,
            min(meth_value) as min_meth_value  
        from gene  where 1=1 ;"""
        MaxMin = sqliteUtil.execute_fetchOne(sqlMaxMin)
        
        # print(MaxMin)

        try:
            if len(dat[1]) == 0:
                return {"status":"dataNotFound","msg":"can not query gene","data":[],"count":0,"unique_locus_type":[],"MaxMin":{}}
            else:
                return {"status":"ok","msg":"retrevial data successfully","data":dat[1],"count":tatalDatLength[1],"unique_locus_type":UniqLocusTypeData2,"MaxMin":MaxMin[1]}
        except:
            return {"status":"failed","msg":"sqlite database crash","data":[],"count":0,"unique_locus_type":[],"MaxMin":{}}


@app.post(BASE_URL +"/api/get_gene_anno_table_length_by_jobid")
def getGeneAnnoTableLengthByJobID(jobid:str):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"sqlite3 database not found","data":None}
    else:

        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)

        sql = """select 
        count(*)  as count
        from gene ;"""
        dat = sqliteUtil.execute_fetchOne(sql)

        try:
            if len(dat[1]) == 0:
                return {"status":"dataNotFound","msg":"can not query gene","data":None}
            else:
                return {"status":"ok","msg":"retrevial data successfully","data":dat[1]}
        except:
            return {"status":"failed","msg":"sqlite database crash","data":None}


# 返回一个基因的所有注释数据
@app.post(BASE_URL +"/api/get_one_gene_anno_by_geneid")
def getOneGeneAnnoByGeneid(jobid:str,geneid:str):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"sqlite3 database not found","data":None}
    else:

        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)

        sql = """select 
        * 
        from gene where geneid = ? ;"""
        dat = sqliteUtil.execute_fetchOne(sql,(geneid,))

        try:
            if len(dat[1].keys()) == 0:
                return {"status":"dataNotFound","msg":"can not query gene","data":None}
            else:

                d = dat[1]
                d['data'] = json.loads(d['data'])

                return {"status":"ok","msg":"retrevial data successfully","data":d}
        except Exception as e:
            logging.info(f"sqlite3 query failed, reason: {str(e)}")
            return {"status":"failed","msg":"sqlite database crash","data":None}

# overview disease ontology
@app.post(BASE_URL +"/api/get_overview_disease_ontology")
def getOverviewDiseaseOntology(jobid:str):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")


    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"job path or job sqlite3 file not found in disk","data":None}
    else:
        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)
        
        
        #===================
        try:
            ThisMysqlUtils = webDBmanager.webMysqlUtil()
            jobdat = ThisMysqlUtils.get_one_jobinfo_by_job_id(jobid)
            # 这里不判断 jobdat 结果是否为空，因为前边判断如果sqlite3文件不存在，有jobid 记录在mysql的job表中没有意义


            sql = """
            select 
            * 
            from overview_disease_ontology limit 1 ;"""
            dat = sqliteUtil.execute_fetchOne(sql)
            if len(dat[1].keys()) == 0:
                return {"status":"dataNotFound","msg":"can not query gene","data":None}
            else:
                d = dat[1]
                d['data'] =  json.loads(d['data'])
                d['jobinfo'] = {k:v  for k,v in jobdat.items() if k != "workdir"}

                return {"status":"ok","msg":"retrevial data successfully","data":d}
        #====================
        except Exception as e:
            logging.info(f"sqlite3 query failed, reason: {str(e)}")
            return {"status":"failed","msg":"sqlite database crash","data":None}

# overview clinical
@app.post(BASE_URL +"/api/get_overview_clinical_table_by_page")
def getOverviewClinicalTableByPage(jobid:str,
    pageNumber:int,
    pageSize:int,
    ORDERBY:Optional[str]=None,
    ORDERDESC:Optional[bool]=False,
    BriefTitle:Optional[str]=None,
    Intervention:Optional[str]=None,
    NCTID:Optional[str]=None,
    Phase:Optional[str]=None
    ):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"sqlite3 database not found","data":None}
    else:

        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)

        filterSQLList = []
        if BriefTitle is not None:
            filterSQLList.append(f"BriefTitle like '%{BriefTitle.strip()}%'")
        if Intervention is not None:
            filterSQLList.append(f"Intervention like '%{Intervention}%'")
        if NCTID is not None:
            filterSQLList.append(f"NCTID like '%{NCTID}%'")
        if Phase is not None:
            filterSQLList.append(f"Phase like '%{Phase}%'")
        if len(filterSQLList) > 0 :
            subSQL = " and " + " and ".join(filterSQLList)
        else:
            subSQL = ""
        OrderByDict = {
            "NCTID":"NCTID",
            "Phase":"Phase",
        }

        if ORDERBY in OrderByDict.keys():
            if ORDERDESC:
                subSQL +=  f" ORDER BY {OrderByDict[ORDERBY]} DESC"
            else:
                subSQL +=  f" ORDER BY {OrderByDict[ORDERBY]} "


        sql = f"""
        select 
        NCTID,URL,BriefTitle,BriefSummary,DetailDescription,
        EligbilityCriteria,Reference,Phase,Intervention,MESH
        from overview_clinical where 1=1 {subSQL} limit ?,? ;"""
        print(sql)
        dat = sqliteUtil.execute_fetchAll(sql,(webUtils.calPageStart(pagenumber=pageNumber,pagesize=pageSize),pageSize,))

        sqlLength = f"""select 
        count(*) as count  
        from overview_clinical  where 1=1 {subSQL} """
        tatalDatLength = sqliteUtil.execute_fetchOne(sqlLength)

        try:
            if len(dat[1]) == 0:
                return {"status":"dataNotFound","msg":"can not query","data":None,"count":0}
            else:
                return {"status":"ok","msg":"retrevial data successfully","data":dat[1],"count":tatalDatLength[1]}
        except:
            return {"status":"failed","msg":"sqlite database crash","data":None,"count":0}

# overview pathways
@app.post(BASE_URL +"/api/get_overview_pathway_table_by_page")
def getOverviewPathwayTableByPage(
    jobid:str,
    pageNumber:int,
    pageSize:int,
    DisplayName:Optional[str]=None,
    ID:Optional[str]=None,
    ORDERBY:Optional[str]=None,
    ORDERDESC:Optional[bool]=False,
    HAS_SNVINDEL:Optional[bool]=False,
    HAS_EXP:Optional[bool]=False,
    HAS_CNV:Optional[bool]=False,
    HAS_METH:Optional[bool]=False

    ):
    sqlite3dbPath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(sqlite3dbPath):
        return {"status":"failed","msg":"sqlite3 database not found","data":None}
    else:

        sqliteUtil = webDBmanager.sqlite3Utils(sqlite3dbPath)

        filterSQLList = []
        if DisplayName is not None:
            filterSQLList.append(f"DisplayName like '%{DisplayName.strip()}%'")
        if ID is not None:
            filterSQLList.append(f"ID like '%{ID}%'")
        if HAS_SNVINDEL == True:
            filterSQLList.append(f" summary_snvindel > 0")
        if HAS_EXP == True:
            filterSQLList.append(f" summary_exp > 0")
        if HAS_CNV == True:
            filterSQLList.append(f" summary_cnv > 0")
        if HAS_METH == True:
            filterSQLList.append(f" summary_meth > 0")

        if len(filterSQLList) > 0 :
            subSQL = " and " + " and ".join(filterSQLList)
        else:
            subSQL = ""
        OrderByDict = {
            "DisplayName":"DisplayName",
            "ID":"ID",
        }

        if ORDERBY in OrderByDict.keys():
            if ORDERDESC:
                subSQL +=  f" ORDER BY {OrderByDict[ORDERBY]} DESC"
            else:
                subSQL +=  f" ORDER BY {OrderByDict[ORDERBY]} "

        sql = f"""
        select 
        ID,DisplayName,AlternavieNames,HitsGene,summary_snvindel,
        summary_cnv,summary_exp,summary_meth,
        literatureReference,summation,subEvent
        from overview_pathway where 1=1 {subSQL} limit ?,? ;"""
        dat = sqliteUtil.execute_fetchAll(sql,(webUtils.calPageStart(pagenumber=pageNumber,pagesize=pageSize),pageSize,))

        sqlLength = f"""select 
        count(*) as count  
        from overview_pathway  where 1=1 {subSQL} """
        tatalDatLength = sqliteUtil.execute_fetchOne(sqlLength)

        try:
            if len(dat[1]) == 0:
                return {"status":"dataNotFound","msg":"can not query gene","data":None,"count":0}
            else:

                newdat = []
                # print(dat[1])
                for x in dat[1]:
                    newdat.append(
                        {
                           "ID":x['ID'], 
                           "DisplayName":x['DisplayName'], 
                           "AlternavieNames":x['AlternavieNames'], 
                           "HitsGene":json.loads(x['HitsGene']), 
                           "summation":json.loads(x['summation']), 
                           "literatureReference":json.loads(x['literatureReference']), 
                           "summary_snvindel":x['summary_snvindel'], 
                           "summary_cnv":x['summary_cnv'], 
                           "summary_exp":x['summary_exp'], 
                           "summary_meth":x['summary_meth']
                        }
                    )

                return {"status":"ok","msg":"retrevial data successfully","data":newdat,"count":tatalDatLength[1]}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"sqlite database crash","data":None}

@app.post(BASE_URL + "/api/get_overview_tumor_signature")
def getOverviewTumorSignature(jobid:str):
    
    jpath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".TumorSignature.json")
    if not os.path.exists(jpath):
        return {"status":"failed","msg":"json not found","data":None,"count":0}
    else:

        try:
            dat = json.load(open(jpath))
            return {"status":"ok","msg":"retrevial json successfully","data":dat}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}


@app.post(BASE_URL + "/api/get_overview_signature_similarity")
def getOverviewSignatureSimilarity(jobid:str):
    
    jpath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".CosmicSigSimilarity.json")
    if not os.path.exists(jpath):
        return {"status":"failed","msg":"json not found","data":None}
    else:

        try:
            dat = json.load(open(jpath))
            return {"status":"ok","msg":"retrevial json successfully","data":dat}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}


@app.post(BASE_URL + "/api/get_overview_ssgsea_raw")
def getOverviewSSGSEARaw(jobid:str):
    
    jpath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".ssGSEA.raw.json")
    if not os.path.exists(jpath):
        return {"status":"failed","msg":"json not found","data":None}
    else:
        try:
            dat = json.load(open(jpath))
            return {"status":"ok","msg":"retrevial json successfully","data":dat}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}

@app.post(BASE_URL + "/api/get_overview_ssgsea_normalize")
def getOverviewSSGSEANormalize(jobid:str):
    
    jpath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".ssGSEA.normalize.json")
    if not os.path.exists(jpath):
        return {"status":"failed","msg":"json not found","data":None}
    else:
        try:
            dat = json.load(open(jpath))
            return {"status":"ok","msg":"retrevial json successfully","data":dat}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}

@app.post(BASE_URL + "/api/get_overview_signature_desc")
def getOverviewSignatureDesc():
        try:
            dat = webGlobal.signatureDesc
            return {"status":"ok","msg":"retrevial json successfully","data":dat}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}



@app.post(BASE_URL + "/api/get_home_disease_tree")
def getHomeDiseaseTree():
        try:
            dat = webGlobal.disease_tree
            return {"status":"ok","msg":"retrevial json successfully","data":dat}
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}


@app.get(BASE_URL + "/api/download_sqlite3")
def download_sqlite3(jobid:str):
    
    jpath = os.path.join(webGlobal.workspaceRoot,jobid,jobid+".data.sqlite3")
    if not os.path.exists(jpath):
        return {"status":"failed","msg":"sqlite3 not found","data":None}
    else:
        try:
            
            return FileResponse(
                jpath,
                filename=jobid+".data.sqlite3"
            )
        except Exception as e:
            print(str(e))
            return {"status":"failed","msg":"load json crash","data":None}


@app.post(BASE_URL + "/api/home_submit")
async def HomeSubmit(

    snvindeltype:str,
    doid:str,
    refver:str,
    background_tasks: BackgroundTasks,
    email:Optional[str]=None,
    jobtitle:Optional[str]=None,
    exptype:Optional[str]=None,
    cnvtype:Optional[str]=None,
    methtype:Optional[str]=None,
    snvindelFile:UploadFile =File(...),
    expFile:Optional[UploadFile] =File(None),
    cnvFile:Optional[UploadFile] =File(None),
    methFile:Optional[UploadFile] =File(None)
    ):
    print(expFile)

    # format validation
    msg = {
        "status":"succeed",
        "errmsg":[],
        "jobid":None,
    }

    if not doid.strip().upper().startswith("DOID:"):
        msg['status'] = "error"
        msg['errmsg'].append(f"DOID '{doid}' format is not correct!")
    else:
        if doid.strip().upper() not in webGlobal.disease_tree['dict'].keys():
            msg['status'] = "error"
            msg['errmsg'].append(f"DOID '{doid}' not supported!")

    if refver.strip().lower() not in ['hg19',"hg38"]:
        msg['status'] = "error"
        msg['errmsg'].append(f"reference version must be 'hg19' or 'hg38', '{doid}' found!")

    if email is not None  and not re.match(r"^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$",email.strip()):
        msg['status'] = "error"
        msg['errmsg'].append(f"Email '{email}'is not in correct format!")     

    if snvindeltype.strip().lower() not in ['vcf',"maf","5coltsv"]:
        msg['status'] = "error"
        msg['errmsg'].append(f"cnvtype must be 'gene' or 'region', '{doid}' found!")
    if cnvtype is not None and cnvtype.strip().lower() not in ['gene',"region"]:
        msg['status'] = "error"
        msg['errmsg'].append(f"cnvtype must be 'gene' or 'region', '{doid}' found!")

    if methtype is not None and methtype.strip().lower() not in ['gene',"region"]:
        msg['status'] = "error"
        msg['errmsg'].append(f"methtype must be 'gene' or 'region', '{doid}' found!")

    if exptype is not None and exptype.strip().lower() not in ['gene']:
        msg['status'] = "error"
        msg['errmsg'].append(f"cnvtype must be 'gene' or 'region', '{doid}' found!")

    if not ((expFile is not None and exptype is not None) or (expFile is None and exptype is None)):
        print(f"expFile:{expFile},exptype:{exptype}")
        print((expFile is not None and exptype is not None))
        msg['status'] = "error"
        msg['errmsg'].append(f"exp file and exptype must co-occur or not")
    
    if not ((cnvFile is not None and cnvtype is not None) or (cnvFile is None and cnvtype is None)):
        msg['status'] = "error"
        msg['errmsg'].append(f"cnv file and cnvtype must co-occur or not")

    if not ((methFile is not None and methtype is not None) or (methFile is None and methtype is None)):
        msg['status'] = "error"
        msg['errmsg'].append(f"meth file and methtype must co-occur or not")

    if msg['status'] == "error":
        return msg

    # generate jobid
    jobid = webUtils.getJobID()
    jobpath = webUtils.create_job_dir(jobid=jobid,rootPath=webGlobal.workspaceRoot)
    # insert to mysql db
    ThisMysqlUtils = webDBmanager.webMysqlUtil()

    ThisMysqlUtils.insertOneJob(
        jobid=jobid,
        status="1:running",
        refver=refver,
        workdir=jobpath,
        start_time=datetime.datetime.now(),
        snvindeltype=snvindeltype,
        has_exp=0 if expFile is None else 1,
        has_cnv=0 if cnvFile is None else 1,
        has_meth=0 if methFile is None else 1,
        email=email,
        end_time=None,
        exptype=exptype,
        cnvtype=cnvtype,
        methtype=methtype,
        title=jobtitle,
        has_send_jobid=0,
        has_send_finished=0
    )
    # copy file to workdir
    snvindelPathInWorkdir = os.path.join(jobpath,jobid+".input.snv."+snvindeltype)
    SaveFileHandler = open(snvindelPathInWorkdir,"wb")
    SaveFileHandler.write(snvindelFile.file.read())
    SaveFileHandler.close()

    expPathInWorkdir = None
    if expFile is not None and exptype is not None:
        expPathInWorkdir = os.path.join(jobpath,jobid+".input.exp.txt")
        SaveFileHandler = open(expPathInWorkdir,"wb")
        SaveFileHandler.write(expFile.file.read())
        SaveFileHandler.close()

    cnvPathInWorkdir = None
    if cnvFile is not None and cnvtype is not None:
        cnvPathInWorkdir = os.path.join(jobpath,jobid+".input.cnv.txt")
        SaveFileHandler = open(cnvPathInWorkdir,"wb")
        SaveFileHandler.write(cnvFile.file.read())
        SaveFileHandler.close()

    methPathInWorkdir = None
    if methFile is not None and methtype is not None:
        methPathInWorkdir = os.path.join(jobpath,jobid+".input.meth.txt")
        SaveFileHandler = open(methPathInWorkdir,"wb")
        SaveFileHandler.write(methFile.file.read())
        SaveFileHandler.close()

    pipecmd = f""" nohup python3 {webGlobal.CCASpipeline} --snvindel {snvindelPathInWorkdir}  --snvindeltype {snvindeltype} --exp {expPathInWorkdir} --meth {methPathInWorkdir} --methtype {methtype}  --cnv {cnvPathInWorkdir} --cnvtype {cnvtype}  --doid {doid} --jobid {jobid}  --refver {refver} --outdir {jobpath}   --jobtitle '{str(jobtitle)}' --email {str(email)}  &>{os.path.join(jobpath,jobid+".CCASPipe.log")}  & """
    print(pipecmd)
    p = subprocess.Popen(pipecmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    msg['jobid'] = jobid
    
    ThisMysqlUtils.commit()
    ThisMysqlUtils.close()

    if email is not None:
        background_tasks.add_task(automail.auto_mail,f"Dear CCAS user,\nYour submission has started, and will take a few minutes. Notification E-mail will be sent after job finished.\nThe job id is ' {jobid} '.\nThe job title is ' {jobtitle} '\n",
        "CCAS auto",
        email) #"hello","CCAS test","zhengxinchang@big.ac.cn"

    return msg


@app.post(BASE_URL + "/api/checkjob")
async def checkjog(
    jobid:str,
    ):

    webdbUtils = webDBmanager.webMysqlUtil()
    res = webdbUtils.checkJobStatus(jobid=jobid.strip())
    return res
