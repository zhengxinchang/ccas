<template>
  <v-sheet class="mx-3">
    <v-row  class="pt-6">
      <v-col cols="12">
        <v-sheet  >

          <v-sheet>
            <filter-panel #default="{ isexpand}">
              <v-sheet v-show="isexpand" color="grey lighten-4"  min-height="100" class="py-6">
                <v-row align="center" class="mx-3 pt-3">
                  <v-col cols="3">
                    <v-text-field
                      v-model="dat.tablePage1.DisplayName"
                      background-color="white"

                      clearable
                      color="teal" dense hide-details label="Pathway Name" outlined
                    >
                    </v-text-field>
                  </v-col>
                  <v-col cols="3">
                    <v-text-field
                      v-model="dat.tablePage1.ID"
                      background-color="white"
                      clearable
                      color="teal" dense hide-details label="Reactome ID" outlined
                    >
                    </v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-card  color="grey lighten-3" class="px-2 " outlined shaped tile   rounded>
                      <v-row dense align="center">
                        <v-col cols="3">
                          <v-checkbox
                            class="py-0"
                            v-model="dat.tablePage1.HAS_SNVINDEL"
                            color="teal"
                            label="Show data must include variants at SNV/Indels level"
                          ></v-checkbox>
                        </v-col>
                        <v-col cols="3">
                          <v-checkbox
                            class="py-0"
                            v-model="dat.tablePage1.HAS_EXP"
                            color="teal"
                            label="Show data must include variants at Expression level"
                          ></v-checkbox>
                        </v-col>
                        <v-col cols="3">
                          <v-checkbox
                            class="py-0"
                            v-model="dat.tablePage1.HAS_CNV"
                            color="teal"
                            label="Show data must include variants at CNV level"
                          ></v-checkbox>
                        </v-col>

                        <v-col cols="3">
                          <v-checkbox
                            class="py-0"
                            v-model="dat.tablePage1.HAS_METH"
                            color="teal"
                            label="Show data must include variants at Methylation level"
                          ></v-checkbox>
                        </v-col>
                      </v-row>


                    </v-card>

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
                    <v-col cols="12">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Literature</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>

                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto"  >
                            <vxe-table
                              border
                              stripe
                              round
                              height="300"
                              :data="row.literatureReference"
                              ref="subpathwayPaper"
                            >
                              <vxe-column field="title" width="50%" title="Title">
                                <template #default = "{row}" >
                                  <a style="text-decoration: none"  class="teal--text" :href="row.url" target="_blank">{{row.title}}</a>


                                </template>
                              </vxe-column>
                              <vxe-column field="year" title="Year"></vxe-column>
                              <vxe-column field="journal" title="Journal"></vxe-column>
                              <vxe-column  title="Details">
                                <template #default = "{row}" >
                                  volume:{{row.volume}}
                                  page:{{row.pages}}
                                </template>
                              </vxe-column>

                            </vxe-table>

                          </v-sheet>
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-col cols="6">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Genes in the pathway and detected in user uploaded data</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>
                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" color="grey lighten-3"  >
                            <v-list height="250" class="overflow-x-auto overflow-y-auto" color="grey lighten-3">
                              <v-list-item :key="item" v-for="item in row.HitsGene">
                                <v-list-item-icon>
                                  <v-icon color="teal">
                                    mdi-hexagon-slice-6
                                  </v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                  <v-list-item-title >
                                    <v-chip color="teal" label outlined @click="$router.push({name:'genedetail',params:{jobid:jobid,geneid:'GENEID:'+item.ENSG}})">Ensembl ID:&nbsp; {{item.ENSG}}</v-chip>
                                  </v-list-item-title>

                                  <v-list-item-subtitle >
                                    Detected levels: &nbsp;
                                    <v-chip color="teal lighten-2" v-show="item.snvindel " label outlined>SNV/Indels</v-chip>
                                    <v-chip color="teal lighten-2"  v-show="item.exp " label outlined>Expression  </v-chip>
                                    <v-chip color="teal lighten-2" v-show="item.cnv " label outlined>CNV </v-chip>
                                    <v-chip color="teal lighten-2"  v-show="item.meth " label outlined>Methylation </v-chip>

                                  </v-list-item-subtitle>
                                </v-list-item-content>


                              </v-list-item>
                            </v-list>
                          </v-sheet>
                        </v-col>
                      </v-row>

                    </v-col>
                    <v-col cols="6">
                      <v-row>
                        <v-col cols="12">
                          <v-sheet class="font-weight-bold">Summary of variants detected in multi-level data</v-sheet>

                        </v-col>
                        <v-col cols="12">
                          <v-divider></v-divider>
                        </v-col>
                        <v-col cols="12">
                          <v-sheet rounded class="pa-3 text-justify overflow-y-auto" color="grey lighten-3"  >
                            <v-list height="250" class="overflow-x-auto overflow-y-auto" color="grey lighten-3">
                              <v-list-item >
                                <v-list-item-icon>
                                  <v-icon color="teal">
                                    mdi-hexagon-slice-6
                                  </v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                  <v-list-item-title >
                                    Number of variants at SNV/Indels level: &nbsp; {{row.summary_snvindel}}
                                  </v-list-item-title>
                                </v-list-item-content>
                              </v-list-item>
                              <v-list-item >
                                <v-list-item-icon>
                                  <v-icon color="teal">
                                    mdi-hexagon-slice-6
                                  </v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                  <v-list-item-title >
                                    Number of variants at Expression level: &nbsp; {{row.summary_exp}}
                                  </v-list-item-title>
                                </v-list-item-content>
                              </v-list-item>
                              <v-list-item >
                                <v-list-item-icon>
                                  <v-icon color="teal">
                                    mdi-hexagon-slice-6
                                  </v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                  <v-list-item-title >
                                    Number of variants at CNV level: &nbsp; {{row.summary_cnv}}
                                  </v-list-item-title>
                                </v-list-item-content>
                              </v-list-item>
                              <v-list-item >
                                <v-list-item-icon>
                                  <v-icon color="teal">
                                    mdi-hexagon-slice-6
                                  </v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                  <v-list-item-title >
                                    Number of variants at Methylation level: &nbsp; {{row.summary_meth}}
                                  </v-list-item-title>
                                </v-list-item-content>
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
            <vxe-column field="DisplayName"  width="10%"  title="Display Name"></vxe-column>
            <vxe-column field="ID" sortable   width="10%" title="Reactome ID">
              <template #default="{row}">
                <a style="text-decoration: none" class="teal--text" :href=" $commonfunc.renderLinkReactome(row.ID )" target="_blank">{{ row.ID }}</a>
              </template>

            </vxe-column>
            <vxe-column show-overflow="tooltip"  width="55%" title="Description">

              <template #default="{row}">
                {{row.summation && row.summation[0] && row.summation[0].text}}
              </template>
            </vxe-column>
            <vxe-column field="ID"    width="5%" title="Has Variants at SNV/Indels level">
              <template #default="{row}">
                {{row.summary_snvindel && row.summary_snvindel > 0 ? "Yes":"No"}}
              </template>
            </vxe-column>
            <vxe-column field="ID"   width="5%" title="Has Variants at Expression level">
              <template #default="{row}">
                {{row.summary_exp && row.summary_exp > 0 ? "Yes":"No"}}
              </template>
            </vxe-column>
            <vxe-column field="ID"    width="5%" title="Has Variants at CNV level">
              <template #default="{row}">
                {{row.summary_cnv && row.summary_cnv > 0 ? "Yes":"No"}}
              </template>
            </vxe-column>
            <vxe-column field="ID"   width="5%" title="Has Variants at Methylation level">
              <template #default="{row}">
                {{row.summary_meth && row.summary_meth > 0 ? "Yes":"No"}}
              </template>
            </vxe-column>
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
          color="teal lighten-3" dark elevation="0" href="https://reactome.org/" small
          style="text-transform: none"
          target="_blank">Reactome
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>

</template>

<script>
import FilterPanel from "../sub/filterPanel";
import Axios from "axios";

export default {
name: "subOverviewPathway",
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
          DisplayName:null,
          ID:null,
          HAS_SNVINDEL:false,
          HAS_EXP:false,
          HAS_CNV:false,
          HAS_METH:false,

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
        "/ccas/api/get_overview_pathway_table_by_page",
        {},
        {
          params: {
            jobid: this.jobid,
            pageNumber: this.dat.tablePage1.currentPage,
            pageSize: this.dat.tablePage1.pageSize,
            ORDERBY:this.dat.tablePage1.ORDERBY,
            ORDERDESC:this.dat.tablePage1.ORDERDESC,
            DisplayName:this.dat.tablePage1.DisplayName,
            ID:this.dat.tablePage1.ID,
            HAS_SNVINDEL:this.dat.tablePage1.HAS_SNVINDEL,
            HAS_EXP:this.dat.tablePage1.HAS_EXP,
            HAS_CNV:this.dat.tablePage1.HAS_CNV,
            HAS_METH:this.dat.tablePage1.HAS_METH,

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
    'dat.tablePage1.DisplayName': function () {
      console.log("dat.tablePage1.DisplayName changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.ID': function () {
      console.log("dat.tablePage1.ID changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.HAS_SNVINDEL': function () {
      console.log("dat.tablePage1.HAS_SNVINDEL changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.HAS_EXP': function () {
      console.log("dat.tablePage1.HAS_EXP changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.HAS_CNV': function () {
      console.log("dat.tablePage1.HAS_CNV changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
    'dat.tablePage1.HAS_METH': function () {
      console.log("dat.tablePage1.HAS_METH changing...")
      // this.dat.filterQuery.symbol = true;
      this.debounceFilter()
    },
  }
}
</script>

<style scoped>

</style>
