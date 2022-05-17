<template>

  <v-container class="container--fluid">
    <v-sheet class="z-transparent" style="margin-top: 120px;"></v-sheet>
    <v-row align="center">
      <v-col cols="12">
        <v-sheet class="px4 mx-6" max-height="60" min-height="60" rounded>
          <v-row align="center" dense>
            <v-col>
              <v-breadcrumbs
                :items="[{text:'home',disabled:false,to:'/home'},{text:'check results',disabled:false,to:'/checkresults'},{text:'results',disabled:true}]"></v-breadcrumbs>
            </v-col>
          </v-row>

        </v-sheet>
      </v-col>
    </v-row>
    <!--    导航条结束-->
    <!--    下边开始overview的内容-->
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
                Overview
              </v-toolbar-title>
            </v-toolbar>
            <v-tabs class="text-start text-body-2 px-3  mt-3" color="teal" grow>
              <!--              取消把字体都转换为大写-->

              <v-tab style="text-transform: none">
                <v-icon left>
                  mdi-label-multiple
                </v-icon>
                Job & Disease overview
              </v-tab>
              <v-tab style="text-transform: none">
                <v-icon left>
                  mdi-label-multiple
                </v-icon>
                Mutation signature
              </v-tab>
              <v-tab style="text-transform: none">
                <v-icon left>
                  mdi-label-multiple
                </v-icon>
                ssGSEA
              </v-tab>
              <v-tab style="text-transform: none">
                <v-icon left>
                  mdi-label-multiple
                </v-icon>
                Clinical trials
              </v-tab>
              <v-tab style="text-transform: none">
                <v-icon left>
                  mdi-label-multiple
                </v-icon>
                Pathways
              </v-tab>

              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <!--                    overview disease overview-->
                    <!--                    每个overview的tabitem是一个独立的component-->
                    <sub-overview-disease-overview :dat="dat.overview.diseaseOverview"></sub-overview-disease-overview>
                  </v-card-text>
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <sub-overview-mut-signature :jobid="$route.params.jobid"></sub-overview-mut-signature>
                  </v-card-text>
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <sub-overview-s-s-g-s-e-a :jobid="$route.params.jobid"></sub-overview-s-s-g-s-e-a>
                  </v-card-text>
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <sub-overview-clinical-trials :jobid="$route.params.jobid"></sub-overview-clinical-trials>
                  </v-card-text>
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <sub-overview-pathway :jobid="$route.params.jobid"></sub-overview-pathway>
                  </v-card-text>
                </v-card>
              </v-tab-item>

            </v-tabs>
          </v-card>

        </v-sheet>

      </v-col>
    </v-row>
    <!--    往下是gene annotation table-->
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
                Annotation Gene Table
              </v-toolbar-title>
            </v-toolbar>
            <v-sheet class="pa-3" rounded>
              <v-sheet class="pt-6  px-3 pb-6">
                <!--                下边是筛选-->
                <!--                filter-panel是控制折叠的panel。里边slot是具体筛选的逻辑-->
                <filter-panel #default="{ isexpand}">
                  <v-sheet v-show="isexpand" class="py-6" color="grey lighten-4">
                    <!--                    filter的内容-->
                    <v-row class="mx-3 pt-3">
                      <v-col class="text-left">
                        <v-sheet class="text-left" color="grey lighten-4 teal--text font-weight-bold">Basic Filters
                        </v-sheet>
                        <v-divider></v-divider>
                      </v-col>
                    </v-row>
                    <v-row class="mx-3 pt-3">
                      <v-col cols="3">
                        <v-text-field
                          v-model="dat.tablePage1.SYMBOL"
                          background-color="white"

                          clearable
                          color="teal" dense hide-details label="Symbol" outlined
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="3">
                        <v-text-field
                          v-model="dat.tablePage1.NAME"
                          background-color="white"
                          clearable
                          color="teal" dense hide-details label="Gene Name" outlined
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="3">
                        <v-text-field
                          v-model="dat.tablePage1.ENSGID"
                          background-color="white"

                          clearable
                          color="teal" dense hide-details label="Ensembl ID" outlined

                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="3">

                        <v-select

                          v-model="dat.tablePage1.LOUCSTYPE"
                          :items="dat.tablePage1.LOCUSTYPE_RUNTIME"
                          background-color="white"

                          clearable
                          color="teal"
                          dense hide-details label="Locus Type" outlined
                        >

                        </v-select>
                      </v-col>
                    </v-row>
                    <v-row class="mx-3 pt-3">
                      <v-col class="text-left">
                        <v-sheet class="text-left" color="grey lighten-4 teal--text font-weight-bold">
                          Advance Filters
                          <v-icon v-show="dat.expandAdvanceFilter ==false" color="teal" small
                                  @click="dat.expandAdvanceFilter =true">mdi-chevron-double-down
                          </v-icon>
                          <v-icon v-show="dat.expandAdvanceFilter ==true" color="teal" small
                                  @click="dat.expandAdvanceFilter =false">mdi-chevron-double-up
                          </v-icon>
                        </v-sheet>
                        <v-divider></v-divider>
                      </v-col>
                    </v-row>
                    <v-sheet v-show="dat.expandAdvanceFilter" color="grey lighten-4">


                      <v-row class="mx-3 pt-3">
                        <v-col class="text-left" cols="3">
                          <v-switch v-model="dat.tablePage1.FilterSNV" class="font-weight-bold float-start" color="teal"
                                    inset
                                    label="Filter data at SNV/Indels level"></v-switch>
                          <common-help-message class="float-left">When this button is turned on, all genes with SNV /
                            indels level variation will be selected by default.
                          </common-help-message>
                        </v-col>
                      </v-row>
                      <v-row dense>
                        <v-col cols="10" offset="1">
                          <v-expansion-panels :value="0" flat>
                            <v-expansion-panel>
                              <v-expansion-panel-header color="grey lighten-4 font-weight-bold ">
                                <v-sheet color="grey lighten-4">
                                  IMPACT　& Consequence
                                  <common-help-message class="float-left">The IMPACT and Consequence of SNV/Indels are
                                    filtered here. CCAS uses the VEP criteria to classify the variants.
                                  </common-help-message>
                                </v-sheet>

                              </v-expansion-panel-header>
                              <v-expansion-panel-content color="grey lighten-4">
                                <!--                    HIGH IMPACT-->
                                <v-row align="center" dense>
                                  <v-col cols="2" offset="1">
                                    <v-sheet color="grey lighten-4  font-weight-bold">

                                      <v-checkbox
                                        v-model="dat.tablePage1.SNVsubFilter.impact.HIGH.mark"
                                        :disabled="!dat.tablePage1.FilterSNV "
                                        color="teal"
                                        label="HIGH IMPACT"
                                      ></v-checkbox>
                                    </v-sheet>
                                  </v-col>
                                  <v-col cols="10" offset="2">
                                    <v-row dense>
                                      <v-col v-for="item in Object.keys(dat.tablePage1.SNVsubFilter.impact.HIGH.consequence) "
                                             :key="item"
                                             cols="4"
                                      >
                                        <v-checkbox
                                          v-model="dat.tablePage1.SNVsubFilter.impact.HIGH.consequence[item].value"
                                          :disabled="!dat.tablePage1.FilterSNV "
                                          :label="`${item.replace('consequence_','')}`"
                                          color="teal"
                                          dense
                                        ></v-checkbox>
                                      </v-col>
                                    </v-row>
                                  </v-col>
                                </v-row>
                                <!--                    MODERATE-->
                                <v-row align="center" dense>
                                  <v-col cols="2" offset="1">
                                    <v-sheet color="grey lighten-4  font-weight-bold">

                                      <v-checkbox
                                        v-model="dat.tablePage1.SNVsubFilter.impact.MODERATE.mark"
                                        :disabled="!dat.tablePage1.FilterSNV "
                                        color="teal"
                                        label="MODERATE IMPACT"
                                      ></v-checkbox>
                                    </v-sheet>
                                  </v-col>
                                  <v-col cols="10" offset="2">
                                    <v-row dense>
                                      <v-col v-for="item in Object.keys(dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence) "
                                             :key="item"
                                             cols="4"
                                      >
                                        <v-checkbox
                                          v-model="dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence[item].value"
                                          :disabled="!dat.tablePage1.FilterSNV "
                                          :label="`${item.replace('consequence_','')}`"
                                          color="teal"
                                          dense
                                        ></v-checkbox>
                                      </v-col>
                                    </v-row>
                                  </v-col>
                                </v-row>
                                <!--                    LOW-->
                                <v-row align="center" dense>
                                  <v-col cols="2" offset="1">
                                    <v-sheet color="grey lighten-4  font-weight-bold">

                                      <v-checkbox
                                        v-model="dat.tablePage1.SNVsubFilter.impact.LOW.mark"
                                        :disabled="!dat.tablePage1.FilterSNV "
                                        color="teal"
                                        dense
                                        label="LOW IMPACT"
                                      ></v-checkbox>
                                    </v-sheet>
                                  </v-col>
                                  <v-col cols="10" offset="2">
                                    <v-row dense>
                                      <v-col v-for="item in Object.keys(dat.tablePage1.SNVsubFilter.impact.LOW.consequence) "
                                             :key="item"
                                             cols="4"
                                      >
                                        <v-checkbox
                                          v-model="dat.tablePage1.SNVsubFilter.impact.LOW.consequence[item].value"

                                          :disabled="!dat.tablePage1.FilterSNV "
                                          :label="`${item.replace('consequence_','')}`"
                                          color="teal"
                                          dense
                                        ></v-checkbox>
                                      </v-col>
                                    </v-row>
                                  </v-col>
                                </v-row>
                                <!--                    MODIFIER-->
                                <v-row align="center" dense>
                                  <v-col cols="2" offset="1">
                                    <v-sheet color="grey lighten-4  font-weight-bold">

                                      <v-checkbox
                                        v-model="dat.tablePage1.SNVsubFilter.impact.MODIFIER.mark"
                                        :disabled="!dat.tablePage1.FilterSNV "
                                        color="teal"
                                        label="MODIFIER IMPACT"
                                      ></v-checkbox>
                                    </v-sheet>
                                  </v-col>
                                  <v-col cols="10" offset="2">
                                    <v-row dense>
                                      <v-col v-for="item in Object.keys(dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence) "
                                             :key="item"
                                             cols="4"
                                      >
                                        <v-checkbox
                                          v-model="dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence[item].value"
                                          :disabled="!dat.tablePage1.FilterSNV "
                                          :label="`${item.replace('consequence_','')}`"
                                          color="teal"
                                        ></v-checkbox>
                                      </v-col>
                                    </v-row>
                                  </v-col>
                                </v-row>

                              </v-expansion-panel-content>
                            </v-expansion-panel>
                          </v-expansion-panels>
                        </v-col>
                      </v-row>
                      <v-row class="mx-3 pt-3">
                        <v-col class="text-left">
                          <v-switch v-model="dat.tablePage1.FilterEXP" class="font-weight-bold float-start" color="teal"
                                    inset
                                    label="Filter data at Expression level"

                          ></v-switch>
                          <common-help-message class="float-left">When this button is turned on, all genes with
                            Expression level abnormalities will be selected by default. The max and min value of the
                            slider are depend on the max and min value in the expression level file which user uploaded.
                          </common-help-message>
                        </v-col>
                      </v-row>
                      <v-row dense>
                        <v-col cols="10" offset="1">
                          <v-sheet>
                            <v-range-slider
                              v-model="dat.tablePage1.ExpsubFilter.range" :disabled="! dat.tablePage1.FilterEXP"
                              :max="dat.tablePage1.ExpsubFilter.setmax"
                              :min="dat.tablePage1.ExpsubFilter.setmin"
                              background-color="grey lighten-2"
                              class="align-center"
                              color="teal"
                              dark
                              step="0.05"
                              hide-details
                              thumb-color="teal lighten-1"
                              thumb-label
                            >
                            </v-range-slider>
                          </v-sheet>

                        </v-col>
                      </v-row>
                      <v-row class="mx-3 pt-3">
                        <v-col class="text-left">
                          <v-switch v-model="dat.tablePage1.FilterCNV" class="font-weight-bold float-start" color="teal"
                                    inset label="Filter data at CNV level"></v-switch>
                          <common-help-message class="float-left">When this button is turned on, all genes with CNV
                            level abnormalities will be selected by default. The max and min value of the slider are
                            depend on the max and min value in the CNV level file which user uploaded.
                          </common-help-message>
                        </v-col>
                      </v-row>
                      <v-row dense>
                        <v-col cols="10" offset="1">
                          <v-sheet>
                            <v-range-slider
                              v-model="dat.tablePage1.CNVsubFilter.range" :disabled="! dat.tablePage1.FilterCNV"
                              :max="dat.tablePage1.CNVsubFilter.setmax"
                              :min="dat.tablePage1.CNVsubFilter.setmin"
                              background-color="grey lighten-2"
                              class="align-center"
                              color="teal"
                              dark
                              hide-details
                              thumb-color="teal lighten-1"
                              thumb-label
                              step="0.05"
                            >
                            </v-range-slider>
                          </v-sheet>

                        </v-col>
                      </v-row>
                      <v-row class="mx-3 pt-3">
                        <v-col class="text-left">
                          <v-switch v-model="dat.tablePage1.FilterMETH" class="font-weight-bold float-start" color="teal"
                                    inset
                                    label="Filter data at Methylation level"></v-switch>
                          <common-help-message class="float-left">When this button is turned on, all genes with
                            Methylation level abnormalities will be selected by default. The max and min value of the
                            slider are depend on the max and min value in the Methylation level file which user
                            uploaded.
                          </common-help-message>
                        </v-col>
                      </v-row>
                      <v-row dense>
                        <v-col cols="10" offset="1">
                          <v-sheet>
                            <v-range-slider
                              v-model="dat.tablePage1.MethsubFilter.range" :disabled="! dat.tablePage1.FilterMETH"
                              :max="dat.tablePage1.MethsubFilter.setmax"
                              :min="dat.tablePage1.MethsubFilter.setmin"
                              background-color="grey lighten-2"
                              class="align-center"
                              color="teal"

                              step="0.05"
                              dark
                              hide-details
                              thumb-color="teal lighten-1"
                              thumb-label
                            >
                            </v-range-slider>
                          </v-sheet>

                        </v-col>
                      </v-row>
                      <v-row class="mx-3 pt-3" dense>
                        <v-spacer>
                        </v-spacer>
                        <v-col cols="2">
                          <v-btn color="teal" dark small style="text-transform: none" width="80%" @click="resetFilters">
                            Reset
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-sheet>
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
                <!--                :sort-config="{sortMethod:customSortMethod}"-->
                <!--                :sort-config="{sortMethod:customSortMethod,remote:true}"-->
                <vxe-column field="symbol" sortable title="Symbol"></vxe-column>
                <vxe-column field="name" sortable title="Name"></vxe-column>
                <vxe-column sortable title="ID">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    This id is generated by using Ensembl id with prefix 'GENEID:'
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">

                    <a class="font-weight-bold" style="text-decoration: none;color: #008080"
                       @click="$router.push({name:'genedetail',params:{jobid:$route.params.jobid,geneid:row.geneid}})">

                      {{ row.geneid }}
                    </a>

                  </template>

                </vxe-column>
                <vxe-column field="genefamily" sortable title="Gene Family"></vxe-column>
                <vxe-column field="location" sortable title="Location"></vxe-column>
                <vxe-column field="locus_type" sortable title="Locus Type"></vxe-column>
                <vxe-column align="center" field="numofsnvindel" sortable title="#SNV/indels">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    Number of SNVs or Indels detected in user uploaded file in this gene
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofsnvindel == 0?'grey': 'teal' " dark label samll>{{ row.numofsnvindel }}
                    </v-chip>
                  </template>
                </vxe-column>
                <vxe-column align="center" field="numofexp" sortable title="#Expression">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    This gene was detected in Expression file that user uploaded.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofexp == 0?'grey': 'teal' " dark label samll>{{ row.numofexp }}</v-chip>
                  </template>
                </vxe-column>
                <vxe-column align="center" field="numofcnv" sortable title="#CNV">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    This gene was detected in CNV file that user uploaded.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofcnv == 0?'grey': 'teal' " dark label samll>{{ row.numofcnv }}</v-chip>
                  </template>
                </vxe-column>
                <vxe-column align="center" field="numofmeth" sortable title="#Methylation">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    This gene was detected in Methylation file that user uploaded.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofmeth == 0?'grey': 'teal' " dark label samll>{{ row.numofmeth }}</v-chip>
                  </template>
                </vxe-column>
                <vxe-column align="center" field="numofdpathway" sortable title="#Pathways of this gene">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    Number of Pathways that have this gene.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofdpathway == 0?'grey': 'teal' " dark label samll>{{ row.numofdpathway }}
                    </v-chip>
                  </template>
                </vxe-column>

                <vxe-column align="center" field="numofcancer" sortable title="#Cancer cohorts have variants in this gene">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    Number of cancer cohorts that have variants in this gene.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofcancer == 0?'grey': 'teal' " dark label samll>{{ row.numofcancer }}
                    </v-chip>
                  </template>
                </vxe-column>

                <vxe-column align="center" field="numofpaper" sortable title="#Publications of this gene">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    Number of Publications assocated with this gene.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofpaper == 0?'grey': 'teal' " dark label samll>{{ row.numofpaper }}</v-chip>
                  </template>
                </vxe-column>
                <vxe-column align="center" field="numofdruginteraction" sortable
                            title="#Drug interactions of this gene">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    Number of Drug interactions of this gene.
                  </common-help-message></span>
                  </template>
                  <template #default="{row}">
                    <v-chip :color="row.numofdruginteraction == 0?'grey': 'teal' " dark label samll>
                      {{ row.numofdruginteraction }}
                    </v-chip>
                  </template>
                </vxe-column>
                <vxe-column title="Detail">
                  <template #header="{column}">
                    <span>{{ column.title }}</span><span><common-help-message>
                    View gene details by click 'Detail' in each row.
                  </common-help-message></span>
                  </template>
                  <template #default="{ row }">
                    <v-btn class="font-weight-bold" color="teal" dark outlined small style="text-transform: none"
                           @click="$router.push({name:'genedetail',params:{jobid:$route.params.jobid,geneid:row.geneid}})">
                      View
                    </v-btn>
                  </template>
                </vxe-column>
                <!--                @click="$router.push({name:'/annoresults/genedetail',params:{jobid:$route.params.jobid,geneid:row.geneid}})"-->


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
          </v-card>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Axios from 'axios'
import qs from 'qs'
import SubOverviewDiseaseOverview from "./subResults/subOverviewDiseaseOverview";
import filterPanel from "./sub/filterPanel";
import CommonHelpMessage from "./sub/commonHelpMessage";
import _ from 'lodash'
import SubOverviewClinicalTrials from "./subResults/subOverviewClinicalTrials";
import SubOverviewPathway from "./subResults/subOverviewPathway";
import SubOverviewMutSignature from "./subResults/subOverviewMutSignature";
import SubOverviewSSGSEA_echarts_bar from "./subResults/subOverviewSSGSEA_echarts_bar";
import SubOverviewSSGSEA from "./subResults/subOverviewSSGSEA";

export default {
  name: "annoresults",
  components: {
    SubOverviewSSGSEA,
    SubOverviewSSGSEA_echarts_bar,
    SubOverviewMutSignature,
    SubOverviewPathway, SubOverviewClinicalTrials, CommonHelpMessage, SubOverviewDiseaseOverview, filterPanel
  },
  data() {
    return {
      dat: {
        overview: {
          diseaseOverview: null,
        },
        expandAdvanceFilter: false,
        allAlign: null,
        tableData: [],
        tableloading1: false,
        tablePage1: {
          currentPage: 1,
          pageSize: 10,
          ENSGID: null,
          SYMBOL: null,
          LOUCSTYPE: null,
          ORDERBY: "symbol",
          ORDERDESC: true, //如果有值，则是DESC
          NAME: null,
          LOCUSTYPE_RUNTIME: [],
          FilterSNV: false,
          FilterEXP: false,
          FilterCNV: false,
          FilterMETH: false,
          SNVsubFilterShowConsequenceSelectAll: true,
          SNVsubFilter: {
            impact: {
              HIGH: {
                mark: true,
                consequence: {
                  consequence_transcript_ablation: {impact: "HIGH", value: true},
                  consequence_splice_acceptor_variant: {impact: "HIGH", value: true},
                  consequence_splice_donor_variant: {impact: "HIGH", value: true},
                  consequence_stop_gained: {impact: "HIGH", value: true},
                  consequence_frameshift_variant: {impact: "HIGH", value: true},
                  consequence_stop_lost: {impact: "HIGH", value: true},
                  consequence_start_lost: {impact: "HIGH", value: true},
                }
              },  //这里设置为true则表示，包括这部分数据，不加filter，如果为f，则添加筛选条件 HIGH = 0
              LOW: {
                mark: true,
                consequence: {
                  consequence_splice_region_variant: {impact: "LOW", value: true},
                  consequence_incomplete_terminal_codon_variant: {impact: "LOW", value: true},
                  consequence_start_retained_variant: {impact: "LOW", value: true},
                  consequence_stop_retained_variant: {impact: "LOW", value: true},
                  consequence_synonymous_variant: {impact: "LOW", value: true},
                }
              },
              MODERATE: {
                mark: true,
                consequence: {
                  consequence_inframe_insertion: {impact: "MODERATE", value: true},
                  consequence_inframe_deletion: {impact: "MODERATE", value: true},
                  consequence_missense_variant: {impact: "MODERATE", value: true},
                  consequence_protein_altering_variant: {impact: "MODERATE", value: true},
                }
              },
              MODIFIER: {
                mark: true,
                consequence: {
                  consequence_coding_sequence_variant: {impact: "MODIFIER", value: true},
                  consequence_mature_miRNA_variant: {impact: "MODIFIER", value: true},
                  consequence_5_prime_UTR_variant: {impact: "MODIFIER", value: true},
                  consequence_3_prime_UTR_variant: {impact: "MODIFIER", value: true},
                  consequence_non_coding_transcript_exon_variant: {impact: "MODIFIER", value: true},
                  consequence_intron_variant: {impact: "MODIFIER", value: true},
                  consequence_NMD_transcript_variant: {impact: "MODIFIER", value: true},
                  consequence_non_coding_transcript_variant: {impact: "MODIFIER", value: true},
                  consequence_upstream_gene_variant: {impact: "MODIFIER", value: true},
                  consequence_downstream_gene_variant: {impact: "MODIFIER", value: true},
                  consequence_TFBS_ablation: {impact: "MODIFIER", value: true},
                  consequence_TFBS_amplification: {impact: "MODIFIER", value: true},
                  consequence_TF_binding_site_variant: {impact: "MODIFIER", value: true},
                  consequence_regulatory_region_ablation: {impact: "MODIFIER", value: true},
                  consequence_regulatory_region_amplification: {impact: "MODIFIER", value: true},
                  consequence_feature_elongation: {impact: "MODIFIER", value: true},
                  consequence_regulatory_region_variant: {impact: "MODIFIER", value: true},
                  consequence_feature_truncation: {impact: "MODIFIER", value: true},
                  consequence_intergenic_variant: {impact: "MODIFIER", value: true},
                }
              }
            },
            // consequence:{
            //   consequence_transcript_ablation:true,
            //   consequence_splice_acceptor_variant:true,
            //   consequence_splice_donor_variant:true,
            //   consequence_stop_gained:true,
            //   consequence_frameshift_variant:true,
            //   consequence_stop_lost:true,
            //   consequence_start_lost:true,
            //   consequence_transcript_amplification:true,
            //   consequence_inframe_insertion:true,
            //   consequence_inframe_deletion:true,
            //   consequence_missense_variant:true,
            //   consequence_protein_altering_variant:true,
            //   consequence_splice_region_variant:true,
            //   consequence_incomplete_terminal_codon_variant:true,
            //   consequence_start_retained_variant:true,
            //   consequence_stop_retained_variant:true,
            //   consequence_synonymous_variant:true,
            //   consequence_coding_sequence_variant:true,
            //   consequence_mature_miRNA_variant:true,
            //   consequence_5_prime_UTR_variant:true,
            //   consequence_3_prime_UTR_variant:true,
            //   consequence_non_coding_transcript_exon_variant:true,
            //   consequence_intron_variant:true,
            //   consequence_NMD_transcript_variant:true,
            //   consequence_non_coding_transcript_variant:true,
            //   consequence_upstream_gene_variant:true,
            //   consequence_downstream_gene_variant:true,
            //   consequence_TFBS_ablation:true,
            //   consequence_TFBS_amplification:true,
            //   consequence_TF_binding_site_variant:true,
            //   consequence_regulatory_region_ablation:true,
            //   consequence_regulatory_region_amplification:true,
            //   consequence_feature_elongation:true,
            //   consequence_regulatory_region_variant:true,
            //   consequence_feature_truncation:true,
            //   consequence_intergenic_variant:true,
            // }
          },

          ExpsubFilter: {
            setmax: 0,
            setmin: 100,
            range: [0, 0],
          },
          CNVsubFilter: {
            setmax: 100,
            setmin: 0,
            range: [0, 0],
          },
          MethsubFilter: {
            setmax: 100,
            setmin: 0,
            range: [0, 0],
          },
          totalPage: null,
        },

      }
    }
  },
  watch: {
    '$route.params.jobid': {
      handler: function (jobid) {

        // 这里开始load结果
        // disease overview
        Axios.post(
          "/ccas/api/get_overview_disease_ontology",
          {},
          {
            params: {
              jobid: jobid
            }
          }
        ).then(res => {
          this.dat.overview.diseaseOverview = res.data.data
        })

        this.loadDataByPage()

      },
      deep: true,
      immediate: true
    },

    'dat.tablePage1.FilterSNV': function (val) {
      console.log("dat.tablePage1.FilterSNV changing...")
      if (val == false) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.HIGH.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.HIGH.consequence[x].value = true
        }
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence[x].value = true
        }
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.LOW.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.LOW.consequence[x].value = true
        }
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence[x].value = true
        }
      }

      this.debounceFilter()
    },

    'dat.tablePage1.SNVsubFilter': {
      handler: function () {
        this.debounceFilter()
      },
      deep: true,
      immediate: true,
    },

    'dat.tablePage1.FilterCNV': function (val) {
      console.log("dat.tablePage1.FilterCNV changing...")

      if (val == true) {
        this.dat.tablePage1.CNVsubFilter.range = [
          this.dat.tablePage1.CNVsubFilter.setmin,
          this.dat.tablePage1.CNVsubFilter.setmax,
        ]
      }

      this.debounceFilter()
    },

    'dat.tablePage1.CNVsubFilter.range': {
      handler: function (val) {

        if (isNaN(val[0]) || isNaN(val[1])) {
          this.dat.tablePage1.CNVsubFilter.range = [
            0,
            0
          ]
        } else {
          this.debounceFilter()
        }
        console.log("dat.tablePage1.CNVsubFilter changing...")

      },
      deep: true,
      immediate: true,
    },

    'dat.tablePage1.FilterEXP': function (val) {
      console.log("dat.tablePage1.FilterEXP changing..." + val)

      if (val == true) {
        this.dat.tablePage1.ExpsubFilter.range = [
          isNaN(this.dat.tablePage1.ExpsubFilter.setmin) ? 0 : this.dat.tablePage1.ExpsubFilter.setmin,
          isNaN(this.dat.tablePage1.ExpsubFilter.setmax) ? 0 : this.dat.tablePage1.ExpsubFilter.setmax,
        ]
      }
      this.debounceFilter()
    },

    'dat.tablePage1.ExpsubFilter.range': {
      handler: function (val) {

        if (isNaN(val[0]) || isNaN(val[1])) {
          this.dat.tablePage1.ExpsubFilter.range = [
            0,
            0
          ]
        } else {
          this.debounceFilter()
        }
        console.log("dat.tablePage1.ExpsubFilter changing..." + val)

      },
      deep: true,
      immediate: true,
    },

    'dat.tablePage1.FilterMETH': function (val) {
      console.log("dat.tablePage1.FilterMETH changing...")

      if (val == true) {
        this.dat.tablePage1.MethsubFilter.range = [
          this.dat.tablePage1.MethsubFilter.setmin,
          this.dat.tablePage1.MethsubFilter.setmax,
        ]
      }
      this.debounceFilter()
    },

    'dat.tablePage1.MethsubFilter.range':
      {
        handler: function (val) {

          if (isNaN(val[0]) || isNaN(val[1])) {
            this.dat.tablePage1.MethsubFilter.range = [
              0,
              0
            ]
          } else {
            this.debounceFilter()
          }
          console.log("dat.tablePage1.MethsubFilter changing..." + val)

        },
        deep: true,
        immediate: true,
      },

    'dat.tablePage1.SYMBOL': function () {
      console.log("dat.tablePage1.SYMBOL changing...")
      this.debounceFilter()
    },
    'dat.tablePage1.ENSGID': function () {
      console.log("dat.tablePage1.ENSGID changing...")
      this.debounceFilter()
    },
    'dat.tablePage1.NAME': function () {
      console.log("dat.tablePage1.NAME changing...")
      this.debounceFilter()
    },
    'dat.tablePage1.LOUCSTYPE': {
      handler: function () {

        console.log("dat.tablePage1.LOUCSTYPE changing...")
        this.debounceFilter()
      },
      deep: true,
      immediate: true,


    },
    "dat.tablePage1.SNVsubFilter.impact.HIGH.mark": function (val) {
      if (val == false) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.HIGH.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.HIGH.consequence[x].value = false
        }
      } else if (val == true) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.HIGH.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.HIGH.consequence[x].value = true
        }
      }
    },
    "dat.tablePage1.SNVsubFilter.impact.MODERATE.mark": function (val) {
      if (val == false) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence[x].value = false
        }
      } else if (val == true) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.MODERATE.consequence[x].value = true
        }
      }
    },
    "dat.tablePage1.SNVsubFilter.impact.LOW.mark": function (val) {
      if (val == false) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.LOW.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.LOW.consequence[x].value = false
        }
      } else if (val == true) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.LOW.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.LOW.consequence[x].value = true
        }
      }
    },
    "dat.tablePage1.SNVsubFilter.impact.MODIFIER.mark": function (val) {
      if (val == false) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence[x].value = false
        }
      } else if (val == true) {
        for (let x in this.dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence) {
          this.dat.tablePage1.SNVsubFilter.impact.MODIFIER.consequence[x].value = true
        }
      }
    },

  },

  methods: {
    handlePageChange({currentPage, pageSize}) {
      this.dat.tablePage1.currentPage = currentPage
      this.dat.tablePage1.pageSize = pageSize
      this.loadDataByPage()
    },
    loadDataByPage() {
      this.dat.tableloading1 = true
      Axios.post(
        "/ccas/api/get_gene_anno_table_by_page_filters",
        {},
        {
          params: {
            jobid: this.$route.params.jobid,
            pageNumber: this.dat.tablePage1.currentPage,
            pageSize: this.dat.tablePage1.pageSize,
            ENSGID: this.dat.tablePage1.ENSGID,
            SYMBOL: this.dat.tablePage1.SYMBOL,
            LOUCSTYPE: this.dat.tablePage1.LOUCSTYPE,
            ORDERBY: this.dat.tablePage1.ORDERBY,
            ORDERDESC: this.dat.tablePage1.ORDERDESC, //如果有值，则是DESC
            NAME: this.dat.tablePage1.NAME,
            IS_FILTER_SNV: this.dat.tablePage1.FilterSNV,
            IS_FILTER_CNV: this.dat.tablePage1.FilterCNV,
            IS_FILTER_EXP: this.dat.tablePage1.FilterEXP,
            IS_FILTER_METH: this.dat.tablePage1.FilterMETH,
            FILTER_SNV_CUTOFF: JSON.stringify({
              IMPACT: this.dat.tablePage1.SNVsubFilter.impact
            }),
            FILTER_EXP_CUTOFF: JSON.stringify(
              this.dat.tablePage1.ExpsubFilter.range
            ),
            FILTER_CNV_CUTOFF: JSON.stringify(
              this.dat.tablePage1.CNVsubFilter.range
            ),
            FILTER_METH_CUTOFF: JSON.stringify(
              this.dat.tablePage1.MethsubFilter.range
            ),
          }
        }
      ).then(res => {
        this.dat.tableData = res.data.data
        this.dat.tablePage1.totalPage = res.data.count.count;
        this.dat.tablePage1.LOCUSTYPE_RUNTIME = res.data.unique_locus_type;
        this.dat.tablePage1.ExpsubFilter.setmax = res.data.MaxMin.max_exp_value
        this.dat.tablePage1.ExpsubFilter.setmin = res.data.MaxMin.min_exp_value
        this.dat.tablePage1.CNVsubFilter.setmax = res.data.MaxMin.max_cnv_value
        this.dat.tablePage1.CNVsubFilter.setmin = res.data.MaxMin.min_cnv_value
        this.dat.tablePage1.MethsubFilter.setmax = res.data.MaxMin.max_meth_value
        this.dat.tablePage1.MethsubFilter.setmin = res.data.MaxMin.min_meth_value

        // this.dat.tablePage1.ExpsubFilter.range = [
        //   res.data.MaxMin.max_exp_value,
        //   res.data.MaxMin.min_exp_value
        // ]
        //
        // this.dat.tablePage1.CNVsubFilter.range = [
        //   res.data.MaxMin.max_cnv_value,
        //   res.data.MaxMin.min_cnv_value
        // ]
        //
        // this.dat.tablePage1.MethsubFilter.range = [
        //   res.data.MaxMin.max_meth_value,
        //   res.data.MaxMin.min_meth_value
        // ]

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
    resetFilters() {
      this.dat.tablePage1.SYMBOL = null;
      this.dat.tablePage1.ENSGID = null;
      this.dat.tablePage1.NAME = null;
      this.dat.tablePage1.LOUCSTYPE = null;
      this.dat.tablePage1.pageSize = 10;
      this.dat.tablePage1.currentPage = 1;
      this.dat.tablePage1.FilterEXP = false;
      this.dat.tablePage1.FilterSNV = false;
      this.dat.tablePage1.FilterCNV = false;
      this.dat.tablePage1.FilterMETH = false;
      for (let x in this.dat.tablePage1.SNVsubFilter.impact) {
        this.dat.tablePage1.SNVsubFilter.impact[x].mark = true;
      }


      this.loadDataByPage()
    },
    debounceFilter: _.debounce(function () {
      // console.log("enter setTimeout")
      this.dat.tablePage1.currentPage = 1
      this.loadDataByPage()
    }, 500),

  },

}
</script>

<style scoped>
.z-transparent {
  background-color: transparent !important;
  opacity: 1;
  border-color: transparent !important;
}
</style>
