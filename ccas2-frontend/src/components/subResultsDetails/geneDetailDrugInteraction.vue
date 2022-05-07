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
            <vxe-column sortable width="15%" show-overflow="tooltip" field="drug_name" title="Drug Name">
            </vxe-column>
            <vxe-column sortable width="20%" show-overflow="tooltip" field="drug_claim_primary_name" title="Drug Claim Name">
            </vxe-column>
            <vxe-column sortable width="15%" show-overflow="tooltip" field="drug_concept_id" title="Drug ID">

              <template #default="{row}">
                <a style="text-decoration: none"  class="teal--text" :href="$commonfunc.renderLinkChembl(row.drug_concept_id.replace('chembl:','')) " target="_blank">{{row.drug_concept_id.replace('chembl:','')}}</a>
              </template>

            </vxe-column>
            <vxe-column sortable width="15%" show-overflow="tooltip" field="interaction_claim_source" title="Source">
            </vxe-column>
            <vxe-column sortable width="15%" show-overflow="tooltip" field="interaction_types" title="Interaction Types">
            </vxe-column>
            <vxe-column sortable width="15%" sort-type="number" show-overflow="tooltip"  field="interaction_group_score" title="Interaction Score">
            </vxe-column>


          </vxe-table>

        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="2">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://dgidb.genome.wustl.edu/" small
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
  name: "geneDetailDrugInteraction",
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
