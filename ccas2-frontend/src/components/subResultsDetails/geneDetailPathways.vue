<template>
  <v-sheet class="mx-3">
    <v-row align="end" class="pt-6">
      <v-col cols="12">

        <v-sheet height="650" >
          <vxe-toolbar ref="subpathway" custom export print  ></vxe-toolbar>
          <vxe-table
            ref="subpathway"
            :align="dat.allAlign"
            :loading="dat.tableloading1"
            :data="dat.tableData"
            :export-config="{}"
            :print-config="{}"
            border
            stripe
            max-height="600"
            empty-text="Empty"
            round
            :expand-config="{accordion:true}"
            :sort-config="{trigger:'cell'}"
            :column-config="{resizable: true}"
          >

            <vxe-column  width="5%"  type="seq" title="#"></vxe-column>
            <vxe-column sortable width="20%"  field="DisplayName" title="Display Name">
              <template #header="{column}">
                <span>{{ column.title }}</span><span><common-help-message>
                    Brief name of the pathway
                  </common-help-message></span>
              </template>
            </vxe-column>

            <vxe-column sortable width="10%"   field="ID" title="Reactome ID">
                <template #default="{row}">
                  <a style="text-decoration: none"  class="teal--text" :href="$commonfunc.renderLinkReactome(row.ID) " target="_blank">{{row.ID}}</a>

                </template>
            </vxe-column>

            <vxe-column sortable width="10%"  type="expand" show-overflow="tooltip"  title="#Literature of the pathway">
              <template #default="{row}" >
                {{ row.literatureReference.length || 0 }}
              </template>
              <template #content="{ row, rowIndex }">

                <v-row class="pa-3">
                  <v-col>
                    <vxe-table
                      border
                      stripe
                      height="400"
                      round
                      :data="row.literatureReference"
                      ref="subpathwayPaper"
                    >
                      <vxe-column field="title" width="50%" title="Title">
                        <template #default = "{row}" >
                          <a style="text-decoration: none" :href="row.url" target="_blank">{{row.title}}</a>


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
                  </v-col>

                </v-row >


              </template>
            </vxe-column>

            <vxe-column sortable width="55%"  show-overflow="tooltip" title="Description">
              <template #header="{column}">
                <span>{{ column.title }}</span><span><common-help-message>
                      Brief Descritption of this pathway
                    </common-help-message></span>
              </template>
              <template #default="{row}" >
                {{ row.summation[0].text }}
              </template>
            </vxe-column>


          </vxe-table>
<!--          <vxe-pager-->
<!--            ref="subpathway"-->
<!--            :current-page="dat.tablePage1.currentPage"-->
<!--            :layouts="['PrevPage', 'JumpNumber', 'NextPage', 'FullJump', 'Sizes', 'Total']"-->
<!--            :loading="dat.tableloading1"-->
<!--            :page-size="dat.tablePage1.pageSize"-->
<!--            :total="dat.tablePage1.totalPage"-->
<!--            @page-change="handlePageChange2"-->
<!--          >-->
<!--          </vxe-pager>-->
        </v-sheet>

      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="2">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://reactome.org/" small style="text-transform: none"
          target="_blank"> Reactome
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import CommonHelpMessage from "../sub/commonHelpMessage";
export default {
name: "geneDetailPathways",
  components: {CommonHelpMessage},
  props:["tableData"],
  data(){
    return{
        dat:{
          tableloading1:false,
          tableData:[],
          allAlign:null,
          tablePage1:{
            currentPage:1,
            pageSize:10,
            totalPage:null,
          }
        }
    }
  },
  watch:{
    tableData:{
      handler:function () {
        console.log(this.tableData)
        this.dat.tableData = this.tableData
        this.dat.tablePage1.totalPage = this.tableData.length || 0

      },
      immediate:true,
      deep:true
    }

  },
  methods:{
    handlePageChange2({currentPage, pageSize}){
      this.dat.tablePage1.currentPage = currentPage
      this.dat.tablePage1.pageSize = pageSize
    },
  }
}
</script>

<style scoped>

</style>
