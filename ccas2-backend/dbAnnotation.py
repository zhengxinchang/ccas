import myutils
import logging
import os
import json
import myconfig

global null_str
null_str = "NULL"




#=========
def annotateVariantByDatabase(geneslit,DOID):
    
    outjson = {}

    # global mysql
    annodbManager = myutils.annotatedb()
    #==========================================
    #
    #    add database data into gene obj
    #
    #==========================================
    
    reactome_pathway_info = {}
    logging.info("Start to query gene list")

    interval = 800
    ENSGList = [x.replace("GENEID:","") for x in geneslit.keys()]
    

    for i in range(0, len(ENSGList), interval):
        subENSGList=ENSGList[i:i + interval]
        for geneid in subENSGList:
            geneslit[myutils.Utils.addGENEID( geneid)]['dgidb'] = []
            geneslit[myutils.Utils.addGENEID( geneid)]['cancermine'] = []
            geneslit[myutils.Utils.addGENEID( geneid)]['reactome'] = []
            geneslit[myutils.Utils.addGENEID( geneid)]['intogen'] = []
            geneslit[myutils.Utils.addGENEID( geneid)]['opentarget'] = []
            geneslit[myutils.Utils.addGENEID( geneid)]['uniprot'] = []
        logging.info("start to annotate dgidb")
        reslist = annodbManager.batch_select_dgidb(subENSGList)
        for res in reslist:
            if res is not None: 
                dgidbENSGID =  res['EnsemblID']
                geneslit[myutils.Utils.addGENEID(dgidbENSGID)]["dgidb"].append(res)
        logging.info("start to annotate cancermine")            
        reslist = annodbManager.batch_select_cancermine(subENSGList)
        for res in reslist:
            if res is not None: 
                cancermineENSGID =  res['ENSGID']
                geneslit[myutils.Utils.addGENEID(cancermineENSGID)]["cancermine"].append(res)
        logging.info("start to annotate intogen")        
        reslist = annodbManager.batch_select_intogen(subENSGList)
        for res in reslist:
            if res is not None: 
                intogenENSGID =  res['ENSEMBL_GENE_ID']
                geneslit[myutils.Utils.addGENEID(intogenENSGID)]["intogen"].append(res)

        logging.info("start to annotate opentarget")
        reslist = annodbManager.batch_select_opentarget(subENSGList)
        for res in reslist:
            if res is not None: 
                opentargetENSGID =  res['targetId']
                geneslit[myutils.Utils.addGENEID(opentargetENSGID)]["opentarget"].append(res)

        logging.info("start to annotate uniprot")
        reslist = annodbManager.batch_select_uniprot(subENSGList)
        for res in reslist:
            if res is not None: 
                uniportENSGID =  res['EnsemblID']
                geneslit[myutils.Utils.addGENEID(uniportENSGID)]["uniprot"].append(res)

        logging.info("start to annotate reactome")
        reslist = list(annodbManager.batch_select_ensembl2reactome_join_pathwaydetail(subENSGList))
        for res in reslist:
            if res is not None: 
                ensgID =  res['ENSEMBLID']
                newRes = res
                newRes['subEvent'] = json.loads(res['subEvent'])
                newRes['literatureReference'] = json.loads(res['literatureReference'])
                newRes['summation'] = json.loads(res['summation'])
                geneslit[myutils.Utils.addGENEID(ensgID)]["reactome"].append(newRes)
                reactomeID = res.get("ReactomeID",False)
                if reactomeID:
                    # logging.info("start to build overview pathway")
                    reactomeENSGID = annodbManager.select_reactome_pathway(reactomeID) # return is a dict beacuse I use fetchOne() in return function
                    if reactomeID not in reactome_pathway_info.keys():
                        reactome_pathway_info[reactomeID] = reactomeENSGID
                        reactome_pathway_info[reactomeID]['HitsGene'] = [
                            {   "ENSG":ensgID,
                                "snvindel": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_snvindel_list']) > 0 else False,
                                "exp": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_exp_list']) > 0 else False,
                                "cnv": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_cnv_list']) > 0 else False,
                                "meth": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_meth_list']) > 0 else False,
                            }
                        ]

                        
                    else:
                        # logging.info(reactome_pathway_info[reactomeID])
                        reactome_pathway_info[reactomeID]['HitsGene'].append({
                                "ENSG":ensgID,
                                "snvindel": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_snvindel_list']) > 0 else False,
                                "exp": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_exp_list']) > 0 else False,
                                "cnv": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_cnv_list']) > 0 else False,
                                "meth": True if len(geneslit[myutils.Utils.addGENEID(ensgID)]['patient_meth_list']) > 0 else False,
                            })

    reactome_pathway_info_list = [v for v in reactome_pathway_info.values()]
    

    #========diseaseontology_mesh_nct==========

    if not DOID:
        logging.error("can not allocate gene object")
        exit(1)
    

    logging.info("Start to annotate clinical trials")
    DO_mesh_NCTID = list(annodbManager.select_diseaseontology(DOID))
    DO_mesh_NCTID_dict ={}
    if len(DO_mesh_NCTID) >0:
        DO_mesh_NCTID_dict = DO_mesh_NCTID[0]

        try:
            nctids = DO_mesh_NCTID_dict['NCTID'].split("/")
        except:
            nctids = []
            
        nctdata = []
        if len(nctids) > 0:
            
            nctdata = list(annodbManager.select_clinicaltrials(nctids))
            DO_mesh_NCTID_dict['NCTdata'] = nctdata

    outjson['overview']={}
    logging.info("Start to annotate Disease Ontology")
    DiseaseOntology = annodbManager.select_DiseaseOntology_by_ID(DOID)
    DiseaseOntologyData = json.loads(DiseaseOntology['data'])
    DiseaseOntologyData['doid'] = DiseaseOntology['doid']
    
    outjson['overview']["Disease_ontology"] = DiseaseOntologyData

    outjson['overview']["clinical_trials"] = DO_mesh_NCTID_dict

    logging.info("Start to annotate overview reactome_pathway")
    for onepathway in range(0,len(reactome_pathway_info_list)):
        countGeneType  = {
            "snvindel":0,
            "cnv":0,
            "exp":0,
            "meth":0,
        }
        for k in reactome_pathway_info_list[onepathway]['HitsGene']:
            if k['snvindel'] is True:
                countGeneType['snvindel'] +=1
            if k['exp'] is True:
                countGeneType['exp'] +=1
            if k['cnv'] is True:
                countGeneType['cnv'] +=1
            if k['meth'] is True:
                countGeneType['meth'] +=1
        reactome_pathway_info_list[onepathway]['HitsGeneSummary'] = countGeneType
    outjson['overview']["reactome_pathway"] = reactome_pathway_info_list


    #=========================================
    # add genelist into main json obj
    outjson['genelist'] =geneslit

    annodbManager.commit()
    annodbManager.close()
    return outjson

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO,format="[%(levelname)s - %(asctime)s] %(message)s")
    
    
    methret =  myutils.ProcessCNVAndMethlation.process("./demo/cnv.txt","region","hg19","aabb_ccdd_ee","./demo","cnv")
    cnvret = myutils.ProcessCNVAndMethlation.process("./demo/cnv.txt","region","hg19","aabb_ccdd_ee","./demo","cnv")
    expret =myutils.ProcessCNVAndMethlation.process("./demo/exp.tsv","gene","hg19","aabb_ccdd_ee","./demo","exp")

    # expret = {}
    # cnvret = {}
    # methret = {}

    snvret = json.load(open("/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/demo/test_snv.debug.gene.json"))
    
    combine = myutils.combineMultiOmicsJson(snvret,expret,cnvret,methret)

    combineAddIDs =  myutils.addIDsToCombinedOmicsData(combine=combine)
    dbAnnotatedResult = annotateVariantByDatabase(combineAddIDs,"DOID:3864")

    print(json.dumps(dbAnnotatedResult,indent=4))    