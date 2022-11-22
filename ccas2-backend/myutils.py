import os
import subprocess
import myconfig
import logging
import pymysql
import sqlite3
import json
import logging 

class Utils():
    
    @staticmethod
    def normalizeChr(a):
        if not a.strip().lower().startswith("chr"):
            x='chr'+a
            return x
        else:
            return a
    @staticmethod
    def stripENSGversion(a):
        if '.' not in a:
            return a
        else:
            return a.split(".")[0]
    @staticmethod
    def addGENEID(a):
        return("GENEID:"+a)


class ProcessCNVAndMethlation():

    @staticmethod
    def process(f,ft,refver,jobid,outdir,omic_type):
        '''
        out = {
            type:gene,
            data:{
                ENSG:{
                    "ENSG":
                    "value":
                    "regions":[
                        chr:,
                        start:,
                        end:
                    ]
                }
            }
        }
        '''
        bed_processed_out = {
        }    
        if ft.strip().lower() == "gene":
            """
            如果是基因类型的，则region是空的列表
            """
            # bed_processed_out['type'] = ft.strip().lower()
            with open(f) as inf:
                next(inf)
                for a in inf:
                    
                    lineList = a.strip().split("\t")

                    GENEID = "GENEID:"+Utils.stripENSGversion(lineList[0])
                    block ={ 
                            "ENSG":GENEID,
                            "value":lineList[1],
                            "regions":None
                           }
                    bed_processed_out[GENEID] = block     

        elif ft.strip().lower() == "region":
            # bed_processed_out['type'] = ft.strip().lower()
            
            with open(f) as inf:
                header = next(inf)
                # add chr to bed if it does not exits
                tmpcnv = [Utils.normalizeChr(a).strip() for a in inf]
                ftmpcnv_path = os.path.join(outdir,jobid+"."+omic_type+".normalize.bed")
                ftmpcnv = open(ftmpcnv_path,"w") 
                for tmp in tmpcnv:
                    ftmpcnv.write(tmp+"\n")
                ftmpcnv.close()

                # intersect user input bed to gene bed

                ref_gene_bed_path = myconfig.config.get('bed',{}).get('gene_bed',{}).get(refver,{})

                if ref_gene_bed_path is not None:
                    cmd = f"bedtools intersect  -a { ref_gene_bed_path }    -b  {ftmpcnv_path} -wao"
                    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out=res.stdout.readlines()
                    
                    # 如果执行成功，则生成json格式的文件
                    for x in out:
                    
                        xlist = x.decode().strip().split("\t")
                        # print(xlist)
                        if str(xlist[7].strip()) == "-1":
                            continue # skip not mapped genes
                        else:
                            GENEID = "GENEID:"+Utils.stripENSGversion(xlist[5])

                            if GENEID not in bed_processed_out.keys():
                                block ={ 
                                    "ENSG":GENEID,
                                    "value":xlist[9],
                                    "regions":":".join([xlist[6],xlist[7],xlist[8],xlist[9]])
                                }
                                bed_processed_out[GENEID] = block     
                            else:
                                pass # 处理如果一个基因重复出现再结果中的情况，现在的处理方法就是只取第一个的region
                
                # region格式转为gene value格式给ssGSEA用
                geneformatpath  = os.path.join(outdir,jobid+".input."+ft+".gene.txt")
                with open(geneformatpath,"w") as genevalueout :
                    for x  in bed_processed_out.values():
                        genevalueout.write(x['ENSG']+"\t"+x['value']+"\n")


        return (bed_processed_out)



class sqlite3Utils():

    def __init__(self,dbpath):
        # 创建log日志数据库
        """
        create table if not exists batchs ( BATCHID	 text not null PRIMARY KEY , INIT_TIME_STAMP text not null, CURR_TIME_STAMP	 text not null, BATCHID_DIR	 text not null, STATUS	 integer not null default 0, IDLIST	 text , ACCN	 text not null, FTP_DIR	 text not null, PROCESS_DIR	 text not null, START_GWHID	 text , END_GWHID text , START_WGSID text , END_WGSID text);
        """

        self.con = sqlite3.connect(dbpath)
        self.cur = self.con.cursor()
    def init_tables(self):
        sqlgene0 = "drop table if exists gene"
        sqlgene = """
                create table gene (
                geneid text not null PRIMARY KEY,
                symbol text ,
                entrezid text,
                ucscid text,
                uniprotids text,
                name text,
                locus_type text,
                location text,
                genefamily text,
                numofsnvindel integer not null,
                numofcnv integer not null,
                numofexp integer not null,
                numofmeth integer not null,
                numofpaper integer not null,
                numofdruginteraction integer not null,
                numofdpathway integer not null,
                numofcancer integer not null,
                cnv_value integer,
                exp_value integer,
                meth_value integer,
                HIGH integer not null,
                LOW integer not null,
                MODERATE integer not null,
                MODIFIER integer not null,
                consequence_transcript_ablation integer not null,
                consequence_splice_acceptor_variant integer not null,
                consequence_splice_donor_variant integer not null,
                consequence_stop_gained integer not null,
                consequence_frameshift_variant integer not null,
                consequence_stop_lost integer not null,
                consequence_start_lost integer not null,
                consequence_transcript_amplification integer not null,
                consequence_inframe_insertion integer not null,
                consequence_inframe_deletion integer not null,
                consequence_missense_variant integer not null,
                consequence_protein_altering_variant integer not null,
                consequence_splice_region_variant integer not null,
                consequence_incomplete_terminal_codon_variant integer not null,
                consequence_start_retained_variant integer not null,
                consequence_stop_retained_variant integer not null,
                consequence_synonymous_variant integer not null,
                consequence_coding_sequence_variant integer not null,
                consequence_mature_miRNA_variant integer not null,
                consequence_5_prime_UTR_variant integer not null,
                consequence_3_prime_UTR_variant integer not null,
                consequence_non_coding_transcript_exon_variant integer not null,
                consequence_intron_variant integer not null,
                consequence_NMD_transcript_variant integer not null,
                consequence_non_coding_transcript_variant integer not null,
                consequence_upstream_gene_variant integer not null,
                consequence_downstream_gene_variant integer not null,
                consequence_TFBS_ablation integer not null,
                consequence_TFBS_amplification integer not null,
                consequence_TF_binding_site_variant integer not null,
                consequence_regulatory_region_ablation integer not null,
                consequence_regulatory_region_amplification integer not null,
                consequence_feature_elongation integer not null,
                consequence_regulatory_region_variant integer not null,
                consequence_feature_truncation integer not null,
                consequence_intergenic_variant integer not null,
                data text not null

                );
        """

        sqlclinical0 = "drop table if exists overview_clinical"
        sqlclinical = """
            create table overview_clinical (
                NCTID text not null PRIMARY KEY,
                URL text ,
                BriefTitle text,
                BriefSummary text,
                DetailDescription text,
                EligbilityCriteria text,
                Reference text,
                Phase text,
                Intervention text,
                MESH text,
                data text not null
                );
        """
        sqlpathway0 = "drop table if exists overview_pathway"
        sqlpathway = """
            create table overview_pathway (
                ID text not null PRIMARY KEY,
                DisplayName text ,
                AlternavieNames text,
                Figure text,
                literatureReference text,
                summation text,
                subEvent text,
                HitsGene text not null,
                summary_snvindel int not null,
                summary_cnv int not null,
                summary_exp int not null,
                summary_meth int not null,
                data text not null
                );
        """

        sqlDiseaseOntology0 = "drop table if exists overview_disease_ontology"
        sqlDiseaseOntology = """
            create table overview_disease_ontology (
                doid text not null PRIMARY KEY,
                jobid text,
                data text 
                );
        """



        try:
            self.cur.execute(sqlgene0)
            self.cur.execute(sqlgene)
            self.con.commit()

            self.cur.execute(sqlclinical0)
            self.cur.execute(sqlclinical)
            self.con.commit()

            self.cur.execute(sqlpathway0)
            self.cur.execute(sqlpathway)
            self.con.commit()

            self.cur.execute(sqlDiseaseOntology0)
            self.cur.execute(sqlDiseaseOntology)
            self.con.commit()


            return([True,"OK"])
        except Exception as e:
            self.con.rollback()
            print(f"initialization database failed. beacuse {str(e)}")
            return([False,str(e)])  


    def execute_fetchOne(self,sql,params):
        try:
            self.cur.execute(sql,params)
            results = self.cur.fetchone()
            return([True,results])
        except Exception as e:
            self.con.rollback()
            return([False,str(e)])  

    def execute_fetchAll(self,sql,params):
        try:
            self.cur.execute(sql,params)
            results = self.cur.fetchall()
            return([True,results])
        except Exception as e:
            self.con.rollback()
            return([False,str(e)])            

    def getOneGeneDetail(self,GeneID):
        sql = "select * from gene WHERE geneid = ?;"
        return self.execute_fetchOne(sql,(GeneID,))

    def batchInsertGeneRecords(self,records_list):
        sql = """insert into gene (
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
            consequence_intergenic_variant ,
            data
            ) values (
                ?,?,?,?,?  ,?,?,?,?,? ,?,?,?,?,? ,?,?,?,?,?, 
                ?,?,?,?,?  ,?,?,?,?,? ,?,?,?,?,? ,?,?,?,?,?, 
                ?,?,?,?,?  ,?,?,?,?,? ,?,?,?,?,? ,?,?,?,?,?,
                ?
                )
            """
        self.cur.executemany(sql,records_list)
        self.con.commit()
    def batchInsertOverviewclincialRecords(self,records_list):
        sql = """insert into overview_clinical (
                NCTID ,
                URL  ,
                BriefTitle ,
                BriefSummary ,
                DetailDescription ,
                EligbilityCriteria ,
                Reference ,
                Phase ,
                Intervention ,
                MESH ,
                data ) values (
                ?,?,?,?,?  ,?,?,?,?,? ,?)
            """
        self.cur.executemany(sql,records_list)
        self.con.commit()

    def batchInsertOverviewclincialRecords(self,records_list):
        sql = """insert into overview_clinical (
                NCTID ,
                URL  ,
                BriefTitle ,
                BriefSummary ,
                DetailDescription ,
                EligbilityCriteria ,
                Reference ,
                Phase ,
                Intervention ,
                MESH ,
                data ) values (
                ?,?,?,?,?  ,?,?,?,?,? ,?)
            """
        self.cur.executemany(sql,records_list)
        self.con.commit()

    def batchInsertOverviewpathwayRecords(self,records_list):
        sql = """insert into overview_pathway (
                ID ,
                DisplayName  ,
                AlternavieNames ,
                Figure ,
                literatureReference ,
                summation ,
                subEvent ,
                HitsGene ,
                summary_snvindel ,
                summary_cnv ,
                summary_exp ,
                summary_meth ,
                data ) values (
                ?,?,?,?,?  ,?,?,?,?,? ,?,?,?)
            """
        self.cur.executemany(sql,records_list)
        self.con.commit()

    def insertDiseaseOntologyRecored(self,record_json):
        sql = """
        insert into overview_disease_ontology (
                doid ,
                data 
                ) values 
                (?,?)
                """
        try:
            self.cur.execute(sql,(record_json['doid'],json.dumps(record_json),))
            self.con.commit()
            return True
        except Exception as e :
            logging.error("Can not excute insertDiseaseOntologyRecored, reason:{e}")
            return False

    def close(self):
        self.con.commit()
        self.con.close()

class mysqlUtils():
    
    # def __init__(self,confobj):
    def __init__(self):
        self.host = "192.168.164.83"
        self.port = "33067"
        self.username = "zhengxc"
        self.password = "canceranno"
        self.dbname = "cancerkdb"
        self.charsets = "UTF8"

        self.base_header = "INSERT INTO {}.".format(self.dbname)
        try:
            self.con = pymysql.Connect(
            host=self.host,
            port = int(self.port),
            user=self.username,
            passwd = self.password,
            db=self.dbname,
            charset=self.charsets,
            cursorclass=pymysql.cursors.DictCursor  # return the query results in dict format not the tuple format.
            )
            #获得数据库的游标
            self.cursor = self.con.cursor() #开启事务
            logging.info("Get cursor successfully")
        except Exception as e :
            logging.info("Can not connect databse {}\nReason:{}".format(self.dbname,e))

    def close(self):
        if  self.con:
            self.con.commit()
            self.con.close()
            logging.info("Close database {} successfully".format(self.dbname))
        else:
            logging.info("DataBase doesn't connect,close connectiong error;please check the db config.")

    def fetchOne(self):
        data = self.cursor.fetchone()
        return(data)

    def fetchAll(self):
        data  = self.cursor.fetchall()
        return(data)

    def excute(self,sql,data = None):
        if data is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql,data)

        return(self.cursor.rowcount)

    def commit(self):
        self.con.commit()

   
    def rollback(self):
        self.con.rollback()
        logging.info("RollBack Transaction")


class annotatedb(mysqlUtils): # inherient from mysqlUtils class

    def __inti__(self):
        pass
    def select_dgidb(self,geneid):
        sql  = "select * from dgidbaggr where EnsemblID = '{}'".format(geneid)
        self.excute(sql)
        return(self.fetchAll())

    def batch_select_dgidb(self,geneid_list):
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from dgidbaggr where EnsemblID in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())    

    def select_cancermine(self,geneid):
        sql  = "select * from cancermineaggr2 where ENSGID = '{}'".format(geneid)
        self.excute(sql)
        return(self.fetchAll())

    def batch_select_cancermine(self,geneid_list):
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from cancermineaggr2 where ENSGID in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())    


    def select_ensembl2reactome(self,geneid):
        sql  = "select * from ensembl2reactome where ENSEMBLID = '{}'".format(geneid)
        self.excute(sql)
        return(self.fetchAll())

    def batch_select_ensembl2reactome(self,geneid_list):    
        """Deprecated"""
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from ensembl2reactome where ENSEMBLID in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())         

    def batch_select_ensembl2reactome_join_pathwaydetail(self,geneid_list):    
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        # sql  = "select * from ensembl2reactome where ENSEMBLID in ({}); ".format(format_strings)
        sql  = "SELECT *  from  reactome_pathway  as r left join ensembl2reactome as e  on r.ID = e.ReactomeID WHERE e.ENSEMBLID in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())            
    
    def select_intogen(self,geneid):
        sql  = "select * from intogen where ENSEMBL_GENE_ID = '{}'".format(geneid)
        self.excute(sql)
        return(self.fetchAll())

    def batch_select_intogen(self,geneid_list):    
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from intogen where ENSEMBL_GENE_ID in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())            
    
    def select_opentarget(self,geneid):
        
        sql  = "select * from opentarget where targetId = '{}'".format(geneid)
        self.excute(sql)
        return(self.fetchAll())
    def batch_select_opentarget(self,geneid_list): 
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from opentarget where targetId in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())    

    def select_uniprot(self,geneid):
        
        sql  = "select * from uniprot_human where EnsemblID = '{}'".format(geneid)
        self.excute(sql)
        return(self.fetchAll())
    def batch_select_uniprot(self,geneid_list): 
        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from uniprot_human where EnsemblID in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())    

    def select_diseaseontology(self,DOID):
        sql  = "select * from do_mesh_nct where DOID = '{}'".format(DOID)
        self.excute(sql)
        return(self.fetchAll())

    def select_clinicaltrials(self,nctids):
        sql  = "select * from clinicaltrials  where NCTID IN ( {} )  ".format( "'" + "','".join(nctids) +"'" )
        self.excute(sql)
        return(self.fetchAll())  
    def select_reactome_pathway(self,reactomeid):
        sql  = "SELECT * from  reactome_pathway WHERE ID = '{}'".format(reactomeid)
        self.excute(sql)
        return(self.fetchOne())      

    def select_IDs_from_hgnc_by_ENSGID(self,geneid):
        sql  = "select * from hgnc_projection  h WHERE h.ensembl_gene_id = '{}'; ".format(geneid)
        self.excute(sql)
        return(self.fetchOne()) 

    def batch_select_IDs_from_hgnc_by_ENSGID(self,geneid_list):

        format_strings = ','.join(['(%s)'] * len(geneid_list))
        sql  = "select * from hgnc_projection  h WHERE h.ensembl_gene_id in ({}); ".format(format_strings)
        # print(sql)
        self.excute(sql,tuple(geneid_list))
        return(self.fetchAll())        


    def select_DiseaseOntology_by_ID(self,doid):
        sql  = "select * from full_DOID_list f WHERE f.doid  = '{}'; ".format(doid)
        self.excute(sql)
        return(self.fetchOne())   


def combineMultiOmicsJson(jsonSNVIndel,jsonExp,jsonCNV,jsonMeth):
    """
    combine all omics json file into one and each term starts with patient_*
    """
    combine = {}

    snvindel_gene = list(jsonSNVIndel.keys())
    logging.info(f"A total of snvindel_gene {(len(snvindel_gene))} genes found!")
    exp_gene = list(jsonExp.keys())
    logging.info(f"A total of exp_gene {(len(exp_gene))} genes found!")
    cnv_gene = list(jsonCNV.keys())
    logging.info(f"A total of snvindel_gcnv_geneene {(len(cnv_gene))} genes found!")
    meth_gene = list(jsonMeth.keys())
    logging.info(f"A total of meth_gene {(len(meth_gene))} genes found!")
    all_gene = list(set(snvindel_gene + exp_gene + cnv_gene + meth_gene))
    logging.info(f"A total of {(len(all_gene))} genes found!")
    # combine['patient_exp_list'] = 
    # combine['patient_CNV_list'] = 
    # combine['patient_meth_list'] 
    """
    {
        "GENEID:ENSG00000067606": {
            "ENSG": "GENEID:ENSG00000067606",
            "value": "396",
            "regions": "chr1:2026474:3298168:396"
        },
    }


    {
        "GENEID:ENSG00000142655": {
        "ENSG": "ENSG00000142655",
        "patient_snvindel_list":[
            {
                xxx
            }
        ]
    }
    """

    # create combine gene list
    for one in all_gene:
        if one not in combine.keys():
            combine[one]={}
            if one in jsonSNVIndel.keys():
                combine[one]['patient_snvindel_list'] = jsonSNVIndel[one]["patient_snvindel_list"]
            if one in jsonExp.keys():
                combine[one]['patient_exp_list'] = [jsonExp[one]]
            if one in jsonCNV.keys():
                combine[one]['patient_cnv_list'] = [jsonCNV[one]]
            if one in jsonMeth.keys():
                combine[one]['patient_meth_list'] = [jsonMeth[one]]            
        else:
            if one in jsonSNVIndel.keys():
                combine[one]['patient_snvindel_list'].extend(jsonSNVIndel[one]["patient_snvindel_list"])
            if one in jsonExp.keys():
                combine[one]['patient_exp_list'].append(jsonExp[one])
            if one in jsonCNV.keys():
                combine[one]['patient_cnv_list'].append(jsonCNV[one])
            if one in jsonMeth.keys():
                combine[one]['patient_meth_list'].append(jsonMeth[one])                   
        combine[one]['ensembl_gene_id'] = one.replace("GENEID:","")
    
    # add emtpy patient list to build for category for each gene
    for onegene in combine.keys():
        if combine[onegene].get("patient_snvindel_list",None) is None:
            combine[onegene]['patient_snvindel_list'] = []
            
        if combine[onegene].get("patient_exp_list",None) is None:
            combine[onegene]['patient_exp_list'] = []
        if combine[onegene].get("patient_cnv_list",None) is None:
            combine[onegene]['patient_cnv_list'] = []
        if combine[onegene].get("patient_meth_list",None) is None:
            combine[onegene]['patient_meth_list'] = []

    return combine 

def addIDsToCombinedOmicsData(combine):
    dbutil = annotatedb()
    count = 0
    interval = 100
    ENSGList = [x.replace("GENEID:","") for x in combine.keys()]
    
    for i in range(0, len(ENSGList), interval):
        subENSGList=ENSGList[i:i + interval]
        count += 1
        # print(count)
        reslist = dbutil.batch_select_IDs_from_hgnc_by_ENSGID(subENSGList)
        for res in reslist:
            
            if res is not None: 
                this_ENSG = "GENEID:"+res['ensembl_gene_id']
                # print(this_ENSG)
                combine[this_ENSG]['hgnc_id'] = res.get("hgnc_id",None)
                combine[this_ENSG]['symbol'] = res.get("symbol",None)
                combine[this_ENSG]['entrez_id'] = res.get("entrez_id",None)
                combine[this_ENSG]['ucsc_id'] = res.get("ucsc_id",None)
                combine[this_ENSG]['uniprot_ids'] = res.get("uniprot_ids",None)
                combine[this_ENSG]['symbol'] = res.get("symbol",None)
                combine[this_ENSG]['name'] = res.get("name",None)
                combine[this_ENSG]['locus_type'] = res.get("locus_type",None)
                combine[this_ENSG]['location'] = res.get("location",None)
                combine[this_ENSG]['gene_family'] = res.get("gene_family",None)
        #     # else:
            #     combine[x]['hgnc_id'] = None
            #     combine[x]['symbol'] = None            
            #     combine[x]['entrez_id'] = None
            #     combine[x]['ucsc_id'] = None
            #     combine[x]['uniprot_ids'] = None
    
    dbutil.close()
    return combine


def checkVcfIsOK(vcf):
    count = 0
    startWithSharpLine = False
    startWithChrLine = False
    with open(vcf) as inf:
        for a in inf:
            count +=1
            if a.strip().startswith('#'):
                startWithSharpLine = True
            if a.strip().startswith("chr"):
                startWithChrLine = True
    if  startWithSharpLine == True and  startWithChrLine == True and  count >0:
        return True
    else:
        return False        

def addGlobalError(err):
    myconfig.globalError.append(err)

if __name__ == "__main__":
    import json
    logging.basicConfig(level=logging.INFO,format="[%(levelname)s - %(asctime)s] %(message)s")
    methret = ProcessCNVAndMethlation.process("./demo/cnv.txt","region","hg19","aabb_ccdd_ee","./demo","cnv")
    cnvret = ProcessCNVAndMethlation.process("./demo/cnv.txt","region","hg19","aabb_ccdd_ee","./demo","cnv")
    expret = ProcessCNVAndMethlation.process("./demo/exp.tsv","gene","hg19","aabb_ccdd_ee","./demo","exp")

    # expret = {}
    # cnvret = {}
    # methret = {}

    snvret = json.load(open("/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/demo/test_snv.debug.gene.json"))
    
    combine = combineMultiOmicsJson(snvret,expret,cnvret,methret)

    combineAddIDs =  addIDsToCombinedOmicsData(combine=combine)

    print(json.dumps(combineAddIDs,indent=4))
             


                        
                    
                    