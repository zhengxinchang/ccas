import logging
logging.basicConfig(level=logging.DEBUG,format="<<< %(asctime)s : %(funcName)s : %(levelname)s >>> %(message)s")

BASE_URL="/ccas"
appname = "ccas"
workspaceRoot = "/canceranno/zhengxc/ccas2/workspace/public"
CCASpipeline = "/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/CCASannotator.py"
this_mode = "dev"

if this_mode == "dev":
    mysql_username="root"
    mysql_pwd=""
    mysql_port=""
    mysql_host=""
    mysql_dbname=""
elif this_mode == "prod":
    mysql_username="root"
    mysql_pwd=""
    mysql_port=""
    mysql_host=""
    mysql_dbname=""

mail = {
    "f_addr":'zhengxc_auto@163.com',
    "f_pswd":'',
    "f_smtp":'smtp.163.com',
    "bottom_text":"Sencerely,\nCCAS team.\nNote:This Message was sent automatically. Please DO NOT reply it. \nIf you have any questions, please feel free to contact zhengxinchang@big.ac.cn"
}



signatureDesc = {
    "S1": {
        "ID": "1",
        "CancerTypes": " Signature 1 has been found in all cancer types and in most cancer samples.",
        "ProposedAetiology": "Signature 1 is the result of an endogenous mutational process initiated by spontaneous deamination of 5-methylcytosine.",
        "AdditionalFeatures": "Signature 1 is associated with small numbers of small insertions and deletions in most tissue types.",
        "Comments": "The number of Signature 1 mutations correlates with age of cancer diagnosis."
    },
    "S10": {
        "ID": "10",
        "CancerTypes": " Signature 10 has been found in six cancer types, notably colorectal and uterine cancer, usually generating huge numbers of mutations in small subsets of samples.",
        "ProposedAetiology": "It has been proposed that the mutational process underlying this signature is altered activity of the error-prone polymerase POLE. The presence of large numbers of Signature 10 mutations is associated with recurrent POLE somatic mutations, viz., Pro286Arg and Val411Leu.",
        "AdditionalFeatures": "Signature 10 exhibits strand bias for C>A mutations at TpCpT context and T>G mutations at TpTpT context.",
        "Comments": "Signature 10 is associated with some of most mutated cancer samples. Samples exhibiting this mutational signature have been termed ultra-hypermutators."
    },
    "S11": {
        "ID": "11",
        "CancerTypes": " Signature 11 has been found in melanoma and glioblastoma.",
        "ProposedAetiology": "Signature 11 exhibits a mutational pattern resembling that of alkylating agents. Patient histories have revealed an association between treatments with the alkylating agent temozolomide and Signature 11 mutations.",
        "AdditionalFeatures": "Signature 11 exhibits a strong transcriptional strand-bias for C>T substitutions indicating that mutations occur on guanine and that these mutations are effectively repaired by transcription-coupled nucleotide excision repair.",
        "Comments": "NA"
    },
    "S12": {
        "ID": "12",
        "CancerTypes": " Signature 12 has been found in liver cancer.",
        "ProposedAetiology": "The aetiology of Signature 12 remains unknown.",
        "AdditionalFeatures": "Signature 12 exhibits a strong transcriptional strand-bias for T>C substitutions.",
        "Comments": "Signature 12 usually contributes a small percentage (<20%) of the mutations observed in a liver cancer sample."
    },
    "S13": {
        "ID": "13",
        "CancerTypes": " Signature 13 has been found in 22 cancer types and seems to be commonest in cervical and bladder cancers. In most of these 22 cancer types, Signature 13 is present in at least 10% of samples.",
        "ProposedAetiology": "Signature 13 has been attributed to activity of the AID/APOBEC family of cytidine deaminases converting cytosine to uracil. On the basis of similarities in the sequence context of cytosine mutations caused by APOBEC enzymes in experimental systems, a role for APOBEC1, APOBEC3A and/or APOBEC3B in human cancer appears more likely than for other members of the family. Signature 13 causes predominantly C>G mutations. This may be due to generation of abasic sites after removal of uracil by base excision repair and replication over these abasic sites by REV1.",
        "AdditionalFeatures": "Transcriptional strand bias of mutations has been observed in exons, but is not present or is weaker in introns.",
        "Comments": "Signature 2 is usually found in the same samples as Signature 13. It has been proposed that activation of AID/APOBEC cytidine deaminases is due to viral infection, retrotransposon jumping or to tissue inflammation. Currently, there is limited evidence to support these hypotheses. A germline deletion polymorphism involving APOBEC3A and APOBEC3B is associated with the presence of large numbers of Signature 2 and 13 mutations and with predisposition to breast cancer. Mutations of similar patterns to Signatures 2 and 13 are commonly found in the phenomenon of local hypermutation present in some cancers, known as kataegis, potentially implicating AID/APOBEC enzymes in this process as well."
    },
    "S14": {
        "ID": "14",
        "CancerTypes": " Signature 14 has been observed in four uterine cancers and a single adult low-grade glioma sample.",
        "ProposedAetiology": "The aetiology of Signature 14 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "Signature 14 generates very high numbers of somatic mutations (>200 mutations per MB) in all samples in which it has been observed."
    },
    "S15": {
        "ID": "15",
        "CancerTypes": " Signature 15 has been found in several stomach cancers and a single small cell lung carcinoma.",
        "ProposedAetiology": "Signature 15 is associated with defective DNA mismatch repair.",
        "AdditionalFeatures": "Signature 15 is associated with high numbers of small (shorter than 3bp) insertions and deletions at mono/polynucleotide repeats.",
        "Comments": "Signature 15 is one of four mutational signatures associated with defective DNA mismatch repair and is often found in the same samples as Signatures 6, 20, and 26."
    },
    "S16": {
        "ID": "16",
        "CancerTypes": " Signature 16 has been found in liver cancer.",
        "ProposedAetiology": "The aetiology of Signature 16 remains unknown.",
        "AdditionalFeatures": "Signature 16 exhibits an extremely strong transcriptional strand bias for T>C mutations at ApTpN context, with T>C mutations occurring almost exclusively on the transcribed strand.",
        "Comments": "NA"
    },
    "S17": {
        "ID": "17",
        "CancerTypes": " Signature 17 has been found in oesophagus cancer, breast cancer, liver cancer, lung adenocarcinoma, B-cell lymphoma, stomach cancer and melanoma.",
        "ProposedAetiology": "The aetiology of Signature 17 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "NA"
    },
    "S18": {
        "ID": "18",
        "CancerTypes": " Signature 18 has been found commonly in neuroblastoma. Additionally, Signature 18 has been also observed in breast and stomach carcinomas.",
        "ProposedAetiology": "The aetiology of Signature 18 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "NA"
    },
    "S19": {
        "ID": "19",
        "CancerTypes": " Signature 19 has been found only in pilocytic astrocytoma.",
        "ProposedAetiology": "The aetiology of Signature 19 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "NA"
    },
    "S2": {
        "ID": "2",
        "CancerTypes": " Signature 2 has been found in 22 cancer types, but most commonly in cervical and bladder cancers. In most of these 22 cancer types, Signature 2 is present in at least 10% of samples.",
        "ProposedAetiology": "Signature 2 has been attributed to activity of the AID/APOBEC family of cytidine deaminases. On the basis of similarities in the sequence context of cytosine mutations caused by APOBEC enzymes in experimental systems, a role for APOBEC1, APOBEC3A and/or APOBEC3B in human cancer appears more likely than for other members of the family.",
        "AdditionalFeatures": "Transcriptional strand bias of mutations has been observed in exons, but is not present or is weaker in introns.NA",
        "Comments": "Signature 2 is usually found in the same samples as Signature 13. It has been proposed that activation of AID/APOBEC cytidine deaminases is due to viral infection, retrotransposon jumping or to tissue inflammation. Currently, there is limited evidence to support these hypotheses. A germline deletion polymorphism involving APOBEC3A and APOBEC3B is associated with the presence of large numbers of Signature 2 and 13 mutations and with predisposition to breast cancer. Mutations of similar patterns to Signatures 2 and 13 are commonly found in the phenomenon of local hypermutation present in some cancers, known as kataegis, potentially implicating AID/APOBEC enzymes in this process as well."
    },
    "S20": {
        "ID": "20",
        "CancerTypes": " Signature 20 has been found in stomach and breast cancers.",
        "ProposedAetiology": "Signature 20 is believed to be associated with defective DNA mismatch repair.",
        "AdditionalFeatures": "Signature 20 is associated with high numbers of small (shorter than 3bp) insertions and deletions at mono/polynucleotide repeats.",
        "Comments": "Signature 20 is one of four mutational signatures associated with defective DNA mismatch repair and is often found in the same samples as Signatures 6, 15, and 26."
    },
    "S21": {
        "ID": "21",
        "CancerTypes": " Signature 21 has been found only in stomach cancer.",
        "ProposedAetiology": "The aetiology of Signature 21 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "Signature 21 is found only in four samples all generated by the same sequencing centre. The mutational pattern of Signature 21 is somewhat similar to the one of Signature 26. Additionally, Signature 21 is found only in samples that also have Signatures 15 and 20. As such, Signature 21 is probably also related to microsatellite unstable tumours."
    },
    "S22": {
        "ID": "22",
        "CancerTypes": " Signature 22 has been found in urothelial (renal pelvis) carcinoma and liver cancers.",
        "ProposedAetiology": "Signature 22 has been found in cancer samples with known exposures to aristolochic acid. Additionally, the pattern of mutations exhibited by the signature is consistent with the one previous observed in experimental systems exposed to aristolochic acid.",
        "AdditionalFeatures": "Signature 22 exhibits a very strong transcriptional strand bias for T>A mutations indicating adenine damage that is being repaired by transcription-coupled nucleotide excision repair.",
        "Comments": "Signature 22 has a very high mutational burden in urothelial carcinoma; however, its mutational burden is much lower in liver cancers."
    },
    "S23": {
        "ID": "23",
        "CancerTypes": " Signature 23 has been found only in a single liver cancer sample.",
        "ProposedAetiology": "The aetiology of Signature 23 remains unknown.",
        "AdditionalFeatures": "Signature 23 exhibits very strong transcriptional strand bias for C>T mutations.",
        "Comments": "NA"
    },
    "S24": {
        "ID": "24",
        "CancerTypes": " Signature 24 has been observed in a subset of liver cancers.",
        "ProposedAetiology": "Signature 24 has been found in cancer samples with known exposures to aflatoxin. Additionally, the pattern of mutations exhibited by the signature is consistent with that previous observed in experimental systems exposed to aflatoxin.",
        "AdditionalFeatures": "Signature 24 exhibits a very strong transcriptional strand bias for C>A mutations indicating guanine damage that is being repaired by transcription-coupled nucleotide excision repair.",
        "Comments": "NA"
    },
    "S25": {
        "ID": "25",
        "CancerTypes": " Signature 25 has been observed in Hodgkin lymphomas.",
        "ProposedAetiology": "The aetiology of Signature 25 remains unknown.",
        "AdditionalFeatures": "Signature 25 exhibits transcriptional strand bias for T>A mutations.",
        "Comments": "This signature has only been identified in Hodgkin\u2019s cell lines. Data is not available from primary Hodgkin lymphomas."
    },
    "S26": {
        "ID": "26",
        "CancerTypes": " Signature 26 has been found in breast cancer, cervical cancer, stomach cancer and uterine carcinoma.",
        "ProposedAetiology": "Signature 26 is believed to be associated with defective DNA mismatch repair.",
        "AdditionalFeatures": "Signature 26 is associated with high numbers of small (shorter than 3bp) insertions and deletions at mono/polynucleotide repeats.",
        "Comments": "Signature 26 is one of four mutational signatures associated with defective DNA mismatch repair and is often found in the same samples as Signatures 6, 15 and 20."
    },
    "S27": {
        "ID": "27",
        "CancerTypes": " Signature 27 has been observed in a subset of kidney clear cell carcinomas.",
        "ProposedAetiology": "The aetiology of Signature 27 remains unknown.",
        "AdditionalFeatures": "Signature 27 exhibits very strong transcriptional strand bias for T>A mutations. Signature 27 is associated with high numbers of small (shorter than 3bp) insertions and deletions at mono/polynucleotide repeats.",
        "Comments": "NA"
    },
    "S28": {
        "ID": "28",
        "CancerTypes": " Signature 28 has been observed in a subset of stomach cancers.",
        "ProposedAetiology": "The aetiology of Signature 28 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "NA"
    },
    "S29": {
        "ID": "29",
        "CancerTypes": " Signature 29 has been observed only in gingivo-buccal oral squamous cell carcinoma.",
        "ProposedAetiology": "Signature 29 has been found in cancer samples from individuals with a tobacco chewing habit.",
        "AdditionalFeatures": "Signature 29 exhibits transcriptional strand bias for C>A mutations indicating guanine damage that is most likely repaired by transcription-coupled nucleotide excision repair. Signature 29 is also associated with CC>AA dinucleotide substitutions.",
        "Comments": "The Signature 29 pattern of C>A mutations due to tobacco chewing appears different from the pattern of mutations due to tobacco smoking reflected by Signature 4."
    },
    "S3": {
        "ID": "3",
        "CancerTypes": " Signature 3 has been found in breast, ovarian, and pancreatic cancers.",
        "ProposedAetiology": "Signature 3 is associated with failure of DNA double-strand break-repair by homologous recombination.",
        "AdditionalFeatures": "Signature 3 associates strongly with elevated numbers of large (longer than 3bp) insertions and deletions with overlapping microhomology at breakpoint junctions.",
        "Comments": "Signature 3 is strongly associated with germline and somatic BRCA1 and BRCA2 mutations in breast, pancreatic, and ovarian cancers. In pancreatic cancer, responders to platinum therapy usually exhibit Signature 3 mutations."
    },
    "S30": {
        "ID": "30",
        "CancerTypes": " Signature 30 has been observed in a small subset of breast cancers.",
        "ProposedAetiology": "The aetiology of Signature 30 remains unknown.",
        "AdditionalFeatures": "NA",
        "Comments": "NA"
    },
    "S4": {
        "ID": "4",
        "CancerTypes": " Signature 4 has been found in head and neck cancer, liver cancer, lung adenocarcinoma, lung squamous carcinoma, small cell lung carcinoma, and oesophageal cancer.",
        "ProposedAetiology": "Signature 4 is associated with smoking and its profile is similar to the mutational pattern observed in experimental systems exposed to tobacco carcinogens (e.g., benzo[a]pyrene). Signature 4 is likely due to tobacco mutagens.",
        "AdditionalFeatures": "Signature 4 exhibits transcriptional strand bias for C>A mutations, compatible with the notion that damage to guanine is repaired by transcription-coupled nucleotide excision repair. Signature 4 is also associated with CC>AA dinucleotide substitutions.",
        "Comments": "Signature 29 is found in cancers associated with tobacco chewing and appears different from Signature 4."
    },
    "S5": {
        "ID": "5",
        "CancerTypes": " Signature 5 has been found in all cancer types and most cancer samples.",
        "ProposedAetiology": "The aetiology of Signature 5 is unknown.",
        "AdditionalFeatures": "Signature 5 exhibits transcriptional strand bias for T>C substitutions at ApTpN context.",
        "Comments": "NA"
    },
    "S6": {
        "ID": "6",
        "CancerTypes": " Signature 6 has been found in 17 cancer types and is most common in colorectal and uterine cancers. In most other cancer types, Signature 6 is found in less than 3% of examined samples.",
        "ProposedAetiology": "Signature 6 is associated with defective DNA mismatch repair and is found in microsatellite unstable tumours.",
        "AdditionalFeatures": "Signature 6 is associated with high numbers of small (shorter than 3bp) insertions and deletions at mono/polynucleotide repeats.",
        "Comments": "Signature 6 is one of four mutational signatures associated with defective DNA mismatch repair and is often found in the same samples as Signatures 15, 20, and 26."
    },
    "S7": {
        "ID": "7",
        "CancerTypes": " Signature 7 has been found predominantly in skin cancers and in cancers of the lip categorized as head and neck or oral squamous cancers.",
        "ProposedAetiology": "Based on its prevalence in ultraviolet exposed areas and the similarity of the mutational pattern to that observed in experimental systems exposed to ultraviolet light Signature 7 is likely due to ultraviolet light exposure.",
        "AdditionalFeatures": "Signature 7 is associated with large numbers of CC>TT dinucleotide mutations at dipyrimidines. Additionally, Signature 7 exhibits a strong transcriptional strand-bias indicating that mutations occur at pyrimidines (viz., by formation of pyrimidine-pyrimidine photodimers) and these mutations are being repaired by transcription-coupled nucleotide excision repair.",
        "Comments": "NA"
    },
    "S8": {
        "ID": "8",
        "CancerTypes": " Signature 8 has been found in breast cancer and medulloblastoma.",
        "ProposedAetiology": "The aetiology of Signature 8 remains unknown.",
        "AdditionalFeatures": "Signature 8 exhibits weak strand bias for C>A substitutions and is associated with double nucleotide substitutions, notably CC>AA.",
        "Comments": "NA"
    },
    "S9": {
        "ID": "9",
        "CancerTypes": " Signature 9 has been found in chronic lymphocytic leukaemias and malignant B-cell lymphomas.",
        "ProposedAetiology": "Signature 9 is characterized by a pattern of mutations that has been attributed to polymerase \u03b7, which is implicated with the activity of AID during somatic hypermutation.",
        "AdditionalFeatures": "NA",
        "Comments": "Chronic lymphocytic leukaemias that possess immunoglobulin gene hypermutation (IGHV-mutated) have elevated numbers of mutations attributed to Signature 9 compared to those that do not have immunoglobulin gene hypermutation."
    }
}

disease_tree = {
    "dict": {
        "DOID:6128": {
            "DOID:6128": "gliomatosis cerebri(DOID:6128)"
        },
        "DOID:3016": {
            "DOID:3016": "breast malignant phyllodes tumor(DOID:3016)"
        },
        "DOID:3308": {
            "DOID:3308": "embryonal carcinoma(DOID:3308)"
        },
        "DOID:8858": {
            "DOID:8858": "tonsil cancer(DOID:8858)"
        },
        "DOID:8691": {
            "DOID:8691": "mycosis fungoides(DOID:8691)"
        },
        "DOID:5485": {
            "DOID:5485": "synovial sarcoma(DOID:5485)"
        },
        "DOID:3864": {
            "DOID:3864": "adult medulloblastoma(DOID:3864)"
        },
        "DOID:7213": {
            "DOID:7213": "transitional meningioma(DOID:7213)"
        },
        "DOID:1659": {
            "DOID:1659": "supratentorial cancer(DOID:1659)"
        },
        "DOID:4908": {
            "DOID:4908": "anal carcinoma(DOID:4908)"
        },
        "DOID:687": {
            "DOID:687": "hepatoblastoma(DOID:687)"
        },
        "DOID:4971": {
            "DOID:4971": "myelofibrosis(DOID:4971)"
        },
        "DOID:5820": {
            "DOID:5820": "composite lymphoma(DOID:5820)"
        },
        "DOID:9256": {
            "DOID:9256": "colorectal cancer(DOID:9256)"
        },
        "DOID:0060058": {
            "DOID:0060058": "lymphoma(DOID:0060058)"
        },
        "DOID:1993": {
            "DOID:1993": "rectum cancer(DOID:1993)"
        },
        "DOID:4362": {
            "DOID:4362": "cervical cancer(DOID:4362)"
        },
        "DOID:192": {
            "DOID:192": "sex cord-gonadal stromal tumor(DOID:192)"
        },
        "DOID:3277": {
            "DOID:3277": "thymus cancer(DOID:3277)"
        },
        "DOID:7912": {
            "DOID:7912": "mixed oligodendroglioma-astrocytoma(DOID:7912)"
        },
        "DOID:2776": {
            "DOID:2776": "adamantinoma(DOID:2776)"
        },
        "DOID:4441": {
            "DOID:4441": "dysgerminoma(DOID:4441)"
        },
        "DOID:12759": {
            "DOID:12759": "choroid cancer(DOID:12759)"
        },
        "DOID:2997": {
            "DOID:2997": "Sertoli-Leydig cell tumor(DOID:2997)"
        },
        "DOID:5958": {
            "DOID:5958": "bladder urachal carcinoma(DOID:5958)"
        },
        "DOID:4143": {
            "DOID:4143": "orbital cancer(DOID:4143)"
        },
        "DOID:5875": {
            "DOID:5875": "retroperitoneal cancer(DOID:5875)"
        },
        "DOID:4790": {
            "DOID:4790": "medulloepithelioma(DOID:4790)"
        },
        "DOID:8683": {
            "DOID:8683": "myeloid sarcoma(DOID:8683)"
        },
        "DOID:119": {
            "DOID:119": "vaginal cancer(DOID:119)"
        },
        "DOID:4085": {
            "DOID:4085": "trophoblastic neoplasm(DOID:4085)"
        },
        "DOID:3493": {
            "DOID:3493": "signet ring cell adenocarcinoma(DOID:3493)"
        },
        "DOID:1521": {
            "DOID:1521": "cecum cancer(DOID:1521)"
        },
        "DOID:10021": {
            "DOID:10021": "duodenum cancer(DOID:10021)"
        },
        "DOID:4916": {
            "DOID:4916": "pituitary carcinoma(DOID:4916)"
        },
        "DOID:3861": {
            "DOID:3861": "medullomyoblastoma(DOID:3861)"
        },
        "DOID:4320": {
            "DOID:4320": "non-gestational choriocarcinoma(DOID:4320)"
        },
        "DOID:4905": {
            "DOID:4905": "pancreatic carcinoma(DOID:4905)"
        },
        "DOID:3512": {
            "DOID:3512": "neurofibrosarcoma(DOID:3512)"
        },
        "DOID:5063": {
            "DOID:5063": "basosquamous carcinoma(DOID:5063)"
        },
        "DOID:4606": {
            "DOID:4606": "bile duct cancer(DOID:4606)"
        },
        "DOID:8538": {
            "DOID:8538": "reticulosarcoma(DOID:8538)"
        },
        "DOID:4205": {
            "DOID:4205": "cerebellum cancer(DOID:4205)"
        },
        "DOID:3305": {
            "DOID:3305": "teratocarcinoma(DOID:3305)"
        },
        "DOID:3113": {
            "DOID:3113": "papillary carcinoma(DOID:3113)"
        },
        "DOID:1664": {
            "DOID:1664": "pineoblastoma(DOID:1664)"
        },
        "DOID:4922": {
            "DOID:4922": "breast secretory carcinoma(DOID:4922)"
        },
        "DOID:5559": {
            "DOID:5559": "mediastinal cancer(DOID:5559)"
        },
        "DOID:3025": {
            "DOID:3025": "acinar cell carcinoma(DOID:3025)"
        },
        "DOID:3302": {
            "DOID:3302": "chordoma(DOID:3302)"
        },
        "DOID:4697": {
            "DOID:4697": "perineurioma(DOID:4697)"
        },
        "DOID:3382": {
            "DOID:3382": "liposarcoma(DOID:3382)"
        },
        "DOID:5411": {
            "DOID:5411": "lung oat cell carcinoma(DOID:5411)"
        },
        "DOID:8007": {
            "DOID:8007": "Pancoast tumor(DOID:8007)"
        },
        "DOID:154": {
            "DOID:154": "mixed cell type cancer(DOID:154)"
        },
        "DOID:1862": {
            "DOID:1862": "jaw cancer(DOID:1862)"
        },
        "DOID:4773": {
            "DOID:4773": "congenital mesoblastic nephroma(DOID:4773)"
        },
        "DOID:0080202": {
            "DOID:0080202": "adenoid cystic carcinoma(DOID:0080202)"
        },
        "DOID:219": {
            "DOID:219": "colon cancer(DOID:219)"
        },
        "DOID:3068": {
            "DOID:3068": "glioblastoma(DOID:3068)"
        },
        "DOID:3119": {
            "DOID:3119": "gastrointestinal system cancer(DOID:3119)"
        },
        "DOID:305": {
            "DOID:305": "carcinoma(DOID:305)"
        },
        "DOID:6262": {
            "DOID:6262": "follicular dendritic cell sarcoma(DOID:6262)"
        },
        "DOID:8628": {
            "DOID:8628": "Hodgkin's lymphoma, lymphocytic depletion(DOID:8628)"
        },
        "DOID:4450": {
            "DOID:4450": "renal cell carcinoma(DOID:4450)"
        },
        "DOID:5076": {
            "DOID:5076": "mixed glioma(DOID:5076)"
        },
        "DOID:4960": {
            "DOID:4960": "bone marrow cancer(DOID:4960)"
        },
        "DOID:2999": {
            "DOID:2999": "granulosa cell tumor(DOID:2999)"
        },
        "DOID:0080842": {
            "DOID:0080842": "intracranial meningioma(DOID:0080842)"
        },
        "DOID:4511": {
            "DOID:4511": "breast angiosarcoma(DOID:4511)"
        },
        "DOID:3112": {
            "DOID:3112": "papillary adenocarcinoma(DOID:3112)"
        },
        "DOID:3565": {
            "DOID:3565": "meningioma(DOID:3565)"
        },
        "DOID:4239": {
            "DOID:4239": "alveolar soft part sarcoma(DOID:4239)"
        },
        "DOID:8997": {
            "DOID:8997": "polycythemia vera(DOID:8997)"
        },
        "DOID:2155": {
            "DOID:2155": "malignant ovarian germ cell neoplasm(DOID:2155)"
        },
        "DOID:4914": {
            "DOID:4914": "esophagus adenocarcinoma(DOID:4914)"
        },
        "DOID:734": {
            "DOID:734": "urethra cancer(DOID:734)"
        },
        "DOID:162": {
            "DOID:162": "cancer(DOID:162)"
        },
        "DOID:10289": {
            "DOID:10289": "prostate malignant phyllodes tumor(DOID:10289)"
        },
        "DOID:7146": {
            "DOID:7146": "Langerhans cell sarcoma(DOID:7146)"
        },
        "DOID:8761": {
            "DOID:8761": "acute megakaryocytic leukemia(DOID:8761)"
        },
        "DOID:1192": {
            "DOID:1192": "peripheral nervous system neoplasm(DOID:1192)"
        },
        "DOID:9597": {
            "DOID:9597": "Krukenberg carcinoma(DOID:9597)"
        },
        "DOID:0060119": {
            "DOID:0060119": "pharynx cancer(DOID:0060119)"
        },
        "DOID:1799": {
            "DOID:1799": "islet cell tumor(DOID:1799)"
        },
        "DOID:3973": {
            "DOID:3973": "thyroid gland medullary carcinoma(DOID:3973)"
        },
        "DOID:4607": {
            "DOID:4607": "biliary tract cancer(DOID:4607)"
        },
        "DOID:1800": {
            "DOID:1800": "neuroendocrine carcinoma(DOID:1800)"
        },
        "DOID:3186": {
            "DOID:3186": "adult oligodendroglioma(DOID:3186)"
        },
        "DOID:2596": {
            "DOID:2596": "larynx cancer(DOID:2596)"
        },
        "DOID:5093": {
            "DOID:5093": "cavity(DOID:5093)"
        },
        "DOID:4927": {
            "DOID:4927": "Klatskin's tumor(DOID:4927)"
        },
        "DOID:7008": {
            "DOID:7008": "protoplasmic astrocytoma(DOID:7008)"
        },
        "DOID:5268": {
            "DOID:5268": "myxoid leiomyosarcoma(DOID:5268)"
        },
        "DOID:4929": {
            "DOID:4929": "tubular adenocarcinoma(DOID:4929)"
        },
        "DOID:3459": {
            "DOID:3459": "breast carcinoma(DOID:3459)"
        },
        "DOID:1319": {
            "DOID:1319": "brain cancer(DOID:1319)"
        },
        "DOID:2671": {
            "DOID:2671": "transitional cell carcinoma(DOID:2671)"
        },
        "DOID:4926": {
            "DOID:4926": "bronchiolo-alveolar adenocarcinoma(DOID:4926)"
        },
        "DOID:7305": {
            "DOID:7305": "astroblastoma(DOID:7305)"
        },
        "DOID:3121": {
            "DOID:3121": "gallbladder cancer(DOID:3121)"
        },
        "DOID:7005": {
            "DOID:7005": "gemistocytic astrocytoma(DOID:7005)"
        },
        "DOID:2876": {
            "DOID:2876": "laryngeal squamous cell carcinoma(DOID:2876)"
        },
        "DOID:0050619": {
            "DOID:0050619": "paranasal sinus cancer(DOID:0050619)"
        },
        "DOID:6496": {
            "DOID:6496": "extraskeletal myxoid chondrosarcoma(DOID:6496)"
        },
        "DOID:4531": {
            "DOID:4531": "mucoepidermoid carcinoma(DOID:4531)"
        },
        "DOID:1793": {
            "DOID:1793": "pancreatic cancer(DOID:1793)"
        },
        "DOID:5690": {
            "DOID:5690": "well-differentiated liposarcoma(DOID:5690)"
        },
        "DOID:4023": {
            "DOID:4023": "linitis plastica(DOID:4023)"
        },
        "DOID:3748": {
            "DOID:3748": "esophagus squamous cell carcinoma(DOID:3748)"
        },
        "DOID:5574": {
            "DOID:5574": "VIPoma(DOID:5574)"
        },
        "DOID:4588": {
            "DOID:4588": "secretory meningioma(DOID:4588)"
        },
        "DOID:3596": {
            "DOID:3596": "placental site trophoblastic tumor(DOID:3596)"
        },
        "DOID:4947": {
            "DOID:4947": "cholangiocarcinoma(DOID:4947)"
        },
        "DOID:2815": {
            "DOID:2815": "cranial nerve malignant neoplasm(DOID:2815)"
        },
        "DOID:3594": {
            "DOID:3594": "choriocarcinoma(DOID:3594)"
        },
        "DOID:1749": {
            "DOID:1749": "squamous cell carcinoma(DOID:1749)"
        },
        "DOID:3284": {
            "DOID:3284": "thymic carcinoma(DOID:3284)"
        },
        "DOID:4586": {
            "DOID:4586": "familial meningioma(DOID:4586)"
        },
        "DOID:688": {
            "DOID:688": "embryonal cancer(DOID:688)"
        },
        "DOID:4226": {
            "DOID:4226": "endometrial stromal sarcoma(DOID:4226)"
        },
        "DOID:660": {
            "DOID:660": "adrenal cortex cancer(DOID:660)"
        },
        "DOID:4473": {
            "DOID:4473": "sarcomatoid renal cell carcinoma(DOID:4473)"
        },
        "DOID:6193": {
            "DOID:6193": "epithelioid sarcoma(DOID:6193)"
        },
        "DOID:1785": {
            "DOID:1785": "pituitary cancer(DOID:1785)"
        },
        "DOID:4659": {
            "DOID:4659": "extracutaneous mastocytoma(DOID:4659)"
        },
        "DOID:2431": {
            "DOID:2431": "glomus tumor(DOID:2431)"
        },
        "DOID:7566": {
            "DOID:7566": "eccrine porocarcinoma(DOID:7566)"
        },
        "DOID:8654": {
            "DOID:8654": "Hodgkin's lymphoma, mixed cellularity(DOID:8654)"
        },
        "DOID:4468": {
            "DOID:4468": "clear cell adenocarcinoma(DOID:4468)"
        },
        "DOID:4136": {
            "DOID:4136": "myxosarcoma(DOID:4136)"
        },
        "DOID:9952": {
            "DOID:9952": "acute lymphoblastic leukemia(DOID:9952)"
        },
        "DOID:3540": {
            "DOID:3540": "choroid plexus cancer(DOID:3540)"
        },
        "DOID:9254": {
            "DOID:9254": "mast-cell leukemia(DOID:9254)"
        },
        "DOID:3030": {
            "DOID:3030": "mucinous adenocarcinoma(DOID:3030)"
        },
        "DOID:7698": {
            "DOID:7698": "non-functioning pancreatic endocrine tumor(DOID:7698)"
        },
        "DOID:0060597": {
            "DOID:0060597": "atypical chronic myeloid leukemia(DOID:0060597)"
        },
        "DOID:3842": {
            "DOID:3842": "skull base cancer(DOID:3842)"
        },
        "DOID:8161": {
            "DOID:8161": "thyroid gland Hurthle cell carcinoma(DOID:8161)"
        },
        "DOID:5409": {
            "DOID:5409": "lung small cell carcinoma(DOID:5409)"
        },
        "DOID:3369": {
            "DOID:3369": "Ewing sarcoma(DOID:3369)"
        },
        "DOID:4471": {
            "DOID:4471": "chromophobe renal cell carcinoma(DOID:4471)"
        },
        "DOID:355": {
            "DOID:355": "mast-cell sarcoma(DOID:355)"
        },
        "DOID:117": {
            "DOID:117": "heart cancer(DOID:117)"
        },
        "DOID:6114": {
            "DOID:6114": "cerebral convexity meningioma(DOID:6114)"
        },
        "DOID:7848": {
            "DOID:7848": "interdigitating dendritic cell sarcoma(DOID:7848)"
        },
        "DOID:2689": {
            "DOID:2689": "lymphangiosarcoma(DOID:2689)"
        },
        "DOID:2775": {
            "DOID:2775": "long bone adamantinoma(DOID:2775)"
        },
        "DOID:0050908": {
            "DOID:0050908": "myelodysplastic syndrome(DOID:0050908)"
        },
        "DOID:4992": {
            "DOID:4992": "optic nerve glioma(DOID:4992)"
        },
        "DOID:363": {
            "DOID:363": "uterine cancer(DOID:363)"
        },
        "DOID:3620": {
            "DOID:3620": "central nervous system cancer(DOID:3620)"
        },
        "DOID:4159": {
            "DOID:4159": "skin cancer(DOID:4159)"
        },
        "DOID:263": {
            "DOID:263": "kidney cancer(DOID:263)"
        },
        "DOID:7211": {
            "DOID:7211": "fibrous meningioma(DOID:7211)"
        },
        "DOID:3948": {
            "DOID:3948": "adrenocortical carcinoma(DOID:3948)"
        },
        "DOID:2394": {
            "DOID:2394": "ovarian cancer(DOID:2394)"
        },
        "DOID:4051": {
            "DOID:4051": "alveolar rhabdomyosarcoma(DOID:4051)"
        },
        "DOID:4359": {
            "DOID:4359": "amelanotic melanoma(DOID:4359)"
        },
        "DOID:4203": {
            "DOID:4203": "brain stem cancer(DOID:4203)"
        },
        "DOID:5675": {
            "DOID:5675": "cribriform carcinoma(DOID:5675)"
        },
        "DOID:3070": {
            "DOID:3070": "high grade glioma(DOID:3070)"
        },
        "DOID:3246": {
            "DOID:3246": "embryonal rhabdomyosarcoma(DOID:3246)"
        },
        "DOID:4594": {
            "DOID:4594": "microcystic meningioma(DOID:4594)"
        },
        "DOID:2994": {
            "DOID:2994": "germ cell cancer(DOID:2994)"
        },
        "DOID:12192": {
            "DOID:12192": "sigmoid colon cancer(DOID:12192)"
        },
        "DOID:120": {
            "DOID:120": "female reproductive organ cancer(DOID:120)"
        },
        "DOID:4235": {
            "DOID:4235": "spindle cell sarcoma(DOID:4235)"
        },
        "DOID:0060318": {
            "DOID:0060318": "acute promyelocytic leukemia(DOID:0060318)"
        },
        "DOID:171": {
            "DOID:171": "neuroectodermal tumor(DOID:171)"
        },
        "DOID:672": {
            "DOID:672": "spleen cancer(DOID:672)"
        },
        "DOID:0050902": {
            "DOID:0050902": "medulloblastoma(DOID:0050902)"
        },
        "DOID:11239": {
            "DOID:11239": "appendix cancer(DOID:11239)"
        },
        "DOID:8864": {
            "DOID:8864": "acute monocytic leukemia(DOID:8864)"
        },
        "DOID:4765": {
            "DOID:4765": "pulmonary blastoma(DOID:4765)"
        },
        "DOID:3275": {
            "DOID:3275": "thymoma(DOID:3275)"
        },
        "DOID:5363": {
            "DOID:5363": "myxoid liposarcoma(DOID:5363)"
        },
        "DOID:3078": {
            "DOID:3078": "anaplastic astrocytoma(DOID:3078)"
        },
        "DOID:3069": {
            "DOID:3069": "malignant astrocytoma(DOID:3069)"
        },
        "DOID:4897": {
            "DOID:4897": "bile duct carcinoma(DOID:4897)"
        },
        "DOID:0080909": {
            "DOID:0080909": "castration-resistant prostate carcinoma(DOID:0080909)"
        },
        "DOID:175": {
            "DOID:175": "vascular cancer(DOID:175)"
        },
        "DOID:3478": {
            "DOID:3478": "iris cancer(DOID:3478)"
        },
        "DOID:0050523": {
            "DOID:0050523": "adult T-cell leukemia(DOID:0050523)"
        },
        "DOID:0050745": {
            "DOID:0050745": "diffuse large B-cell lymphoma(DOID:0050745)"
        },
        "DOID:13499": {
            "DOID:13499": "jejunal cancer(DOID:13499)"
        },
        "DOID:4794": {
            "DOID:4794": "ependymoblastoma(DOID:4794)"
        },
        "DOID:299": {
            "DOID:299": "adenocarcinoma(DOID:299)"
        },
        "DOID:4430": {
            "DOID:4430": "somatostatinoma(DOID:4430)"
        },
        "DOID:833": {
            "DOID:833": "auditory system cancer(DOID:833)"
        },
        "DOID:3149": {
            "DOID:3149": "keratoacanthoma(DOID:3149)"
        },
        "DOID:3193": {
            "DOID:3193": "peripheral nerve sheath neoplasm(DOID:3193)"
        },
        "DOID:0001816": {
            "DOID:0001816": "angiosarcoma(DOID:0001816)"
        },
        "DOID:3071": {
            "DOID:3071": "gliosarcoma(DOID:3071)"
        },
        "DOID:4015": {
            "DOID:4015": "sarcomatoid carcinoma(DOID:4015)"
        },
        "DOID:4618": {
            "DOID:4618": "maxillary cancer(DOID:4618)"
        },
        "DOID:3962": {
            "DOID:3962": "thyroid gland follicular carcinoma(DOID:3962)"
        },
        "DOID:11615": {
            "DOID:11615": "penile cancer(DOID:11615)"
        },
        "DOID:3457": {
            "DOID:3457": "invasive lobular carcinoma(DOID:3457)"
        },
        "DOID:5603": {
            "DOID:5603": "T-cell acute lymphoblastic leukemia(DOID:5603)"
        },
        "DOID:8593": {
            "DOID:8593": "chronic monocytic leukemia(DOID:8593)"
        },
        "DOID:8692": {
            "DOID:8692": "myeloid leukemia(DOID:8692)"
        },
        "DOID:5467": {
            "DOID:5467": "conjunctival cancer(DOID:5467)"
        },
        "DOID:5546": {
            "DOID:5546": "femoral cancer(DOID:5546)"
        },
        "DOID:369": {
            "DOID:369": "olfactory neuroblastoma(DOID:369)"
        },
        "DOID:4236": {
            "DOID:4236": "carcinosarcoma(DOID:4236)"
        },
        "DOID:5032": {
            "DOID:5032": "pineal gland cancer(DOID:5032)"
        },
        "DOID:4706": {
            "DOID:4706": "infratentorial cancer(DOID:4706)"
        },
        "DOID:3968": {
            "DOID:3968": "papillary follicular thyroid adenocarcinoma(DOID:3968)"
        },
        "DOID:7398": {
            "DOID:7398": "cerebral primitive neuroectodermal tumor(DOID:7398)"
        },
        "DOID:3307": {
            "DOID:3307": "teratoma(DOID:3307)"
        },
        "DOID:1380": {
            "DOID:1380": "endometrial cancer(DOID:1380)"
        },
        "DOID:5264": {
            "DOID:5264": "epithelioid leiomyosarcoma(DOID:5264)"
        },
        "DOID:5557": {
            "DOID:5557": "testicular germ cell cancer(DOID:5557)"
        },
        "DOID:1240": {
            "DOID:1240": "leukemia(DOID:1240)"
        },
        "DOID:3672": {
            "DOID:3672": "rhabdoid cancer(DOID:3672)"
        },
        "DOID:1138": {
            "DOID:1138": "spinal meningioma(DOID:1138)"
        },
        "DOID:3904": {
            "DOID:3904": "bronchus carcinoma(DOID:3904)"
        },
        "DOID:768": {
            "DOID:768": "retinoblastoma(DOID:768)"
        },
        "DOID:5041": {
            "DOID:5041": "esophageal cancer(DOID:5041)"
        },
        "DOID:2871": {
            "DOID:2871": "endometrial carcinoma(DOID:2871)"
        },
        "DOID:4972": {
            "DOID:4972": "myelodysplastic/myeloproliferative neoplasm(DOID:4972)"
        },
        "DOID:9119": {
            "DOID:9119": "acute myeloid leukemia(DOID:9119)"
        },
        "DOID:9036": {
            "DOID:9036": "parotid gland cancer(DOID:9036)"
        },
        "DOID:5648": {
            "DOID:5648": "choroid plexus carcinoma(DOID:5648)"
        },
        "DOID:0070324": {
            "DOID:0070324": "systemic Epstein-Barr virus-positive T-cell lymphoma of childhood(DOID:0070324)"
        },
        "DOID:0111147": {
            "DOID:0111147": "angioimmunoblastic T-cell lymphoma(DOID:0111147)"
        },
        "DOID:170": {
            "DOID:170": "endocrine gland cancer(DOID:170)"
        },
        "DOID:9513": {
            "DOID:9513": "plasma cell leukemia(DOID:9513)"
        },
        "DOID:3721": {
            "DOID:3721": "plasmacytoma(DOID:3721)"
        },
        "DOID:2174": {
            "DOID:2174": "ocular cancer(DOID:2174)"
        },
        "DOID:3541": {
            "DOID:3541": "cerebral ventricle cancer(DOID:3541)"
        },
        "DOID:10534": {
            "DOID:10534": "stomach cancer(DOID:10534)"
        },
        "DOID:1863": {
            "DOID:1863": "skull cancer(DOID:1863)"
        },
        "DOID:2668": {
            "DOID:2668": "mesenchymoma(DOID:2668)"
        },
        "DOID:5940": {
            "DOID:5940": "malignant peripheral nerve sheath tumor(DOID:5940)"
        },
        "DOID:9986": {
            "DOID:9986": "orbit lymphoma(DOID:9986)"
        },
        "DOID:3098": {
            "DOID:3098": "small cell sarcoma(DOID:3098)"
        },
        "DOID:769": {
            "DOID:769": "neuroblastoma(DOID:769)"
        },
        "DOID:264": {
            "DOID:264": "hemangiopericytoma(DOID:264)"
        },
        "DOID:1907": {
            "DOID:1907": "malignant fibrous histiocytoma(DOID:1907)"
        },
        "DOID:4839": {
            "DOID:4839": "sebaceous adenocarcinoma(DOID:4839)"
        },
        "DOID:3183": {
            "DOID:3183": "childhood oligodendroglioma(DOID:3183)"
        },
        "DOID:338": {
            "DOID:338": "cranial nerve neoplasm(DOID:338)"
        },
        "DOID:6126": {
            "DOID:6126": "anal canal carcinoma(DOID:6126)"
        },
        "DOID:3869": {
            "DOID:3869": "childhood medulloblastoma(DOID:3869)"
        },
        "DOID:4928": {
            "DOID:4928": "intrahepatic cholangiocarcinoma(DOID:4928)"
        },
        "DOID:3074": {
            "DOID:3074": "giant cell glioblastoma(DOID:3074)"
        },
        "DOID:4210": {
            "DOID:4210": "clear cell meningioma(DOID:4210)"
        },
        "DOID:1790": {
            "DOID:1790": "malignant mesothelioma(DOID:1790)"
        },
        "DOID:8057": {
            "DOID:8057": "olfactory groove meningioma(DOID:8057)"
        },
        "DOID:8533": {
            "DOID:8533": "hypopharynx cancer(DOID:8533)"
        },
        "DOID:5867": {
            "DOID:5867": "clear cell chondrosarcoma(DOID:5867)"
        },
        "DOID:2998": {
            "DOID:2998": "testicular cancer(DOID:2998)"
        },
        "DOID:0080199": {
            "DOID:0080199": "colorectal carcinoma(DOID:0080199)"
        },
        "DOID:1614": {
            "DOID:1614": "male breast cancer(DOID:1614)"
        },
        "DOID:3347": {
            "DOID:3347": "osteosarcoma(DOID:3347)"
        },
        "DOID:6335": {
            "DOID:6335": "bilateral meningioma of optic nerve(DOID:6335)"
        },
        "DOID:3304": {
            "DOID:3304": "germinoma(DOID:3304)"
        },
        "DOID:6548": {
            "DOID:6548": "angiomatous meningioma(DOID:6548)"
        },
        "DOID:8649": {
            "DOID:8649": "tongue cancer(DOID:8649)"
        },
        "DOID:9953": {
            "DOID:9953": "mixed phenotype acute leukemia(DOID:9953)"
        },
        "DOID:3856": {
            "DOID:3856": "male reproductive organ cancer(DOID:3856)"
        },
        "DOID:10155": {
            "DOID:10155": "intestinal cancer(DOID:10155)"
        },
        "DOID:2154": {
            "DOID:2154": "nephroblastoma(DOID:2154)"
        },
        "DOID:3590": {
            "DOID:3590": "gestational trophoblastic neoplasm(DOID:3590)"
        },
        "DOID:3772": {
            "DOID:3772": "intraventricular meningioma(DOID:3772)"
        },
        "DOID:9261": {
            "DOID:9261": "nasopharynx carcinoma(DOID:9261)"
        },
        "DOID:4217": {
            "DOID:4217": "malignant ovarian Brenner tumor(DOID:4217)"
        },
        "DOID:4141": {
            "DOID:4141": "intraorbital meningioma(DOID:4141)"
        },
        "DOID:3644": {
            "DOID:3644": "hypothalamic neoplasm(DOID:3644)"
        },
        "DOID:4464": {
            "DOID:4464": "collecting duct carcinoma(DOID:4464)"
        },
        "DOID:2224": {
            "DOID:2224": "essential thrombocythemia(DOID:2224)"
        },
        "DOID:962": {
            "DOID:962": "neurofibroma(DOID:962)"
        },
        "DOID:8541": {
            "DOID:8541": "Sezary's disease(DOID:8541)"
        },
        "DOID:3507": {
            "DOID:3507": "dermatofibrosarcoma protuberans(DOID:3507)"
        },
        "DOID:4645": {
            "DOID:4645": "retinal cancer(DOID:4645)"
        },
        "DOID:6823": {
            "DOID:6823": "pancreatoblastoma(DOID:6823)"
        },
        "DOID:0050746": {
            "DOID:0050746": "mantle cell lymphoma(DOID:0050746)"
        },
        "DOID:201": {
            "DOID:201": "connective tissue cancer(DOID:201)"
        },
        "DOID:3371": {
            "DOID:3371": "chondrosarcoma(DOID:3371)"
        },
        "DOID:5101": {
            "DOID:5101": "ear cancer(DOID:5101)"
        },
        "DOID:3007": {
            "DOID:3007": "breast ductal carcinoma(DOID:3007)"
        },
        "DOID:285": {
            "DOID:285": "hairy cell leukemia(DOID:285)"
        },
        "DOID:1540": {
            "DOID:1540": "parathyroid carcinoma(DOID:1540)"
        },
        "DOID:5015": {
            "DOID:5015": "fibrolamellar carcinoma(DOID:5015)"
        },
        "DOID:3259": {
            "DOID:3259": "orbit rhabdomyosarcoma(DOID:3259)"
        },
        "DOID:3110": {
            "DOID:3110": "papillary cystadenocarcinoma(DOID:3110)"
        },
        "DOID:1911": {
            "DOID:1911": "endodermal sinus tumor(DOID:1911)"
        },
        "DOID:3111": {
            "DOID:3111": "cystadenocarcinoma(DOID:3111)"
        },
        "DOID:3419": {
            "DOID:3419": "optic nerve neoplasm(DOID:3419)"
        },
        "DOID:7212": {
            "DOID:7212": "meningothelial meningioma(DOID:7212)"
        },
        "DOID:3908": {
            "DOID:3908": "lung non-small cell carcinoma(DOID:3908)"
        },
        "DOID:0060061": {
            "DOID:0060061": "cutaneous T cell lymphoma(DOID:0060061)"
        },
        "DOID:5151": {
            "DOID:5151": "plexiform neurofibroma(DOID:5151)"
        },
        "DOID:3559": {
            "DOID:3559": "pseudomyxoma peritonei(DOID:3559)"
        },
        "DOID:1612": {
            "DOID:1612": "breast cancer(DOID:1612)"
        },
        "DOID:7007": {
            "DOID:7007": "childhood cerebral astrocytoma(DOID:7007)"
        },
        "DOID:4903": {
            "DOID:4903": "granular cell carcinoma(DOID:4903)"
        },
        "DOID:1039": {
            "DOID:1039": "prolymphocytic leukemia(DOID:1039)"
        },
        "DOID:707": {
            "DOID:707": "B-cell lymphoma(DOID:707)"
        },
        "DOID:3355": {
            "DOID:3355": "fibrosarcoma(DOID:3355)"
        },
        "DOID:6869": {
            "DOID:6869": "parasagittal meningioma(DOID:6869)"
        },
        "DOID:775": {
            "DOID:775": "intraocular lymphoma(DOID:775)"
        },
        "DOID:9253": {
            "DOID:9253": "gastrointestinal stromal tumor(DOID:9253)"
        },
        "DOID:10283": {
            "DOID:10283": "prostate cancer(DOID:10283)"
        },
        "DOID:0050873": {
            "DOID:0050873": "follicular lymphoma(DOID:0050873)"
        },
        "DOID:11934": {
            "DOID:11934": "head and neck cancer(DOID:11934)"
        },
        "DOID:3008": {
            "DOID:3008": "invasive ductal carcinoma(DOID:3008)"
        },
        "DOID:3910": {
            "DOID:3910": "lung adenocarcinoma(DOID:3910)"
        },
        "DOID:8923": {
            "DOID:8923": "skin melanoma(DOID:8923)"
        },
        "DOID:1963": {
            "DOID:1963": "fallopian tube carcinoma(DOID:1963)"
        },
        "DOID:3577": {
            "DOID:3577": "Sertoli cell tumor(DOID:3577)"
        },
        "DOID:5520": {
            "DOID:5520": "head and neck squamous cell carcinoma(DOID:5520)"
        },
        "DOID:1964": {
            "DOID:1964": "fallopian tube cancer(DOID:1964)"
        },
        "DOID:4769": {
            "DOID:4769": "pleuropulmonary blastoma(DOID:4769)"
        },
        "DOID:5758": {
            "DOID:5758": "malignant mesenchymoma(DOID:5758)"
        },
        "DOID:8567": {
            "DOID:8567": "Hodgkin's lymphoma(DOID:8567)"
        },
        "DOID:0080915": {
            "DOID:0080915": "histiocytic sarcoma(DOID:0080915)"
        },
        "DOID:3479": {
            "DOID:3479": "uveal cancer(DOID:3479)"
        },
        "DOID:4648": {
            "DOID:4648": "familial retinoblastoma(DOID:4648)"
        },
        "DOID:4163": {
            "DOID:4163": "ganglioneuroblastoma(DOID:4163)"
        },
        "DOID:4552": {
            "DOID:4552": "large cell carcinoma(DOID:4552)"
        },
        "DOID:0060901": {
            "DOID:0060901": "Waldenstroem's macroglobulinemia(DOID:0060901)"
        },
        "DOID:0050458": {
            "DOID:0050458": "juvenile myelomonocytic leukemia(DOID:0050458)"
        },
        "DOID:5166": {
            "DOID:5166": "endometrial stromal tumor(DOID:5166)"
        },
        "DOID:6576": {
            "DOID:6576": "childhood optic nerve glioma(DOID:6576)"
        },
        "DOID:2640": {
            "DOID:2640": "struma ovarii(DOID:2640)"
        },
        "DOID:8543": {
            "DOID:8543": "Hodgkin's lymphoma, lymphocytic-histiocytic predominance(DOID:8543)"
        },
        "DOID:1909": {
            "DOID:1909": "melanoma(DOID:1909)"
        },
        "DOID:3247": {
            "DOID:3247": "rhabdomyosarcoma(DOID:3247)"
        },
        "DOID:3450": {
            "DOID:3450": "cutaneous Paget's disease(DOID:3450)"
        },
        "DOID:169": {
            "DOID:169": "neuroendocrine tumor(DOID:169)"
        },
        "DOID:3587": {
            "DOID:3587": "pancreatic ductal carcinoma(DOID:3587)"
        },
        "DOID:11054": {
            "DOID:11054": "urinary bladder cancer(DOID:11054)"
        },
        "DOID:3953": {
            "DOID:3953": "adrenal gland cancer(DOID:3953)"
        },
        "DOID:6263": {
            "DOID:6263": "inflammatory breast carcinoma(DOID:6263)"
        },
        "DOID:4045": {
            "DOID:4045": "muscle cancer(DOID:4045)"
        },
        "DOID:1798": {
            "DOID:1798": "pancreatic endocrine carcinoma(DOID:1798)"
        },
        "DOID:14174": {
            "DOID:14174": "central neurocytoma(DOID:14174)"
        },
        "DOID:6726": {
            "DOID:6726": "fibrillary astrocytoma(DOID:6726)"
        },
        "DOID:715": {
            "DOID:715": "T-cell lymphoblastic leukemia/lymphoma(DOID:715)"
        },
        "DOID:2531": {
            "DOID:2531": "hematologic cancer(DOID:2531)"
        },
        "DOID:4465": {
            "DOID:4465": "papillary renal cell carcinoma(DOID:4465)"
        },
        "DOID:3095": {
            "DOID:3095": "germ cell and embryonal cancer(DOID:3095)"
        },
        "DOID:3963": {
            "DOID:3963": "thyroid gland carcinoma(DOID:3963)"
        },
        "DOID:6536": {
            "DOID:6536": "plasma cell neoplasm(DOID:6536)"
        },
        "DOID:5515": {
            "DOID:5515": "nasal cavity squamous cell carcinoma(DOID:5515)"
        },
        "DOID:3603": {
            "DOID:3603": "mucinous cystadenocarcinoma(DOID:3603)"
        },
        "DOID:4440": {
            "DOID:4440": "seminoma(DOID:4440)"
        },
        "DOID:5583": {
            "DOID:5583": "lung giant cell carcinoma(DOID:5583)"
        },
        "DOID:3373": {
            "DOID:3373": "parosteal osteosarcoma(DOID:3373)"
        },
        "DOID:5612": {
            "DOID:5612": "spinal cancer(DOID:5612)"
        },
        "DOID:4866": {
            "DOID:4866": "salivary gland adenoid cystic carcinoma(DOID:4866)"
        },
        "DOID:3181": {
            "DOID:3181": "oligodendroglioma(DOID:3181)"
        },
        "DOID:2513": {
            "DOID:2513": "basal cell carcinoma(DOID:2513)"
        },
        "DOID:8564": {
            "DOID:8564": "lip cancer(DOID:8564)"
        },
        "DOID:8584": {
            "DOID:8584": "Burkitt lymphoma(DOID:8584)"
        },
        "DOID:3737": {
            "DOID:3737": "verrucous carcinoma(DOID:3737)"
        },
        "DOID:5050": {
            "DOID:5050": "Ehrlich tumor carcinoma(DOID:5050)"
        },
        "DOID:1040": {
            "DOID:1040": "chronic lymphocytic leukemia(DOID:1040)"
        },
        "DOID:0060060": {
            "DOID:0060060": "non-Hodgkin lymphoma(DOID:0060060)"
        },
        "DOID:5577": {
            "DOID:5577": "gastrinoma(DOID:5577)"
        },
        "DOID:2696": {
            "DOID:2696": "Leydig cell tumor(DOID:2696)"
        },
        "DOID:5842": {
            "DOID:5842": "testis seminoma(DOID:5842)"
        },
        "DOID:3114": {
            "DOID:3114": "serous cystadenocarcinoma(DOID:3114)"
        },
        "DOID:7474": {
            "DOID:7474": "malignant pleural mesothelioma(DOID:7474)"
        },
        "DOID:11819": {
            "DOID:11819": "ureter cancer(DOID:11819)"
        },
        "DOID:0050686": {
            "DOID:0050686": "organ system cancer(DOID:0050686)"
        },
        "DOID:1967": {
            "DOID:1967": "leiomyosarcoma(DOID:1967)"
        },
        "DOID:184": {
            "DOID:184": "bone cancer(DOID:184)"
        },
        "DOID:9538": {
            "DOID:9538": "multiple myeloma(DOID:9538)"
        },
        "DOID:3093": {
            "DOID:3093": "nervous system cancer(DOID:3093)"
        },
        "DOID:7514": {
            "DOID:7514": "Wolffian adnexal neoplasm(DOID:7514)"
        },
        "DOID:3618": {
            "DOID:3618": "epidural spinal canal neoplasm(DOID:3618)"
        },
        "DOID:5158": {
            "DOID:5158": "pleural cancer(DOID:5158)"
        },
        "DOID:3969": {
            "DOID:3969": "thyroid gland papillary carcinoma(DOID:3969)"
        },
        "DOID:6039": {
            "DOID:6039": "uveal melanoma(DOID:6039)"
        },
        "DOID:4467": {
            "DOID:4467": "clear cell renal cell carcinoma(DOID:4467)"
        },
        "DOID:2643": {
            "DOID:2643": "perivascular epithelioid cell tumor(DOID:2643)"
        },
        "DOID:1781": {
            "DOID:1781": "thyroid gland cancer(DOID:1781)"
        },
        "DOID:5563": {
            "DOID:5563": "malignant teratoma(DOID:5563)"
        },
        "DOID:1974": {
            "DOID:1974": "adenosarcoma(DOID:1974)"
        },
        "DOID:5702": {
            "DOID:5702": "pleomorphic liposarcoma(DOID:5702)"
        },
        "DOID:3571": {
            "DOID:3571": "liver cancer(DOID:3571)"
        },
        "DOID:4024": {
            "DOID:4024": "scirrhous adenocarcinoma(DOID:4024)"
        },
        "DOID:1037": {
            "DOID:1037": "lymphoid leukemia(DOID:1037)"
        },
        "DOID:4233": {
            "DOID:4233": "clear cell sarcoma(DOID:4233)"
        },
        "DOID:1245": {
            "DOID:1245": "vulva cancer(DOID:1245)"
        },
        "DOID:8632": {
            "DOID:8632": "Kaposi's sarcoma(DOID:8632)"
        },
        "DOID:2338": {
            "DOID:2338": "mandibular cancer(DOID:2338)"
        },
        "DOID:4830": {
            "DOID:4830": "adenosquamous carcinoma(DOID:4830)"
        },
        "DOID:4545": {
            "DOID:4545": "mesenchymal chondrosarcoma(DOID:4545)"
        },
        "DOID:3868": {
            "DOID:3868": "melanotic medulloblastoma(DOID:3868)"
        },
        "DOID:7210": {
            "DOID:7210": "psammomatous meningioma(DOID:7210)"
        }
    },
    "tree": {
        "Head And Neck Regions": {
            "id": "Head And Neck Regions",
            "name": "Head And Neck Regions",
            "children": [{
                    "id": "Brain",
                    "name": "Brain",
                    "children": [{
                            "id": "DOID:6128",
                            "name": "gliomatosis cerebri(DOID:6128)"
                        }, {
                            "id": "DOID:3864",
                            "name": "adult medulloblastoma(DOID:3864)"
                        }, {
                            "id": "DOID:7213",
                            "name": "transitional meningioma(DOID:7213)"
                        }, {
                            "id": "DOID:1659",
                            "name": "supratentorial cancer(DOID:1659)"
                        }, {
                            "id": "DOID:7912",
                            "name": "mixed oligodendroglioma-astrocytoma(DOID:7912)"
                        }, {
                            "id": "DOID:4790",
                            "name": "medulloepithelioma(DOID:4790)"
                        }, {
                            "id": "DOID:4916",
                            "name": "pituitary carcinoma(DOID:4916)"
                        }, {
                            "id": "DOID:3861",
                            "name": "medullomyoblastoma(DOID:3861)"
                        }, {
                            "id": "DOID:4205",
                            "name": "cerebellum cancer(DOID:4205)"
                        }, {
                            "id": "DOID:1664",
                            "name": "pineoblastoma(DOID:1664)"
                        }, {
                            "id": "DOID:3068",
                            "name": "glioblastoma(DOID:3068)"
                        }, {
                            "id": "DOID:5076",
                            "name": "mixed glioma(DOID:5076)"
                        }, {
                            "id": "DOID:0080842",
                            "name": "intracranial meningioma(DOID:0080842)"
                        }, {
                            "id": "DOID:3565",
                            "name": "meningioma(DOID:3565)"
                        }, {
                            "id": "DOID:3186",
                            "name": "adult oligodendroglioma(DOID:3186)"
                        }, {
                            "id": "DOID:7008",
                            "name": "protoplasmic astrocytoma(DOID:7008)"
                        }, {
                            "id": "DOID:1319",
                            "name": "brain cancer(DOID:1319)"
                        }, {
                            "id": "DOID:7305",
                            "name": "astroblastoma(DOID:7305)"
                        }, {
                            "id": "DOID:7005",
                            "name": "gemistocytic astrocytoma(DOID:7005)"
                        }, {
                            "id": "DOID:4588",
                            "name": "secretory meningioma(DOID:4588)"
                        }, {
                            "id": "DOID:2815",
                            "name": "cranial nerve malignant neoplasm(DOID:2815)"
                        }, {
                            "id": "DOID:4586",
                            "name": "familial meningioma(DOID:4586)"
                        }, {
                            "id": "DOID:1785",
                            "name": "pituitary cancer(DOID:1785)"
                        }, {
                            "id": "DOID:3540",
                            "name": "choroid plexus cancer(DOID:3540)"
                        }, {
                            "id": "DOID:3842",
                            "name": "skull base cancer(DOID:3842)"
                        }, {
                            "id": "DOID:6114",
                            "name": "cerebral convexity meningioma(DOID:6114)"
                        }, {
                            "id": "DOID:4992",
                            "name": "optic nerve glioma(DOID:4992)"
                        }, {
                            "id": "DOID:3620",
                            "name": "central nervous system cancer(DOID:3620)"
                        }, {
                            "id": "DOID:7211",
                            "name": "fibrous meningioma(DOID:7211)"
                        }, {
                            "id": "DOID:4203",
                            "name": "brain stem cancer(DOID:4203)"
                        }, {
                            "id": "DOID:3070",
                            "name": "high grade glioma(DOID:3070)"
                        }, {
                            "id": "DOID:4594",
                            "name": "microcystic meningioma(DOID:4594)"
                        }, {
                            "id": "DOID:171",
                            "name": "neuroectodermal tumor(DOID:171)"
                        }, {
                            "id": "DOID:0050902",
                            "name": "medulloblastoma(DOID:0050902)"
                        }, {
                            "id": "DOID:3078",
                            "name": "anaplastic astrocytoma(DOID:3078)"
                        }, {
                            "id": "DOID:3069",
                            "name": "malignant astrocytoma(DOID:3069)"
                        }, {
                            "id": "DOID:4794",
                            "name": "ependymoblastoma(DOID:4794)"
                        }, {
                            "id": "DOID:3071",
                            "name": "gliosarcoma(DOID:3071)"
                        }, {
                            "id": "DOID:5032",
                            "name": "pineal gland cancer(DOID:5032)"
                        }, {
                            "id": "DOID:4706",
                            "name": "infratentorial cancer(DOID:4706)"
                        }, {
                            "id": "DOID:7398",
                            "name": "cerebral primitive neuroectodermal tumor(DOID:7398)"
                        }, {
                            "id": "DOID:1138",
                            "name": "spinal meningioma(DOID:1138)"
                        }, {
                            "id": "DOID:5648",
                            "name": "choroid plexus carcinoma(DOID:5648)"
                        }, {
                            "id": "DOID:3541",
                            "name": "cerebral ventricle cancer(DOID:3541)"
                        }, {
                            "id": "DOID:3183",
                            "name": "childhood oligodendroglioma(DOID:3183)"
                        }, {
                            "id": "DOID:338",
                            "name": "cranial nerve neoplasm(DOID:338)"
                        }, {
                            "id": "DOID:3869",
                            "name": "childhood medulloblastoma(DOID:3869)"
                        }, {
                            "id": "DOID:3074",
                            "name": "giant cell glioblastoma(DOID:3074)"
                        }, {
                            "id": "DOID:4210",
                            "name": "clear cell meningioma(DOID:4210)"
                        }, {
                            "id": "DOID:8057",
                            "name": "olfactory groove meningioma(DOID:8057)"
                        }, {
                            "id": "DOID:6335",
                            "name": "bilateral meningioma of optic nerve(DOID:6335)"
                        }, {
                            "id": "DOID:3304",
                            "name": "germinoma(DOID:3304)"
                        }, {
                            "id": "DOID:6548",
                            "name": "angiomatous meningioma(DOID:6548)"
                        }, {
                            "id": "DOID:3772",
                            "name": "intraventricular meningioma(DOID:3772)"
                        }, {
                            "id": "DOID:4141",
                            "name": "intraorbital meningioma(DOID:4141)"
                        }, {
                            "id": "DOID:3644",
                            "name": "hypothalamic neoplasm(DOID:3644)"
                        }, {
                            "id": "DOID:7212",
                            "name": "meningothelial meningioma(DOID:7212)"
                        }, {
                            "id": "DOID:7007",
                            "name": "childhood cerebral astrocytoma(DOID:7007)"
                        }, {
                            "id": "DOID:6869",
                            "name": "parasagittal meningioma(DOID:6869)"
                        }, {
                            "id": "DOID:14174",
                            "name": "central neurocytoma(DOID:14174)"
                        }, {
                            "id": "DOID:6726",
                            "name": "fibrillary astrocytoma(DOID:6726)"
                        }, {
                            "id": "DOID:3181",
                            "name": "oligodendroglioma(DOID:3181)"
                        }, {
                            "id": "DOID:4024",
                            "name": "scirrhous adenocarcinoma(DOID:4024)"
                        }, {
                            "id": "DOID:3868",
                            "name": "melanotic medulloblastoma(DOID:3868)"
                        }, {
                            "id": "DOID:7210",
                            "name": "psammomatous meningioma(DOID:7210)"
                        }
                    ]
                }, {
                    "id": "Other Head And Neck Region",
                    "name": "Other Head And Neck Region",
                    "children": [{
                            "id": "DOID:8858",
                            "name": "tonsil cancer(DOID:8858)"
                        }
                    ]
                }, {
                    "id": "Eye",
                    "name": "Eye",
                    "children": [{
                            "id": "DOID:12759",
                            "name": "choroid cancer(DOID:12759)"
                        }, {
                            "id": "DOID:3478",
                            "name": "iris cancer(DOID:3478)"
                        }, {
                            "id": "DOID:5467",
                            "name": "conjunctival cancer(DOID:5467)"
                        }, {
                            "id": "DOID:768",
                            "name": "retinoblastoma(DOID:768)"
                        }, {
                            "id": "DOID:2174",
                            "name": "ocular cancer(DOID:2174)"
                        }, {
                            "id": "DOID:4645",
                            "name": "retinal cancer(DOID:4645)"
                        }, {
                            "id": "DOID:3259",
                            "name": "orbit rhabdomyosarcoma(DOID:3259)"
                        }, {
                            "id": "DOID:3419",
                            "name": "optic nerve neoplasm(DOID:3419)"
                        }, {
                            "id": "DOID:3479",
                            "name": "uveal cancer(DOID:3479)"
                        }, {
                            "id": "DOID:4648",
                            "name": "familial retinoblastoma(DOID:4648)"
                        }, {
                            "id": "DOID:6576",
                            "name": "childhood optic nerve glioma(DOID:6576)"
                        }
                    ]
                }, {
                    "id": "Larynx",
                    "name": "Larynx",
                    "children": [{
                            "id": "DOID:2596",
                            "name": "larynx cancer(DOID:2596)"
                        }, {
                            "id": "DOID:2876",
                            "name": "laryngeal squamous cell carcinoma(DOID:2876)"
                        }
                    ]
                }, {
                    "id": "Paranasal Sinuses",
                    "name": "Paranasal Sinuses",
                    "children": [{
                            "id": "DOID:0050619",
                            "name": "paranasal sinus cancer(DOID:0050619)"
                        }
                    ]
                }, {
                    "id": "Ear",
                    "name": "Ear",
                    "children": [{
                            "id": "DOID:833",
                            "name": "auditory system cancer(DOID:833)"
                        }, {
                            "id": "DOID:5101",
                            "name": "ear cancer(DOID:5101)"
                        }
                    ]
                }, {
                    "id": "Nose",
                    "name": "Nose",
                    "children": [{
                            "id": "DOID:369",
                            "name": "olfactory neuroblastoma(DOID:369)"
                        }
                    ]
                }, {
                    "id": "Throat",
                    "name": "Throat",
                    "children": [{
                            "id": "DOID:8533",
                            "name": "hypopharynx cancer(DOID:8533)"
                        }
                    ]
                }, {
                    "id": "Oral Cavity",
                    "name": "Oral Cavity",
                    "children": [{
                            "id": "DOID:8649",
                            "name": "tongue cancer(DOID:8649)"
                        }, {
                            "id": "DOID:3110",
                            "name": "papillary cystadenocarcinoma(DOID:3110)"
                        }, {
                            "id": "DOID:4866",
                            "name": "salivary gland adenoid cystic carcinoma(DOID:4866)"
                        }, {
                            "id": "DOID:8564",
                            "name": "lip cancer(DOID:8564)"
                        }
                    ]
                }, {
                    "id": "Other",
                    "name": "Other",
                    "children": [{
                            "id": "DOID:3507",
                            "name": "dermatofibrosarcoma protuberans(DOID:3507)"
                        }, {
                            "id": "DOID:11934",
                            "name": "head and neck cancer(DOID:11934)"
                        }, {
                            "id": "DOID:5520",
                            "name": "head and neck squamous cell carcinoma(DOID:5520)"
                        }
                    ]
                }, {
                    "id": "Nasal",
                    "name": "Nasal",
                    "children": [{
                            "id": "DOID:5515",
                            "name": "nasal cavity squamous cell carcinoma(DOID:5515)"
                        }
                    ]
                }
            ]
        },
        "Gland": {
            "id": "Gland",
            "name": "Gland",
            "children": [{
                    "id": "Breast",
                    "name": "Breast",
                    "children": [{
                            "id": "DOID:3016",
                            "name": "breast malignant phyllodes tumor(DOID:3016)"
                        }, {
                            "id": "DOID:3113",
                            "name": "papillary carcinoma(DOID:3113)"
                        }, {
                            "id": "DOID:4922",
                            "name": "breast secretory carcinoma(DOID:4922)"
                        }, {
                            "id": "DOID:4511",
                            "name": "breast angiosarcoma(DOID:4511)"
                        }, {
                            "id": "DOID:3459",
                            "name": "breast carcinoma(DOID:3459)"
                        }, {
                            "id": "DOID:5675",
                            "name": "cribriform carcinoma(DOID:5675)"
                        }, {
                            "id": "DOID:3457",
                            "name": "invasive lobular carcinoma(DOID:3457)"
                        }, {
                            "id": "DOID:1614",
                            "name": "male breast cancer(DOID:1614)"
                        }, {
                            "id": "DOID:3007",
                            "name": "breast ductal carcinoma(DOID:3007)"
                        }, {
                            "id": "DOID:1612",
                            "name": "breast cancer(DOID:1612)"
                        }, {
                            "id": "DOID:3008",
                            "name": "invasive ductal carcinoma(DOID:3008)"
                        }, {
                            "id": "DOID:6263",
                            "name": "inflammatory breast carcinoma(DOID:6263)"
                        }, {
                            "id": "DOID:5050",
                            "name": "Ehrlich tumor carcinoma(DOID:5050)"
                        }
                    ]
                }, {
                    "id": "Other Gland",
                    "name": "Other Gland",
                    "children": [{
                            "id": "DOID:3277",
                            "name": "thymus cancer(DOID:3277)"
                        }, {
                            "id": "DOID:0080202",
                            "name": "adenoid cystic carcinoma(DOID:0080202)"
                        }, {
                            "id": "DOID:1800",
                            "name": "neuroendocrine carcinoma(DOID:1800)"
                        }, {
                            "id": "DOID:299",
                            "name": "adenocarcinoma(DOID:299)"
                        }, {
                            "id": "DOID:4430",
                            "name": "somatostatinoma(DOID:4430)"
                        }, {
                            "id": "DOID:3111",
                            "name": "cystadenocarcinoma(DOID:3111)"
                        }, {
                            "id": "DOID:3603",
                            "name": "mucinous cystadenocarcinoma(DOID:3603)"
                        }
                    ]
                }, {
                    "id": "Salivary Glands",
                    "name": "Salivary Glands",
                    "children": [{
                            "id": "DOID:3025",
                            "name": "acinar cell carcinoma(DOID:3025)"
                        }, {
                            "id": "DOID:4531",
                            "name": "mucoepidermoid carcinoma(DOID:4531)"
                        }, {
                            "id": "DOID:9036",
                            "name": "parotid gland cancer(DOID:9036)"
                        }
                    ]
                }, {
                    "id": "Thyroid",
                    "name": "Thyroid",
                    "children": [{
                            "id": "DOID:3973",
                            "name": "thyroid gland medullary carcinoma(DOID:3973)"
                        }, {
                            "id": "DOID:8161",
                            "name": "thyroid gland Hurthle cell carcinoma(DOID:8161)"
                        }, {
                            "id": "DOID:3962",
                            "name": "thyroid gland follicular carcinoma(DOID:3962)"
                        }, {
                            "id": "DOID:3968",
                            "name": "papillary follicular thyroid adenocarcinoma(DOID:3968)"
                        }, {
                            "id": "DOID:1540",
                            "name": "parathyroid carcinoma(DOID:1540)"
                        }, {
                            "id": "DOID:3963",
                            "name": "thyroid gland carcinoma(DOID:3963)"
                        }, {
                            "id": "DOID:3969",
                            "name": "thyroid gland papillary carcinoma(DOID:3969)"
                        }
                    ]
                }, {
                    "id": "Thymus",
                    "name": "Thymus",
                    "children": [{
                            "id": "DOID:3284",
                            "name": "thymic carcinoma(DOID:3284)"
                        }, {
                            "id": "DOID:3275",
                            "name": "thymoma(DOID:3275)"
                        }
                    ]
                }, {
                    "id": "Adrenal Glands",
                    "name": "Adrenal Glands",
                    "children": [{
                            "id": "DOID:660",
                            "name": "adrenal cortex cancer(DOID:660)"
                        }, {
                            "id": "DOID:3948",
                            "name": "adrenocortical carcinoma(DOID:3948)"
                        }, {
                            "id": "DOID:3953",
                            "name": "adrenal gland cancer(DOID:3953)"
                        }
                    ]
                }, {
                    "id": "Endocrine Glands",
                    "name": "Endocrine Glands",
                    "children": [{
                            "id": "DOID:170",
                            "name": "endocrine gland cancer(DOID:170)"
                        }, {
                            "id": "DOID:169",
                            "name": "neuroendocrine tumor(DOID:169)"
                        }, {
                            "id": "DOID:5577",
                            "name": "gastrinoma(DOID:5577)"
                        }, {
                            "id": "DOID:1781",
                            "name": "thyroid gland cancer(DOID:1781)"
                        }
                    ]
                }
            ]
        },
        "Reproductive Organs": {
            "id": "Reproductive Organs",
            "name": "Reproductive Organs",
            "children": [{
                    "id": "Other Reproductive Organ",
                    "name": "Other Reproductive Organ",
                    "children": [{
                            "id": "DOID:3308",
                            "name": "embryonal carcinoma(DOID:3308)"
                        }, {
                            "id": "DOID:192",
                            "name": "sex cord-gonadal stromal tumor(DOID:192)"
                        }, {
                            "id": "DOID:2997",
                            "name": "Sertoli-Leydig cell tumor(DOID:2997)"
                        }, {
                            "id": "DOID:4468",
                            "name": "clear cell adenocarcinoma(DOID:4468)"
                        }, {
                            "id": "DOID:120",
                            "name": "female reproductive organ cancer(DOID:120)"
                        }, {
                            "id": "DOID:3856",
                            "name": "male reproductive organ cancer(DOID:3856)"
                        }
                    ]
                }, {
                    "id": "Uterus",
                    "name": "Uterus",
                    "children": [{
                            "id": "DOID:4362",
                            "name": "cervical cancer(DOID:4362)"
                        }, {
                            "id": "DOID:4085",
                            "name": "trophoblastic neoplasm(DOID:4085)"
                        }, {
                            "id": "DOID:3596",
                            "name": "placental site trophoblastic tumor(DOID:3596)"
                        }, {
                            "id": "DOID:4226",
                            "name": "endometrial stromal sarcoma(DOID:4226)"
                        }, {
                            "id": "DOID:363",
                            "name": "uterine cancer(DOID:363)"
                        }, {
                            "id": "DOID:1380",
                            "name": "endometrial cancer(DOID:1380)"
                        }, {
                            "id": "DOID:2871",
                            "name": "endometrial carcinoma(DOID:2871)"
                        }, {
                            "id": "DOID:3590",
                            "name": "gestational trophoblastic neoplasm(DOID:3590)"
                        }, {
                            "id": "DOID:5166",
                            "name": "endometrial stromal tumor(DOID:5166)"
                        }, {
                            "id": "DOID:11819",
                            "name": "ureter cancer(DOID:11819)"
                        }, {
                            "id": "DOID:7514",
                            "name": "Wolffian adnexal neoplasm(DOID:7514)"
                        }
                    ]
                }, {
                    "id": "Ovary",
                    "name": "Ovary",
                    "children": [{
                            "id": "DOID:4441",
                            "name": "dysgerminoma(DOID:4441)"
                        }, {
                            "id": "DOID:4320",
                            "name": "non-gestational choriocarcinoma(DOID:4320)"
                        }, {
                            "id": "DOID:3305",
                            "name": "teratocarcinoma(DOID:3305)"
                        }, {
                            "id": "DOID:2155",
                            "name": "malignant ovarian germ cell neoplasm(DOID:2155)"
                        }, {
                            "id": "DOID:9597",
                            "name": "Krukenberg carcinoma(DOID:9597)"
                        }, {
                            "id": "DOID:2394",
                            "name": "ovarian cancer(DOID:2394)"
                        }, {
                            "id": "DOID:3307",
                            "name": "teratoma(DOID:3307)"
                        }, {
                            "id": "DOID:4217",
                            "name": "malignant ovarian Brenner tumor(DOID:4217)"
                        }, {
                            "id": "DOID:3577",
                            "name": "Sertoli cell tumor(DOID:3577)"
                        }, {
                            "id": "DOID:2640",
                            "name": "struma ovarii(DOID:2640)"
                        }, {
                            "id": "DOID:2696",
                            "name": "Leydig cell tumor(DOID:2696)"
                        }, {
                            "id": "DOID:3114",
                            "name": "serous cystadenocarcinoma(DOID:3114)"
                        }
                    ]
                }, {
                    "id": "Vagina",
                    "name": "Vagina",
                    "children": [{
                            "id": "DOID:119",
                            "name": "vaginal cancer(DOID:119)"
                        }
                    ]
                }, {
                    "id": "Prostate",
                    "name": "Prostate",
                    "children": [{
                            "id": "DOID:10289",
                            "name": "prostate malignant phyllodes tumor(DOID:10289)"
                        }, {
                            "id": "DOID:0080909",
                            "name": "castration-resistant prostate carcinoma(DOID:0080909)"
                        }, {
                            "id": "DOID:10283",
                            "name": "prostate cancer(DOID:10283)"
                        }
                    ]
                }, {
                    "id": "Penile",
                    "name": "Penile",
                    "children": [{
                            "id": "DOID:11615",
                            "name": "penile cancer(DOID:11615)"
                        }
                    ]
                }, {
                    "id": "Testis",
                    "name": "Testis",
                    "children": [{
                            "id": "DOID:5557",
                            "name": "testicular germ cell cancer(DOID:5557)"
                        }, {
                            "id": "DOID:2998",
                            "name": "testicular cancer(DOID:2998)"
                        }, {
                            "id": "DOID:5842",
                            "name": "testis seminoma(DOID:5842)"
                        }
                    ]
                }, {
                    "id": "Yolk Sac",
                    "name": "Yolk Sac",
                    "children": [{
                            "id": "DOID:1911",
                            "name": "endodermal sinus tumor(DOID:1911)"
                        }
                    ]
                }, {
                    "id": "Fallopian Tube",
                    "name": "Fallopian Tube",
                    "children": [{
                            "id": "DOID:1963",
                            "name": "fallopian tube carcinoma(DOID:1963)"
                        }, {
                            "id": "DOID:1964",
                            "name": "fallopian tube cancer(DOID:1964)"
                        }
                    ]
                }, {
                    "id": "Vulva",
                    "name": "Vulva",
                    "children": [{
                            "id": "DOID:1245",
                            "name": "vulva cancer(DOID:1245)"
                        }
                    ]
                }
            ]
        },
        "Blood": {
            "id": "Blood",
            "name": "Blood",
            "children": [{
                    "id": "Blood",
                    "name": "Blood",
                    "children": [{
                            "id": "DOID:8691",
                            "name": "mycosis fungoides(DOID:8691)"
                        }, {
                            "id": "DOID:4971",
                            "name": "myelofibrosis(DOID:4971)"
                        }, {
                            "id": "DOID:5820",
                            "name": "composite lymphoma(DOID:5820)"
                        }, {
                            "id": "DOID:0060058",
                            "name": "lymphoma(DOID:0060058)"
                        }, {
                            "id": "DOID:8683",
                            "name": "myeloid sarcoma(DOID:8683)"
                        }, {
                            "id": "DOID:8628",
                            "name": "Hodgkin's lymphoma, lymphocytic depletion(DOID:8628)"
                        }, {
                            "id": "DOID:4960",
                            "name": "bone marrow cancer(DOID:4960)"
                        }, {
                            "id": "DOID:8997",
                            "name": "polycythemia vera(DOID:8997)"
                        }, {
                            "id": "DOID:8761",
                            "name": "acute megakaryocytic leukemia(DOID:8761)"
                        }, {
                            "id": "DOID:4659",
                            "name": "extracutaneous mastocytoma(DOID:4659)"
                        }, {
                            "id": "DOID:8654",
                            "name": "Hodgkin's lymphoma, mixed cellularity(DOID:8654)"
                        }, {
                            "id": "DOID:9952",
                            "name": "acute lymphoblastic leukemia(DOID:9952)"
                        }, {
                            "id": "DOID:9254",
                            "name": "mast-cell leukemia(DOID:9254)"
                        }, {
                            "id": "DOID:0060597",
                            "name": "atypical chronic myeloid leukemia(DOID:0060597)"
                        }, {
                            "id": "DOID:355",
                            "name": "mast-cell sarcoma(DOID:355)"
                        }, {
                            "id": "DOID:7848",
                            "name": "interdigitating dendritic cell sarcoma(DOID:7848)"
                        }, {
                            "id": "DOID:2689",
                            "name": "lymphangiosarcoma(DOID:2689)"
                        }, {
                            "id": "DOID:0050908",
                            "name": "myelodysplastic syndrome(DOID:0050908)"
                        }, {
                            "id": "DOID:0060318",
                            "name": "acute promyelocytic leukemia(DOID:0060318)"
                        }, {
                            "id": "DOID:8864",
                            "name": "acute monocytic leukemia(DOID:8864)"
                        }, {
                            "id": "DOID:0050523",
                            "name": "adult T-cell leukemia(DOID:0050523)"
                        }, {
                            "id": "DOID:0050745",
                            "name": "diffuse large B-cell lymphoma(DOID:0050745)"
                        }, {
                            "id": "DOID:5603",
                            "name": "T-cell acute lymphoblastic leukemia(DOID:5603)"
                        }, {
                            "id": "DOID:8593",
                            "name": "chronic monocytic leukemia(DOID:8593)"
                        }, {
                            "id": "DOID:8692",
                            "name": "myeloid leukemia(DOID:8692)"
                        }, {
                            "id": "DOID:1240",
                            "name": "leukemia(DOID:1240)"
                        }, {
                            "id": "DOID:4972",
                            "name": "myelodysplastic/myeloproliferative neoplasm(DOID:4972)"
                        }, {
                            "id": "DOID:9119",
                            "name": "acute myeloid leukemia(DOID:9119)"
                        }, {
                            "id": "DOID:0070324",
                            "name": "systemic Epstein-Barr virus-positive T-cell lymphoma of childhood(DOID:0070324)"
                        }, {
                            "id": "DOID:0111147",
                            "name": "angioimmunoblastic T-cell lymphoma(DOID:0111147)"
                        }, {
                            "id": "DOID:9513",
                            "name": "plasma cell leukemia(DOID:9513)"
                        }, {
                            "id": "DOID:3721",
                            "name": "plasmacytoma(DOID:3721)"
                        }, {
                            "id": "DOID:9986",
                            "name": "orbit lymphoma(DOID:9986)"
                        }, {
                            "id": "DOID:9953",
                            "name": "mixed phenotype acute leukemia(DOID:9953)"
                        }, {
                            "id": "DOID:2224",
                            "name": "essential thrombocythemia(DOID:2224)"
                        }, {
                            "id": "DOID:8541",
                            "name": "Sezary's disease(DOID:8541)"
                        }, {
                            "id": "DOID:0050746",
                            "name": "mantle cell lymphoma(DOID:0050746)"
                        }, {
                            "id": "DOID:285",
                            "name": "hairy cell leukemia(DOID:285)"
                        }, {
                            "id": "DOID:0060061",
                            "name": "cutaneous T cell lymphoma(DOID:0060061)"
                        }, {
                            "id": "DOID:1039",
                            "name": "prolymphocytic leukemia(DOID:1039)"
                        }, {
                            "id": "DOID:707",
                            "name": "B-cell lymphoma(DOID:707)"
                        }, {
                            "id": "DOID:775",
                            "name": "intraocular lymphoma(DOID:775)"
                        }, {
                            "id": "DOID:0050873",
                            "name": "follicular lymphoma(DOID:0050873)"
                        }, {
                            "id": "DOID:8567",
                            "name": "Hodgkin's lymphoma(DOID:8567)"
                        }, {
                            "id": "DOID:0080915",
                            "name": "histiocytic sarcoma(DOID:0080915)"
                        }, {
                            "id": "DOID:0060901",
                            "name": "Waldenstroem's macroglobulinemia(DOID:0060901)"
                        }, {
                            "id": "DOID:0050458",
                            "name": "juvenile myelomonocytic leukemia(DOID:0050458)"
                        }, {
                            "id": "DOID:8543",
                            "name": "Hodgkin's lymphoma, lymphocytic-histiocytic predominance(DOID:8543)"
                        }, {
                            "id": "DOID:715",
                            "name": "T-cell lymphoblastic leukemia/lymphoma(DOID:715)"
                        }, {
                            "id": "DOID:2531",
                            "name": "hematologic cancer(DOID:2531)"
                        }, {
                            "id": "DOID:6536",
                            "name": "plasma cell neoplasm(DOID:6536)"
                        }, {
                            "id": "DOID:8584",
                            "name": "Burkitt lymphoma(DOID:8584)"
                        }, {
                            "id": "DOID:1040",
                            "name": "chronic lymphocytic leukemia(DOID:1040)"
                        }, {
                            "id": "DOID:0060060",
                            "name": "non-Hodgkin lymphoma(DOID:0060060)"
                        }, {
                            "id": "DOID:9538",
                            "name": "multiple myeloma(DOID:9538)"
                        }, {
                            "id": "DOID:1037",
                            "name": "lymphoid leukemia(DOID:1037)"
                        }
                    ]
                }
            ]
        },
        "Other": {
            "id": "Other",
            "name": "Other",
            "children": [{
                    "id": "Other",
                    "name": "Other",
                    "children": [{
                            "id": "DOID:5485",
                            "name": "synovial sarcoma(DOID:5485)"
                        }, {
                            "id": "DOID:5875",
                            "name": "retroperitoneal cancer(DOID:5875)"
                        }, {
                            "id": "DOID:3493",
                            "name": "signet ring cell adenocarcinoma(DOID:3493)"
                        }, {
                            "id": "DOID:3512",
                            "name": "neurofibrosarcoma(DOID:3512)"
                        }, {
                            "id": "DOID:8538",
                            "name": "reticulosarcoma(DOID:8538)"
                        }, {
                            "id": "DOID:4697",
                            "name": "perineurioma(DOID:4697)"
                        }, {
                            "id": "DOID:3382",
                            "name": "liposarcoma(DOID:3382)"
                        }, {
                            "id": "DOID:154",
                            "name": "mixed cell type cancer(DOID:154)"
                        }, {
                            "id": "DOID:305",
                            "name": "carcinoma(DOID:305)"
                        }, {
                            "id": "DOID:6262",
                            "name": "follicular dendritic cell sarcoma(DOID:6262)"
                        }, {
                            "id": "DOID:2999",
                            "name": "granulosa cell tumor(DOID:2999)"
                        }, {
                            "id": "DOID:3112",
                            "name": "papillary adenocarcinoma(DOID:3112)"
                        }, {
                            "id": "DOID:162",
                            "name": "cancer(DOID:162)"
                        }, {
                            "id": "DOID:7146",
                            "name": "Langerhans cell sarcoma(DOID:7146)"
                        }, {
                            "id": "DOID:1192",
                            "name": "peripheral nervous system neoplasm(DOID:1192)"
                        }, {
                            "id": "DOID:5093",
                            "name": "cavity(DOID:5093)"
                        }, {
                            "id": "DOID:5268",
                            "name": "myxoid leiomyosarcoma(DOID:5268)"
                        }, {
                            "id": "DOID:6496",
                            "name": "extraskeletal myxoid chondrosarcoma(DOID:6496)"
                        }, {
                            "id": "DOID:5690",
                            "name": "well-differentiated liposarcoma(DOID:5690)"
                        }, {
                            "id": "DOID:5574",
                            "name": "VIPoma(DOID:5574)"
                        }, {
                            "id": "DOID:1749",
                            "name": "squamous cell carcinoma(DOID:1749)"
                        }, {
                            "id": "DOID:688",
                            "name": "embryonal cancer(DOID:688)"
                        }, {
                            "id": "DOID:6193",
                            "name": "epithelioid sarcoma(DOID:6193)"
                        }, {
                            "id": "DOID:2431",
                            "name": "glomus tumor(DOID:2431)"
                        }, {
                            "id": "DOID:4136",
                            "name": "myxosarcoma(DOID:4136)"
                        }, {
                            "id": "DOID:4051",
                            "name": "alveolar rhabdomyosarcoma(DOID:4051)"
                        }, {
                            "id": "DOID:3246",
                            "name": "embryonal rhabdomyosarcoma(DOID:3246)"
                        }, {
                            "id": "DOID:2994",
                            "name": "germ cell cancer(DOID:2994)"
                        }, {
                            "id": "DOID:5363",
                            "name": "myxoid liposarcoma(DOID:5363)"
                        }, {
                            "id": "DOID:3193",
                            "name": "peripheral nerve sheath neoplasm(DOID:3193)"
                        }, {
                            "id": "DOID:4015",
                            "name": "sarcomatoid carcinoma(DOID:4015)"
                        }, {
                            "id": "DOID:4236",
                            "name": "carcinosarcoma(DOID:4236)"
                        }, {
                            "id": "DOID:5264",
                            "name": "epithelioid leiomyosarcoma(DOID:5264)"
                        }, {
                            "id": "DOID:2668",
                            "name": "mesenchymoma(DOID:2668)"
                        }, {
                            "id": "DOID:5940",
                            "name": "malignant peripheral nerve sheath tumor(DOID:5940)"
                        }, {
                            "id": "DOID:3098",
                            "name": "small cell sarcoma(DOID:3098)"
                        }, {
                            "id": "DOID:769",
                            "name": "neuroblastoma(DOID:769)"
                        }, {
                            "id": "DOID:1907",
                            "name": "malignant fibrous histiocytoma(DOID:1907)"
                        }, {
                            "id": "DOID:962",
                            "name": "neurofibroma(DOID:962)"
                        }, {
                            "id": "DOID:201",
                            "name": "connective tissue cancer(DOID:201)"
                        }, {
                            "id": "DOID:5151",
                            "name": "plexiform neurofibroma(DOID:5151)"
                        }, {
                            "id": "DOID:4903",
                            "name": "granular cell carcinoma(DOID:4903)"
                        }, {
                            "id": "DOID:3355",
                            "name": "fibrosarcoma(DOID:3355)"
                        }, {
                            "id": "DOID:5758",
                            "name": "malignant mesenchymoma(DOID:5758)"
                        }, {
                            "id": "DOID:4163",
                            "name": "ganglioneuroblastoma(DOID:4163)"
                        }, {
                            "id": "DOID:3247",
                            "name": "rhabdomyosarcoma(DOID:3247)"
                        }, {
                            "id": "DOID:4045",
                            "name": "muscle cancer(DOID:4045)"
                        }, {
                            "id": "DOID:3095",
                            "name": "germ cell and embryonal cancer(DOID:3095)"
                        }, {
                            "id": "DOID:4440",
                            "name": "seminoma(DOID:4440)"
                        }, {
                            "id": "DOID:3373",
                            "name": "parosteal osteosarcoma(DOID:3373)"
                        }, {
                            "id": "DOID:0050686",
                            "name": "organ system cancer(DOID:0050686)"
                        }, {
                            "id": "DOID:1967",
                            "name": "leiomyosarcoma(DOID:1967)"
                        }, {
                            "id": "DOID:3093",
                            "name": "nervous system cancer(DOID:3093)"
                        }, {
                            "id": "DOID:5563",
                            "name": "malignant teratoma(DOID:5563)"
                        }, {
                            "id": "DOID:1974",
                            "name": "adenosarcoma(DOID:1974)"
                        }, {
                            "id": "DOID:5702",
                            "name": "pleomorphic liposarcoma(DOID:5702)"
                        }, {
                            "id": "DOID:8632",
                            "name": "Kaposi's sarcoma(DOID:8632)"
                        }, {
                            "id": "DOID:4830",
                            "name": "adenosquamous carcinoma(DOID:4830)"
                        }, {
                            "id": "DOID:4545",
                            "name": "mesenchymal chondrosarcoma(DOID:4545)"
                        }
                    ]
                }, {
                    "id": "Mediastinum",
                    "name": "Mediastinum",
                    "children": [{
                            "id": "DOID:5559",
                            "name": "mediastinal cancer(DOID:5559)"
                        }
                    ]
                }, {
                    "id": "Placenta",
                    "name": "Placenta",
                    "children": [{
                            "id": "DOID:3594",
                            "name": "choriocarcinoma(DOID:3594)"
                        }
                    ]
                }, {
                    "id": "Blood Vessels",
                    "name": "Blood Vessels",
                    "children": [{
                            "id": "DOID:175",
                            "name": "vascular cancer(DOID:175)"
                        }, {
                            "id": "DOID:0001816",
                            "name": "angiosarcoma(DOID:0001816)"
                        }, {
                            "id": "DOID:264",
                            "name": "hemangiopericytoma(DOID:264)"
                        }, {
                            "id": "DOID:2643",
                            "name": "perivascular epithelioid cell tumor(DOID:2643)"
                        }
                    ]
                }, {
                    "id": "Pleural",
                    "name": "Pleural",
                    "children": [{
                            "id": "DOID:1790",
                            "name": "malignant mesothelioma(DOID:1790)"
                        }, {
                            "id": "DOID:7474",
                            "name": "malignant pleural mesothelioma(DOID:7474)"
                        }, {
                            "id": "DOID:5158",
                            "name": "pleural cancer(DOID:5158)"
                        }
                    ]
                }, {
                    "id": "Pinal Cord",
                    "name": "Pinal Cord",
                    "children": [{
                            "id": "DOID:5612",
                            "name": "spinal cancer(DOID:5612)"
                        }
                    ]
                }
            ]
        },
        "Abdominal Organs": {
            "id": "Abdominal Organs",
            "name": "Abdominal Organs",
            "children": [{
                    "id": "Intestine",
                    "name": "Intestine",
                    "children": [{
                            "id": "DOID:4908",
                            "name": "anal carcinoma(DOID:4908)"
                        }, {
                            "id": "DOID:9256",
                            "name": "colorectal cancer(DOID:9256)"
                        }, {
                            "id": "DOID:1993",
                            "name": "rectum cancer(DOID:1993)"
                        }, {
                            "id": "DOID:1521",
                            "name": "cecum cancer(DOID:1521)"
                        }, {
                            "id": "DOID:10021",
                            "name": "duodenum cancer(DOID:10021)"
                        }, {
                            "id": "DOID:219",
                            "name": "colon cancer(DOID:219)"
                        }, {
                            "id": "DOID:4929",
                            "name": "tubular adenocarcinoma(DOID:4929)"
                        }, {
                            "id": "DOID:12192",
                            "name": "sigmoid colon cancer(DOID:12192)"
                        }, {
                            "id": "DOID:11239",
                            "name": "appendix cancer(DOID:11239)"
                        }, {
                            "id": "DOID:13499",
                            "name": "jejunal cancer(DOID:13499)"
                        }, {
                            "id": "DOID:6126",
                            "name": "anal canal carcinoma(DOID:6126)"
                        }, {
                            "id": "DOID:0080199",
                            "name": "colorectal carcinoma(DOID:0080199)"
                        }, {
                            "id": "DOID:3559",
                            "name": "pseudomyxoma peritonei(DOID:3559)"
                        }
                    ]
                }, {
                    "id": "Liver",
                    "name": "Liver",
                    "children": [{
                            "id": "DOID:687",
                            "name": "hepatoblastoma(DOID:687)"
                        }, {
                            "id": "DOID:4927",
                            "name": "Klatskin's tumor(DOID:4927)"
                        }, {
                            "id": "DOID:4928",
                            "name": "intrahepatic cholangiocarcinoma(DOID:4928)"
                        }, {
                            "id": "DOID:5015",
                            "name": "fibrolamellar carcinoma(DOID:5015)"
                        }, {
                            "id": "DOID:3571",
                            "name": "liver cancer(DOID:3571)"
                        }
                    ]
                }, {
                    "id": "Pancreas",
                    "name": "Pancreas",
                    "children": [{
                            "id": "DOID:4905",
                            "name": "pancreatic carcinoma(DOID:4905)"
                        }, {
                            "id": "DOID:1799",
                            "name": "islet cell tumor(DOID:1799)"
                        }, {
                            "id": "DOID:1793",
                            "name": "pancreatic cancer(DOID:1793)"
                        }, {
                            "id": "DOID:7698",
                            "name": "non-functioning pancreatic endocrine tumor(DOID:7698)"
                        }, {
                            "id": "DOID:6823",
                            "name": "pancreatoblastoma(DOID:6823)"
                        }, {
                            "id": "DOID:3587",
                            "name": "pancreatic ductal carcinoma(DOID:3587)"
                        }, {
                            "id": "DOID:1798",
                            "name": "pancreatic endocrine carcinoma(DOID:1798)"
                        }
                    ]
                }, {
                    "id": "Biliary Tract",
                    "name": "Biliary Tract",
                    "children": [{
                            "id": "DOID:4606",
                            "name": "bile duct cancer(DOID:4606)"
                        }
                    ]
                }, {
                    "id": "Gastrointestinal Tract",
                    "name": "Gastrointestinal Tract",
                    "children": [{
                            "id": "DOID:3119",
                            "name": "gastrointestinal system cancer(DOID:3119)"
                        }, {
                            "id": "DOID:0060119",
                            "name": "pharynx cancer(DOID:0060119)"
                        }, {
                            "id": "DOID:5041",
                            "name": "esophageal cancer(DOID:5041)"
                        }, {
                            "id": "DOID:10534",
                            "name": "stomach cancer(DOID:10534)"
                        }, {
                            "id": "DOID:10155",
                            "name": "intestinal cancer(DOID:10155)"
                        }, {
                            "id": "DOID:9253",
                            "name": "gastrointestinal stromal tumor(DOID:9253)"
                        }
                    ]
                }, {
                    "id": "Bile Duct",
                    "name": "Bile Duct",
                    "children": [{
                            "id": "DOID:4607",
                            "name": "biliary tract cancer(DOID:4607)"
                        }, {
                            "id": "DOID:4947",
                            "name": "cholangiocarcinoma(DOID:4947)"
                        }
                    ]
                }, {
                    "id": "Gallbladder",
                    "name": "Gallbladder",
                    "children": [{
                            "id": "DOID:3121",
                            "name": "gallbladder cancer(DOID:3121)"
                        }, {
                            "id": "DOID:4897",
                            "name": "bile duct carcinoma(DOID:4897)"
                        }
                    ]
                }, {
                    "id": "Stomach",
                    "name": "Stomach",
                    "children": [{
                            "id": "DOID:4023",
                            "name": "linitis plastica(DOID:4023)"
                        }
                    ]
                }, {
                    "id": "Spleen",
                    "name": "Spleen",
                    "children": [{
                            "id": "DOID:672",
                            "name": "spleen cancer(DOID:672)"
                        }
                    ]
                }
            ]
        },
        "Bone": {
            "id": "Bone",
            "name": "Bone",
            "children": [{
                    "id": "Bone",
                    "name": "Bone",
                    "children": [{
                            "id": "DOID:2776",
                            "name": "adamantinoma(DOID:2776)"
                        }, {
                            "id": "DOID:4143",
                            "name": "orbital cancer(DOID:4143)"
                        }, {
                            "id": "DOID:3302",
                            "name": "chordoma(DOID:3302)"
                        }, {
                            "id": "DOID:1862",
                            "name": "jaw cancer(DOID:1862)"
                        }, {
                            "id": "DOID:3369",
                            "name": "Ewing sarcoma(DOID:3369)"
                        }, {
                            "id": "DOID:2775",
                            "name": "long bone adamantinoma(DOID:2775)"
                        }, {
                            "id": "DOID:4618",
                            "name": "maxillary cancer(DOID:4618)"
                        }, {
                            "id": "DOID:5546",
                            "name": "femoral cancer(DOID:5546)"
                        }, {
                            "id": "DOID:1863",
                            "name": "skull cancer(DOID:1863)"
                        }, {
                            "id": "DOID:5867",
                            "name": "clear cell chondrosarcoma(DOID:5867)"
                        }, {
                            "id": "DOID:3347",
                            "name": "osteosarcoma(DOID:3347)"
                        }, {
                            "id": "DOID:3371",
                            "name": "chondrosarcoma(DOID:3371)"
                        }, {
                            "id": "DOID:184",
                            "name": "bone cancer(DOID:184)"
                        }, {
                            "id": "DOID:3618",
                            "name": "epidural spinal canal neoplasm(DOID:3618)"
                        }, {
                            "id": "DOID:4233",
                            "name": "clear cell sarcoma(DOID:4233)"
                        }, {
                            "id": "DOID:2338",
                            "name": "mandibular cancer(DOID:2338)"
                        }
                    ]
                }
            ]
        },
        "Urinary Organs": {
            "id": "Urinary Organs",
            "name": "Urinary Organs",
            "children": [{
                    "id": "Bladder",
                    "name": "Bladder",
                    "children": [{
                            "id": "DOID:5958",
                            "name": "bladder urachal carcinoma(DOID:5958)"
                        }, {
                            "id": "DOID:2671",
                            "name": "transitional cell carcinoma(DOID:2671)"
                        }
                    ]
                }, {
                    "id": "Kidney",
                    "name": "Kidney",
                    "children": [{
                            "id": "DOID:4773",
                            "name": "congenital mesoblastic nephroma(DOID:4773)"
                        }, {
                            "id": "DOID:4450",
                            "name": "renal cell carcinoma(DOID:4450)"
                        }, {
                            "id": "DOID:4473",
                            "name": "sarcomatoid renal cell carcinoma(DOID:4473)"
                        }, {
                            "id": "DOID:4471",
                            "name": "chromophobe renal cell carcinoma(DOID:4471)"
                        }, {
                            "id": "DOID:263",
                            "name": "kidney cancer(DOID:263)"
                        }, {
                            "id": "DOID:3672",
                            "name": "rhabdoid cancer(DOID:3672)"
                        }, {
                            "id": "DOID:2154",
                            "name": "nephroblastoma(DOID:2154)"
                        }, {
                            "id": "DOID:4467",
                            "name": "clear cell renal cell carcinoma(DOID:4467)"
                        }
                    ]
                }, {
                    "id": "Urethra",
                    "name": "Urethra",
                    "children": [{
                            "id": "DOID:734",
                            "name": "urethra cancer(DOID:734)"
                        }
                    ]
                }, {
                    "id": "Urinary Organs",
                    "name": "Urinary Organs",
                    "children": [{
                            "id": "DOID:4464",
                            "name": "collecting duct carcinoma(DOID:4464)"
                        }, {
                            "id": "DOID:11054",
                            "name": "urinary bladder cancer(DOID:11054)"
                        }, {
                            "id": "DOID:4465",
                            "name": "papillary renal cell carcinoma(DOID:4465)"
                        }
                    ]
                }
            ]
        },
        "Skin": {
            "id": "Skin",
            "name": "Skin",
            "children": [{
                    "id": "Skin",
                    "name": "Skin",
                    "children": [{
                            "id": "DOID:5063",
                            "name": "basosquamous carcinoma(DOID:5063)"
                        }, {
                            "id": "DOID:7566",
                            "name": "eccrine porocarcinoma(DOID:7566)"
                        }, {
                            "id": "DOID:4159",
                            "name": "skin cancer(DOID:4159)"
                        }, {
                            "id": "DOID:4359",
                            "name": "amelanotic melanoma(DOID:4359)"
                        }, {
                            "id": "DOID:4235",
                            "name": "spindle cell sarcoma(DOID:4235)"
                        }, {
                            "id": "DOID:3149",
                            "name": "keratoacanthoma(DOID:3149)"
                        }, {
                            "id": "DOID:4839",
                            "name": "sebaceous adenocarcinoma(DOID:4839)"
                        }, {
                            "id": "DOID:8923",
                            "name": "skin melanoma(DOID:8923)"
                        }, {
                            "id": "DOID:1909",
                            "name": "melanoma(DOID:1909)"
                        }, {
                            "id": "DOID:3450",
                            "name": "cutaneous Paget's disease(DOID:3450)"
                        }, {
                            "id": "DOID:2513",
                            "name": "basal cell carcinoma(DOID:2513)"
                        }, {
                            "id": "DOID:3737",
                            "name": "verrucous carcinoma(DOID:3737)"
                        }, {
                            "id": "DOID:6039",
                            "name": "uveal melanoma(DOID:6039)"
                        }
                    ]
                }
            ]
        },
        "Thoracic Organs": {
            "id": "Thoracic Organs",
            "name": "Thoracic Organs",
            "children": [{
                    "id": "Lung",
                    "name": "Lung",
                    "children": [{
                            "id": "DOID:5411",
                            "name": "lung oat cell carcinoma(DOID:5411)"
                        }, {
                            "id": "DOID:8007",
                            "name": "Pancoast tumor(DOID:8007)"
                        }, {
                            "id": "DOID:4239",
                            "name": "alveolar soft part sarcoma(DOID:4239)"
                        }, {
                            "id": "DOID:4926",
                            "name": "bronchiolo-alveolar adenocarcinoma(DOID:4926)"
                        }, {
                            "id": "DOID:3030",
                            "name": "mucinous adenocarcinoma(DOID:3030)"
                        }, {
                            "id": "DOID:5409",
                            "name": "lung small cell carcinoma(DOID:5409)"
                        }, {
                            "id": "DOID:4765",
                            "name": "pulmonary blastoma(DOID:4765)"
                        }, {
                            "id": "DOID:3908",
                            "name": "lung non-small cell carcinoma(DOID:3908)"
                        }, {
                            "id": "DOID:3910",
                            "name": "lung adenocarcinoma(DOID:3910)"
                        }, {
                            "id": "DOID:4769",
                            "name": "pleuropulmonary blastoma(DOID:4769)"
                        }, {
                            "id": "DOID:4552",
                            "name": "large cell carcinoma(DOID:4552)"
                        }, {
                            "id": "DOID:5583",
                            "name": "lung giant cell carcinoma(DOID:5583)"
                        }
                    ]
                }, {
                    "id": "Esophagus",
                    "name": "Esophagus",
                    "children": [{
                            "id": "DOID:4914",
                            "name": "esophagus adenocarcinoma(DOID:4914)"
                        }, {
                            "id": "DOID:3748",
                            "name": "esophagus squamous cell carcinoma(DOID:3748)"
                        }
                    ]
                }, {
                    "id": "Heart",
                    "name": "Heart",
                    "children": [{
                            "id": "DOID:117",
                            "name": "heart cancer(DOID:117)"
                        }
                    ]
                }, {
                    "id": "Bronchus",
                    "name": "Bronchus",
                    "children": [{
                            "id": "DOID:3904",
                            "name": "bronchus carcinoma(DOID:3904)"
                        }
                    ]
                }, {
                    "id": "Respiratory Tract",
                    "name": "Respiratory Tract",
                    "children": [{
                            "id": "DOID:9261",
                            "name": "nasopharynx carcinoma(DOID:9261)"
                        }
                    ]
                }
            ]
        }
    }
}
