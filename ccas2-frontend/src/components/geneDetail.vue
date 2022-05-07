<template>
  <v-container class="container--fluid">

    <v-btn color="teal" dark elevation="1" fab style="position: fixed;bottom: 100px;right: 100px;z-index: 99999999"
           @click="()=>{ $router.push({ name: 'annoresults', params: { jobid: $route.params.jobid }})}">back
    </v-btn>
    <v-sheet class="z-transparent" style="margin-top: 120px;"></v-sheet>
    <v-row align="center">
      <v-col cols="12">
        <v-sheet class="px4 mx-6" max-height="60" min-height="60" rounded>
          <v-row align="center" dense>
            <v-col cols="6">
              <v-breadcrumbs
                divider="/"
              >
                <!--                :items="[-->
                <!--                {text:'home',disabled:false,to:'/home'},-->
                <!--                {text:'check results',disabled:false,to:'/checkresults'},-->
                <!--                {text:'results',disabled:false,to:'/annoresults/'+$route.params.jobid},-->
                <!--                {text:$route.params.geneid,disabled:true},-->
                <!--                ]"-->

                <v-breadcrumbs-item to="/home">home</v-breadcrumbs-item> &nbsp; /
                <v-breadcrumbs-item to="checkresults">check results</v-breadcrumbs-item>
                /&nbsp;&nbsp;
                <v-breadcrumbs-item to=""
                                    @click="()=>{ $router.push({ name: 'annoresults', params: { jobid: $route.params.jobid }})}">
                  <a style="text-decoration: none">results</a>
                </v-breadcrumbs-item>&nbsp;&nbsp;/
                <v-breadcrumbs-item>{{ $route.params.geneid }}</v-breadcrumbs-item>
              </v-breadcrumbs>
            </v-col>
            <v-spacer></v-spacer>
            <v-col cols="1">
              <v-btn color="teal"
                     dark elevation="0" small style="text-transform: none"
                     @click="()=>{ $router.push({ name: 'annoresults', params: { jobid: $route.params.jobid }})}">
                <v-icon>mdi-chevron-double-left</v-icon>
                back
              </v-btn>
            </v-col>
          </v-row>

        </v-sheet>
      </v-col>
    </v-row>

    <!--    导航结束-->
    <v-row>
      <v-col cols="12">
        <v-sheet class="px4 mx-6" rounded>
          <v-card>
            <v-toolbar
              color="teal"
              dark
              flat
            >
              <v-toolbar-title>
                <v-icon class="mdi-36px">mdi-power-on</v-icon>
                Gene {{ dat.genedata && dat.genedata.geneid && dat.genedata.geneid.replace("GENEID:", "") || "" }}
              </v-toolbar-title>
            </v-toolbar>
            <v-sheet class="pa-3" rounded>
              <!--              内部是核心内容-->
              <gene-detail-gene-basic :dat="dat.genedata"></gene-detail-gene-basic>

            </v-sheet>
          </v-card>
        </v-sheet>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-sheet class="px4 mx-6" rounded>
          <v-card>
            <v-toolbar
              color="teal"
              dark
              flat
            >
              <v-toolbar-title>
                <v-icon class="mdi-36px">mdi-power-on</v-icon>
                Gene Associated Information
              </v-toolbar-title>
            </v-toolbar>
            <v-sheet class="pa-3" rounded>
              <!--              内部是核心内容-->

              <v-tabs class="text-start text-body-2 px-3  mt-3" color="teal" grow>
                <!--              取消把字体都转换为大写-->
                <v-tab style="text-transform: none">
                  <v-icon left>
                    mdi-circle-slice-8
                  </v-icon>
                  Abnormalities in user uploaded data
                </v-tab>
                <v-tab style="text-transform: none">
                  <v-icon left>
                    mdi-circle-slice-8
                  </v-icon>
                  Associated pathways <span><common-help-message>
                  This tab shows the pathways that accsociated with this gene. Other inforamtion about the pathway are also shown in this section. Please note that those data are integrated from Reactome database and may not cover all pathways of this gene.
                </common-help-message></span>
                </v-tab>
                <v-tab style="text-transform: none">
                  <v-icon left>
                    mdi-circle-slice-8
                  </v-icon>
                  Assoicated cancer cohorts
                </v-tab>
                <v-tab style="text-transform: none">
                  <v-icon left>
                    mdi-circle-slice-8
                  </v-icon>
                  Assoicated Literature
                </v-tab>
                <v-tab style="text-transform: none">
                  <v-icon left>
                    mdi-circle-slice-8
                  </v-icon>
                  Assoicated Drug Interactions(DGIdb)<span><common-help-message>
                  CCAS incorporated 2 Gene~Drug interactions databases. <br/>This section shows the data retrievaled from DGIdb.
                  Providing the Gene~Drug interactions along with interaction scores. Score is positively correlated with the intensity of interaction.
                </common-help-message></span>
                </v-tab>
                <v-tab style="text-transform: none">
                  <v-icon left>
                    mdi-circle-slice-8
                  </v-icon>
                  Assoicated Drug Interactions(OpenTargetPlatform) <span><common-help-message>
                  CCAS incorporated 2 Gene~Drug interactions databases. <br/>This section shows the data retrievaled from Open Target Platform.
                  Providing the Gene~Drug interactions along with Disease information, clincial trials, and the mechanism of action.
                </common-help-message></span>
                </v-tab>

                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <gene-detail-abnomal-user-uploaded
                        :cnv-table-data="dat.genedata.data.patient_cnv_list || []"
                        :exp-table-data="dat.genedata.data.patient_exp_list || []"
                        :meth-table-data="dat.genedata.data.patient_meth_list || []"
                        :snv-table-data="dat.genedata.data.patient_snvindel_list || []"
                      ></gene-detail-abnomal-user-uploaded>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <gene-detail-pathways :table-data="dat.genedata.data.reactome || []"></gene-detail-pathways>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <gene-detail-cancer-cohort :table-data="dat.genedata.data.intogen || []"></gene-detail-cancer-cohort>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <gene-detail-papers :table-data="dat.genedata.data.cancermine || []"></gene-detail-papers>

                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <gene-detail-drug-interaction
                        :table-data="dat.genedata.data.dgidb || []"></gene-detail-drug-interaction>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <gene-detail-drug-interaction2
                        :table-data="dat.genedata.data.opentarget || []"></gene-detail-drug-interaction2>
                    </v-card-text>
                  </v-card>
                </v-tab-item>


              </v-tabs>
            </v-sheet>
          </v-card>
        </v-sheet>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import Axios from 'axios'
import _ from 'lodash'
import GeneDetailGeneBasic from "./subResultsDetails/geneDetailGeneBasic";
import GeneDetailPathways from "./subResultsDetails/geneDetailPathways";
import CommonHelpMessage from "./sub/commonHelpMessage";
import GeneDetailPapers from "./subResultsDetails/geneDetailPapers";
import GeneDetailDrugInteraction from "./subResultsDetails/geneDetailDrugInteraction";
import GeneDetailDrugInteraction2 from "./subResultsDetails/geneDetailDrugInteraction2";
import GeneDetailAbnomalUserUploaded from "./subResultsDetails/geneDetailAbnomalUserUploaded";
import GeneDetailCancerCohort from "./subResultsDetails/geneDetailCancerCohort";

export default {
  name: "geneDetail",
  components: {
    GeneDetailCancerCohort,
    GeneDetailAbnomalUserUploaded,
    GeneDetailDrugInteraction2,
    GeneDetailDrugInteraction, GeneDetailPapers, CommonHelpMessage, GeneDetailPathways, GeneDetailGeneBasic
  },
  data() {
    return {

      dat: {
        genedata: null,
      }
    }
  },
  computed: {
    jobidgeneid: function () {
      let jobid = this.$route.params.jobid
      let geneid = this.$route.params.geneid
      // console.log("jobid"+jobid)
      // console.log("geneid"+geneid)
      return ({jobid, geneid})
    },
  },
  watch: {
    'jobidgeneid': {
      handler: function (jobid) {
        this.loadData()
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    loadData() {
      Axios.post(
        "/ccas/api/get_one_gene_anno_by_geneid",
        {},
        {
          params: {
            jobid: this.$route.params.jobid,
            geneid: this.$route.params.geneid,
          }
        }
      ).then(res => {
        this.dat.genedata = res.data.data;
      })
    }
  }
}
</script>

<style scoped>

</style>
