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
          <vxe-column  width="5%"  type="seq" title="#"></vxe-column>
          <vxe-column sortable width="25%" show-overflow="tooltip" field="title" title="Title">
            <template #default="{row}">
              <a style="text-decoration: none" class="teal--text" :href="$commonfunc.renderPubmed(row.pmid)" target="_blank"> {{row.title}}</a>
            </template>
          </vxe-column>
          <vxe-column sortable width="30%" show-overflow="tooltip" field="sentence" title="Sentence">
          </vxe-column>

          <vxe-column sortable width="10%"  show-overflow="tooltip" field="cancer_name" title="Cancer Name">
<!--            <template #header="{column}">-->
<!--              <span>{{ column.cancer_name }}</span><span><common-help-message>-->
<!--                  Common name of the cancer.-->
<!--                  </common-help-message></span>-->
<!--            </template>-->
          </vxe-column>
          <vxe-column sortable width="10%"  field="role" title="Role">
          </vxe-column>
          <vxe-column sortable width="10%"   title="Year">
            <template #default="{row}">
              {{row.year}}
            </template>
          </vxe-column>

          <vxe-column sortable width="10%"   title="Journal">
            <template #default="{row}">
              {{row.journal}}
            </template>
          </vxe-column>
        </vxe-table>
<!--        <vxe-pager-->
<!--          :current-page="dat.tablePage1.currentPage"-->
<!--          :layouts="['PrevPage', 'JumpNumber', 'NextPage', 'FullJump', 'Sizes', 'Total']"-->
<!--          :page-size="dat.tablePage1.pageSize"-->
<!--          :total="dat.tablePage1.totalPage"-->
<!--          @page-change="handlePageChange"-->
<!--        >-->
<!--        </vxe-pager>-->
        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="2">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="http://bionlp.bcgsc.ca/cancermine" small
          style="text-transform: none"
          target="_blank"> CancerMine
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import CommonHelpMessage from "../sub/commonHelpMessage";
export default {
  name: "geneDetailPapers",
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
