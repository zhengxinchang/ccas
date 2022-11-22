
from lib2to3.pgen2.pgen import generate_grammar
import myutils
import os
from collections import OrderedDict
import json 
"""
将数据存储到工作目录，
overview - clinical_trials - NCTdata -> sqlite3.overview_clinical
genelist -> sqlite3.gene
overview - reactome_pathway -> sqlite3.overview_pathway
other metadata in overview - clinical_trials will be dump to json file 'jobid.overview.disease'
"""

def dump2Disk(outdir,jobid,dbAnnojson):
    outdbname = os.path.join(outdir,jobid+".data.sqlite3")
    dbutil = myutils.sqlite3Utils(outdbname)
    dbutil.init_tables()
    genelist = dbAnnojson.get("genelist",None)
    if genelist is None:
        return {"status":False,"msg":"genelist is None"} # failed to dump to sqlite3

    # 将dict格式的转换为列表，存放到todump中并存入sqlite数据库
    toGeneDump = []
    for geneid,gene in genelist.items():
        tgene =  [
                geneid, #"geneid" : 
                gene.get('symbol',None), 
                gene.get('entrez_id',None), 
                gene.get('ucsc_id',None), 
                gene.get('uniprot_ids',None),
                gene.get('name',None), 
                gene.get('locus_type',None), 
                gene.get('location',None), 
                gene.get('gene_family',None),
                len(gene['patient_snvindel_list'] ), #"Nsnvindel" : 
                len(gene['patient_cnv_list']), #"Ncnv" : 
                len(gene['patient_exp_list']), #"Nexp" : 
                len(gene['patient_meth_list']), #"Nmeth" : 
                len(gene['cancermine']), #"Npaper": 
                len(gene['dgidb']) + len(gene['opentarget']), #"Ndruginter" : 
                len(gene['reactome']), #"Npathway" : 
                len(gene['intogen']), #"NCancerCohort" : 
                
            ]

        # 以下添加 exp meth cnv 的value ，以及snv的 IMPACT的列表去重  Consequence 去重

        cnv_value = gene.get("patient_cnv_list")[0].get("value",None) if  len(gene.get("patient_cnv_list"))>0  else None
        exp_value = gene.get("patient_exp_list")[0].get("value",None) if  len(gene.get("patient_exp_list"))>0  else None
        meth_value = gene.get("patient_meth_list")[0].get("value",None) if  len(gene.get("patient_meth_list"))>0  else None
        
        tgene.append(cnv_value)
        tgene.append(exp_value)
        tgene.append(meth_value)

        impact_consequence_count_list = OrderedDict()
        impact_consequence_count_list["HIGH"] = 0 
        impact_consequence_count_list["LOW"] = 0 
        impact_consequence_count_list["MODERATE"] = 0 
        impact_consequence_count_list["MODIFIER"] = 0 
        impact_consequence_count_list["HIGH"] = 0
        impact_consequence_count_list["LOW"] = 0
        impact_consequence_count_list["MODERATE"] = 0
        impact_consequence_count_list["MODIFIER"] = 0
        impact_consequence_count_list["transcript_ablation"] = 0
        impact_consequence_count_list["splice_acceptor_variant"] = 0
        impact_consequence_count_list["splice_donor_variant"] = 0
        impact_consequence_count_list["stop_gained"] = 0
        impact_consequence_count_list["frameshift_variant"] = 0
        impact_consequence_count_list["stop_lost"] = 0
        impact_consequence_count_list["start_lost"] = 0
        impact_consequence_count_list["transcript_amplification"] = 0
        impact_consequence_count_list["inframe_insertion"] = 0
        impact_consequence_count_list["inframe_deletion"] = 0
        impact_consequence_count_list["missense_variant"] = 0
        impact_consequence_count_list["protein_altering_variant"] = 0
        impact_consequence_count_list["splice_region_variant"] = 0
        impact_consequence_count_list["incomplete_terminal_codon_variant"] = 0
        impact_consequence_count_list["start_retained_variant"] = 0
        impact_consequence_count_list["stop_retained_variant"] = 0
        impact_consequence_count_list["synonymous_variant"] = 0
        impact_consequence_count_list["coding_sequence_variant"] = 0
        impact_consequence_count_list["mature_miRNA_variant"] = 0
        impact_consequence_count_list["5_prime_UTR_variant"] = 0
        impact_consequence_count_list["3_prime_UTR_variant"] = 0
        impact_consequence_count_list["non_coding_transcript_exon_variant"] = 0
        impact_consequence_count_list["intron_variant"] = 0
        impact_consequence_count_list["NMD_transcript_variant"] = 0
        impact_consequence_count_list["non_coding_transcript_variant"] = 0
        impact_consequence_count_list["upstream_gene_variant"] = 0
        impact_consequence_count_list["downstream_gene_variant"] = 0
        impact_consequence_count_list["TFBS_ablation"] = 0
        impact_consequence_count_list["TFBS_amplification"] = 0
        impact_consequence_count_list["TF_binding_site_variant"] = 0
        impact_consequence_count_list["regulatory_region_ablation"] = 0
        impact_consequence_count_list["regulatory_region_amplification"] = 0
        impact_consequence_count_list["feature_elongation"] = 0
        impact_consequence_count_list["regulatory_region_variant"] = 0
        impact_consequence_count_list["feature_truncation"] = 0
        impact_consequence_count_list["intergenic_variant"] = 0

        for onevar in gene.get("patient_snvindel_list",[]):
            impact = onevar['vep'][0].get("IMPACT")
            impact_consequence_count_list[impact] +=1

        for onevar in gene.get("patient_snvindel_list",[]):
            consequence = onevar['vep'][0].get("Consequence")
            consequence_list = consequence.split("&")
            for ccc in consequence_list:
                impact_consequence_count_list[ccc] +=1

        tgene.extend(list(impact_consequence_count_list.values()))
        tgene.append(json.dumps(gene))
        toGeneDump.append(tgene)

    try:
        dbutil.batchInsertGeneRecords(toGeneDump)
    except Exception as e :
        return  {"status":False,"msg":f"dump gene recored failed :{str(e)}"}

    clinicaltriallist = dbAnnojson.get("overview",{}).get("clinical_trials",{}).get("NCTdata",[])

    toClinicalDump=[]
    for oneclin in clinicaltriallist:
        toClinicalDump.append(
            [
            oneclin['NCTID'],
            oneclin.get('URL',None),
            oneclin.get('BriefTitle',None),
            oneclin.get('BriefSummary',None),
            oneclin.get('DetailDescription',None),
            oneclin.get('EligbilityCriteria',None),
            oneclin.get('Reference',None),
            oneclin.get('Phase',None),
            oneclin.get('Intervention',None),
            oneclin.get('MESH',None),
            json.dumps(oneclin)
            ]
        )
    
    try:
        dbutil.batchInsertOverviewclincialRecords(toClinicalDump)

    except Exception as e :
        return  {"status":False,"msg":f"dump clinical_trials recored failed:{str(e)}"}


    reactome_pathway = dbAnnojson.get("overview",{}).get("reactome_pathway",None)

    if reactome_pathway is None:
        return {"status":False,"msg":"reactome_pathway is None"} # failed to dump to sqlite3

    toPathwayDump=[]
    for oneclin in reactome_pathway:
        toPathwayDump.append(
            [
            oneclin['ID'],
            oneclin.get('DisplayName',None),
            oneclin.get('AlternavieNames',None),
            oneclin.get('Figure',None),
            oneclin.get('literatureReference',None),
            oneclin.get('summation',None),
            oneclin.get('subEvent',None),
            json.dumps(oneclin.get('HitsGene',None)),
            oneclin.get('HitsGeneSummary',{}).get("snvindel",None),
            oneclin.get('HitsGeneSummary',{}).get("cnv",None),
            oneclin.get('HitsGeneSummary',{}).get("exp",None),
            oneclin.get('HitsGeneSummary',{}).get("meth",None),
            json.dumps(oneclin)
            ]
        )
    
    try:
        dbutil.batchInsertOverviewpathwayRecords(toPathwayDump)

    except Exception as e :
        return  {"status":False,"msg":f"dump pathway recored failed:{str(e)}"}

    # get overview -clinical and take the MESHIDs
    overview_tmp_clinical = dbAnnojson.get("overview",{}).get("clinical_trials",None)
    overview_disease_ontology =  dbAnnojson.get("overview",{}).get("Disease_ontology",None)
    if overview_tmp_clinical is None or overview_disease_ontology is None:
        return {"status":False,"msg":"overview_disease is None"} # failed to dump to sqlite3
    
    overview_disease2dump = { k:v for k,v in overview_disease_ontology.items()}
    overview_disease2dump['MESHID'] = overview_tmp_clinical.get("MESH_ID",None)
    overview_disease2dump['MESH_Terms'] = overview_tmp_clinical.get("MESH_Terms","").split("/")

    dbutil.insertDiseaseOntologyRecored(overview_disease2dump)



    dbutil.close()
    return {"status":True,"msg":"all have dumped into sqlite3 db"}

if __name__ == "__main__":

    import json
    d = json.load(open("./demo/dbAnnotated.json"))
    res = dump2Disk("./demo","aa_bb_cc_dd_ee",d)
    print(res)
