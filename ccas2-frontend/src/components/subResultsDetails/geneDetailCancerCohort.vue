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
            <vxe-column sortable width="20%" show-overflow="tooltip" field="CANCER_TYPE" title="Cancer Type">
            </vxe-column>
            <vxe-column sortable width="20%" show-overflow="tooltip" field="COHORT" title="Cohort Name">
            </vxe-column>
            <vxe-column sortable width="15%" show-overflow="tooltip" field="METHODS" title="Detection Method">
            </vxe-column>
            <vxe-column sortable width="10%" show-overflow="tooltip" field="ROLE"  title="Role">
              <template #header="{column}">
                <span>{{column.title}}</span> <span><common-help-message>Act: Activate<br/>Lof: Los of funcion<br/>ambiguous: unknown</common-help-message></span>
              </template>
            </vxe-column>
            <vxe-column sortable width="15%" sort-type="number"  show-overflow="tooltip" field="SAMPLES" title="#Samples">
            </vxe-column>
            <vxe-column sortable width="15%" sort-type="number" show-overflow="tooltip"  field="%_SAMPLES_COHORT" title="Percent of Cohorts(%)">
              <template #default="{row}">
                {{ $_.round(parseFloat( row['%_SAMPLES_COHORT']) * 100,4)}}

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
          color="teal lighten-3" dark elevation="0" href="https://www.intogen.org/" small
          style="text-transform: none"
          target="_blank"> DGIdb
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import CommonHelpMessage from "../sub/commonHelpMessage";
export default {
  name: "geneDetailCancerCohort",
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
