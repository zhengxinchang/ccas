


config ={
    "global":{


    },
    "snv":{
        "variant_level_annotation_sciript":"/canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/CCAS2.0.pipeline.snv.v1.2.sh",
        "mutsigcal":"/canceranno/zhengxc/canceranno/R/R-3.6.1/bin/Rscript /canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/sub/processSNV_MutationSig.r"
    },
    "bed":{
        "gene_bed":{
            "hg19":"/canceranno/zhengxc/ccas2/resources/Homo_sapiens.GRCh37.87.chr.bed",
            "hg38":"/canceranno/zhengxc/ccas2/resources/Homo_sapiens.GRCh38.104.chr.bed"
        }
    },
    "exp":{
        "gene_name_bed":{
            "hg19":"/canceranno/zhengxc/ccas2/resources/Homo_sapiens.GRCh37.87.chr.bed",
            "hg38":"/canceranno/zhengxc/ccas2/resources/Homo_sapiens.GRCh38.104.chr.bed"
        },
        "ssGSEA":{
            "cmd":"~/miniconda3/envs/fastapi/bin/Rscript /canceranno/zhengxc/ccas2/test_ccas2_pipelinev1/sub/processExp_ssGSEA.r",
            "mappingFile":"/canceranno/zhengxc/ccas2/resources/gencode.v25.gid_symbol",
            # "gmtFile":"/canceranno/zhengxc/ccas2/resources/msigdb.v7.5.1.symbols.gmt",
            "gmtFile":"/canceranno/zhengxc/ccas2/resources/c2.all.v7.5.1.symbols.gmt",
        }
    }
}


globalError = []

