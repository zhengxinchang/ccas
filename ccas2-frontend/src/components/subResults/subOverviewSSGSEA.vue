<template>
  <v-sheet>
    <v-row>
      <v-col cols="10" offset="1">
        <v-sheet class="my-4">
          Single-sample GSEA (ssGSEA), an extension of Gene Set Enrichment Analysis (GSEA), calculates separate enrichment scores for each pairing of a sample and gene set.&nbsp;Each ssGSEA enrichment score represents the degree to which the genes in a particular gene set are coordinately up- or down-regulated within a sample.
        </v-sheet>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="8" offset="2">
        <v-sheet  outlined rounded class="overflow-y-auto"  height="400">
<!--        <sub-overview-s-s-g-s-e-a_echarts_bar :jobid="jobid"></sub-overview-s-s-g-s-e-a_echarts_bar>-->
          <v-list dense  >
            <v-list-item  style="min-height: 30px"  v-for="x in dat" :key="x.name">
              <v-row dense  align="center" >
                <v-col cols="6" class="text-right">
                  <v-sheet class="text-body-2" >{{x.Name}}</v-sheet>
                </v-col>
                <v-col cols="6">
                  <v-sheet  class="text-center text-body-2 "  dark rounded color="teal" height="20" :width="x.Value* thisWidth">
                    {{x.Value }}
                  </v-sheet>
                </v-col>
              </v-row>
            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="10" offset="1">
        <v-sheet class="font-weight-bold">
          References:
        </v-sheet>
        <v-sheet>
          1. Subramanian A, Tamayo P, Mootha VK, Mukherjee S, Ebert BL, Gillette MA, Paulovich A, Pomeroy SL, Golub TR, Lander ES, Mesirov JP. Gene set enrichment analysis: A knowledge-based approach for interpreting genome-wide expression profiles.&nbsp;PNAS. 2005;102(43):15545-15550. &nbsp;http://www.pnas.org/content/102/43/15545.abstract
          <br/>
          2. Barbie DA, Tamayo P, et al. Systematic RNA interference reveals that oncogenic KRAS-driven cancers require TBK1. &nbsp;Nature. 2009;462:108-112.
        </v-sheet>
      </v-col>
    </v-row>

  </v-sheet>
</template>

<script>
import SubOverviewSSGSEA_echarts_bar from "./subOverviewSSGSEA_echarts_bar";
export default {
name: "subOverviewSSGSEA",
  components: {SubOverviewSSGSEA_echarts_bar},
  props:["jobid"],
  data(){
  return{
    dat: [
      {
        "Name": "TIMOFEEVA_GROWTH_STRESS_VIA_STAT1_DN",
        "Value": "0.499448732083793"
      },
      {
        "Name": "GCM_PSME1",
        "Value": "0.499448732083793"
      },
      {
        "Name": "LAKE_ADULT_KIDNEY_C7_PROXIMAL_TUBULE_EPITHELIAL_CELLS_S3",
        "Value": "0.498893046153348"
      },
      {
        "Name": "GOCC_POLYSOMAL_RIBOSOME",
        "Value": "0.498346196251378"
      },
      {
        "Name": "HP_ABNORMAL_GRANULOCYTOPOIETIC_CELL_MORPHOLOGY",
        "Value": "0.498346196251378"
      },
      {
        "Name": "HP_ABNORMAL_NUMBER_OF_GRANULOCYTE_PRECURSORS",
        "Value": "0.498346196251378"
      },
      {
        "Name": "LUI_THYROID_CANCER_CLUSTER_3",
        "Value": "0.498346196251378"
      },
      {
        "Name": "LUI_TARGETS_OF_PAX8_PPARG_FUSION",
        "Value": "0.498346196251378"
      },
      {
        "Name": "CHNG_MULTIPLE_MYELOMA_HYPERPLOID_UP",
        "Value": "0.498346196251378"
      },
      {
        "Name": "GCM_TPT1",
        "Value": "0.498346196251378"
      },
      {
        "Name": "GNF2_GLTSCR2",
        "Value": "0.498346196251378"
      },
      {
        "Name": "WP_CYTOPLASMIC_RIBOSOMAL_PROTEINS",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_ABNORMALITY_OF_THE_THENAR_EMINENCE",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_NORMOCHROMIC_ANEMIA",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_RETICULOCYTOPENIA",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_OSTEOSARCOMA",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_ACUTE_MYELOID_LEUKEMIA",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_MALIGNANT_GENITOURINARY_TRACT_TUMOR",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_DUPLICATION_OF_THUMB_PHALANX",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_PARTIAL_DUPLICATION_OF_THE_PHALANX_OF_HAND",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_PERSISTENCE_OF_HEMOGLOBIN_F",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_ABNORMAL_NUMBER_OF_ERYTHROID_PRECURSORS",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_ERYTHROID_HYPOPLASIA",
        "Value": "0.49834384101322"
      },
      {
        "Name": "HP_PURE_RED_CELL_APLASIA",
        "Value": "0.49834384101322"
      },
      {
        "Name": "BUSSLINGER_GASTRIC_PPP1R1B_POSITIVE_CELLS",
        "Value": "0.49834384101322"
      },
      {
        "Name": "MORF_JUND",
        "Value": "0.49834384101322"
      },
      {
        "Name": "GOBP_NEGATIVE_REGULATION_OF_UBIQUITIN_PROTEIN_TRANSFERASE_ACTIVITY",
        "Value": "0.497243660418964"
      },
      {
        "Name": "GOBP_POSITIVE_REGULATION_OF_SIGNAL_TRANSDUCTION_BY_P53_CLASS_MEDIATOR",
        "Value": "0.497243660418964"
      },
      {
        "Name": "GOBP_REGULATION_OF_UBIQUITIN_PROTEIN_LIGASE_ACTIVITY",
        "Value": "0.497243660418964"
      }
      ],
    thisWidth:"600"
  }
  }
}
</script>

<style scoped>

</style>
