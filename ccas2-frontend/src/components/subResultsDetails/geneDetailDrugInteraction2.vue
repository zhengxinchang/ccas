
<template>
  <v-sheet class="mx-3">
    <v-row align="end" class="pt-6">
      <v-col cols="12">
        <v-sheet height="650" >
          <vxe-toolbar ref="xToolbar1" custom export print></vxe-toolbar>
          <vxe-table
            ref="xTable1"
            :align="dat.allAlign"
            :column-config="{resizable: true}"
            :data="dat.tableData"
            :expand-config="{accordion:true}"
            :export-config="{}"
            :print-config="{}"
            :sort-config="{trigger:'cell'}"
            border
            max-height="600"
            empty-text="Empty"
            round
            stripe
          >
            <vxe-column  width="5%"  type="seq" title="#">
            </vxe-column>
            <vxe-column sortable width="20%" show-overflow="tooltip" field="prefName" title="Drug Name">
            </vxe-column>
            <vxe-column sortable width="10%" show-overflow="tooltip" field="drugType" title="Drug Types">
            </vxe-column>
            <vxe-column sortable width="10%" show-overflow="tooltip" field="drugId" title="Drug ID">
              <template #default="{row}">
                <a style="text-decoration: none"  class="teal--text" :href="$commonfunc.renderLinkChembl(row.drugId) " target="_blank">{{row.drugId}}</a>
              </template>
            </vxe-column>
            <vxe-column sortable width="15%" show-overflow="tooltip" field="mechanismOfAction" title="Mechanism">
            </vxe-column>
            <vxe-column sortable width="15%" show-overflow="tooltip" field="label" title="Disease Name">
            </vxe-column>
<!--            <vxe-column sortable width="5%" sort-type="number" show-overflow="tooltip"  field="phase" title="Phase">-->
<!--            </vxe-column>-->
            <vxe-column sortable width="25%"    title="Clinical Trials">
              <template #default="{ row }">

                <v-chip outlined small label dark color="teal" :href="nct.url" target="_blank" :key="name" v-for = "nct in ($commonfunc.drugs_nct_url2nct_name_url(row.NCTs) || [])" >
                  {{nct.name}}
                </v-chip>
<!--                {{ $commonfunc.drugs_nct_url2nct_name_url(row.NCTs)}}-->

              </template>
            </vxe-column>


          </vxe-table>

        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="2">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="platform.opentargets.org" small
          style="text-transform: none"
          target="_blank"> Open Target Platform
        </v-btn>
      </v-col>
    </v-row>

  </v-sheet>
</template>

<script>
// opentarget
import CommonHelpMessage from "../sub/commonHelpMessage";
export default {
name: "geneDetailDrugInteraction2",
  components: {CommonHelpMessage},
  props: ["tableData"],
  data() {
    return {
      dat: {
        tableData: [],
        allAlign: null,
        tablePage1: {
          currentPage: 1,
          pageSize: 10,
          totalPage: null,
        }
      }
    }
  },
  watch: {
    tableData: {
      handler: function () {

        this.dat.tableData = this.tableData
        this.dat.tablePage1.totalPage = this.tableData.length || 0
      },
      immediate: true,
      deep: true
    }

  },
  methods: {
    handlePageChange({currentPage, pageSize}) {
      this.dat.tablePage1.currentPage = currentPage
      this.dat.tablePage1.pageSize = pageSize
    },
  }
}
</script>

<style scoped>

</style>
