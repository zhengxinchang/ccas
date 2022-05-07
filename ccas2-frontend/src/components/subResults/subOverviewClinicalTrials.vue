<template>
  <v-sheet class="mx-3">
    <v-row  class="pt-6">
      <v-col cols="12">
        <v-sheet  >

          <v-sheet>
            <filter-panel #default="{ isexpand}">
            <v-sheet v-show="isexpand" color="grey lighten-4"  min-height="100" class="py-6">
              <v-row class="mx-3 pt-3">
                <v-col cols="3">
                  <v-text-field
                    v-model="dat.tablePage1.BriefTitle"
                    background-color="white"

                    clearable
                    color="teal" dense hide-details label="Brief Title" outlined
                  >
                  </v-text-field>
                </v-col>
                <v-col cols="3">
                  <v-text-field
                    v-model="dat.tablePage1.NCTID"
                    background-color="white"
                    clearable
                    color="teal" dense hide-details label="NCT ID" outlined
                  >
                  </v-text-field>
                </v-col>
                <v-col cols="3">
                  <v-text-field
                    v-model="dat.tablePage1.Intervention"
                    background-color="white"
                    clearable
                    color="teal" dense hide-details label="Intervention" outlined
                  >
                  </v-text-field>
                </v-col>
                <v-col cols="3">

                  <v-select

                    v-model="dat.tablePage1.Phase"
                    :items="['Phase 1','Phase 2','Phase 3','Phase 4']"
                    background-color="white"
                    clearable
                    color="teal"
                    dense hide-details label="Phase" outlined
                  >

                  </v-select>
                </v-col>
              </v-row>

            </v-sheet>
            </filter-panel>
          </v-sheet>

          <vxe-toolbar ref="xToolbar1" custom export print></vxe-toolbar>
          <vxe-table
            ref="xTable1"
            :align="dat.allAlign"
            :column-config="{resizable: true}"
            :data="dat.tableData"
            :export-config="{}"
            :loading="dat.tableloading1"
            :print-config="{}"
            :sort-config="{remote:true,trigger:'cell'}"
            border
            empty-text="Empty"
            round
            stripe
            @sort-change="customSortMethod"
          >

            <vxe-column width="5%" show-overflow="tooltip"  type="expand">
              <template #content="{row,rowIndex}">
                <v-sheet class="pa-3" rounded>
                  <v-row class="px-2">
                    <v-col cols="6">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Brief Summary</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>

                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" height="250" color="grey lighten-3" v-html="row.BriefSummary">

                          </v-sheet>
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-col cols="6">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Detail Description</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>
                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" color="grey lighten-3" height="250" v-html="row.DetailDescription">

                          </v-sheet>
                        </v-col>
                      </v-row>

                    </v-col>
                    <v-col cols="6">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Eligbility Criteria</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>
                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" color="grey lighten-3" height="250" v-html="row.EligbilityCriteria">

                          </v-sheet>
                        </v-col>
                      </v-row>

                    </v-col>
                    <v-col cols="3">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">MeSH Terms</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>
                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" color="grey lighten-3" height="250" >
                            <v-list color="grey lighten-3">
                              <v-list-item  color="grey lighten-3" :key="item" v-for="item in (row.MESH && row.MESH.split('/') || []) " >
                                <v-icon color="teal">
                                  mdi-hexagon-slice-6
                                </v-icon> &nbsp;
                                {{item}}
                              </v-list-item>
                            </v-list>
                          </v-sheet>
                        </v-col>
                      </v-row>

                    </v-col>
                    <v-col cols="3">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Intervention</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>
                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" color="grey lighten-3" height="250" >
                            <v-list color="grey lighten-3">
                              <v-list-item  color="grey lighten-3" :key="item" v-for="item in (row.Intervention && row.Intervention.split('/') || []) " >
                                <v-icon color="teal">
                                  mdi-hexagon-slice-6
                                </v-icon> &nbsp;
                                {{item}}
                              </v-list-item>
                            </v-list>
                          </v-sheet>
                        </v-col>
                      </v-row>

                    </v-col>
                  </v-row>
                </v-sheet>

              </template>
            </vxe-column>
            <vxe-column field="BriefTitle" show-overflow="tooltip" width="70%"  title="Brief Title"></vxe-column>
            <vxe-column field="NCTID" sortable show-overflow="tooltip"  width="15%" title="NCT ID">

              <template #default = "{row}" >
                <a style="text-decoration: none"  class="teal--text" :href="$commonfunc.renderLinkNCTID(row.NCTID) " target="_blank">{{row.NCTID}}</a>
              </template>
            </vxe-column>
            <vxe-column field="Phase" sortable show-overflow="tooltip"  width="10%" title="Phase"></vxe-column>
<!--            <vxe-column  field="MESH"  width="10%" title="MeSH">-->

<!--            </vxe-column>-->
          </vxe-table>
          <vxe-pager
            :current-page="dat.tablePage1.currentPage"
            :layouts="['PrevPage', 'JumpNumber', 'NextPage', 'FullJump', 'Sizes', 'Total']"
            :loading="dat.tableloading1"
            :page-size="dat.tablePage1.pageSize"
            :total="dat.tablePage1.totalPage"
            @page-change="handlePageChange"
          >

          </vxe-pager>
        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="2">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://clinicaltrials.gov/" small
          style="text-transform: none"
          target="_blank"> Clinical trials
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import Axios from "axios";
import FilterPanel from "../sub/filterPanel";

export default {
name: "subOverviewClinicalTrials",
  components: {FilterPanel},
  props:['jobid'],
  data(){
  return{
      dat:{
        allAlign: null,
        tableData: [],
        tableloading1: false,
        tablePage1: {
          currentPage: 1,
          pageSize: 10,
          totalPage: null,
          ORDERBY:null,
          ORDERDESC:false,
          BriefTitle:null,
          Intervention:null,
          NCTID:null,
          Phase:null,
        },
      }
  }
  },
  methods:{
    handlePageChange({currentPage, pageSize}) {
      this.dat.tablePage1.currentPage = currentPage
      this.dat.tablePage1.pageSize = pageSize
      this.loadDataByPage()
    },
    loadDataByPage() {
      this.dat.tableloading1 = true
      Axios.post(
        "/ccas/api/get_overview_clinical_table_by_page",
        {},
        {
          params: {
            jobid: this.jobid,
            pageNumber: this.dat.tablePage1.currentPage,
            pageSize: this.dat.tablePage1.pageSize,
            ORDERBY:this.dat.tablePage1.ORDERBY,
            ORDERDESC:this.dat.tablePage1.ORDERDESC,
            BriefTitle:this.dat.tablePage1.BriefTitle,
            Intervention:this.dat.tablePage1.Intervention,
            NCTID:this.dat.tablePage1.NCTID,
            Phase:this.dat.tablePage1.Phase
          }
        }
      ).then(res => {
        this.dat.tableData = res.data.data
        this.dat.tablePage1.totalPage = res.data.count.count;
        this.dat.tableloading1 = false
      })

      // this.dat.tableloading1 = false;
    },
    customSortMethod({data, column, property, order}) {

      this.dat.tablePage1.ORDERBY = property;
      if (order == 'desc') {
        this.dat.tablePage1.ORDERDESC = true
      } else {
        this.dat.tablePage1.ORDERDESC = false
      }
      this.dat.tablePage1.currentPage = 1;
      this.loadDataByPage()
    },
    debounceFilter: _.debounce(function () {
      // console.log("enter setTimeout")
      // this.dat.filterQuery.symbol = false;
      this.dat.tablePage1.currentPage=1
      this.loadDataByPage()
    }, 500),

  },
  watch:{
    'jobid': {
      handler: function (jobid) {

        // 这里开始load结果
        // disease overview
        // Axios.post(
        //   "/ccas/api/get_overview_disease_ontology",
        //   {},
        //   {
        //     params: {
        //       jobid: jobid
        //     }
        //   }
        // ).then(res => {
        //   // console.log(res.data.data)
        //   this.dat.overview.diseaseOverview = res.data.data
        // })
        //
        // this.loadTotalDataNumber()
        this.loadDataByPage()
        //end

      },
      deep: true,
      immediate: true
    },
    'dat.tablePage1.BriefTitle': function () {
      console.log("dat.tablePage1.BriefTitle changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.Intervention': function () {
      console.log("dat.tablePage1.Intervention changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.NCTID': function () {
      console.log("dat.tablePage1.NCTID changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.Phase': function () {
      console.log("dat.tablePage1.Phase changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
  }
}
</script>

<style scoped>

</style>
