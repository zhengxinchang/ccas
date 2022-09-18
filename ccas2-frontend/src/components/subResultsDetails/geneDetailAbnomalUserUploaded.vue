<template>
  <v-sheet class="mx-3">
    <v-row align="end" class="pt-6">
      <v-col cols="12">
        <v-sheet class="text-h5 align-self-center">
          <v-icon class="mdi-24px" color="teal"> mdi-label-variant-outline</v-icon>
          <span>SNV/Indels</span>
        </v-sheet>
        <v-divider class="my-2"></v-divider>
        <v-sheet>
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
            empty-text="Empty"
            max-height="600"
            round
            stripe
          >
            <vxe-column title="#" type="seq" width="5%">
            </vxe-column>
            <vxe-column title="Details" type="expand" width="5%">
              <template #content="{ row, rowIndex }">

                <v-row class="mx-4 px-4">
                  <v-col class=" text-body-1 text-left" cols="12">
                    <v-sheet class="mt-4 mb-2 font-weight-bold" style="text-align: center">
                      <v-icon color="teal"> mdi-label-variant-outline</v-icon>
                      Variant frequencies in normal cohorts
                    </v-sheet>
                  </v-col>
                  <v-col>
                    <v-divider></v-divider>
                  </v-col>
                  <v-col cols="12">

                    <v-sheet align="center" class="pa-4" color="grey lighten-4 " outlined rounded>
                      <v-row align="center">
                        <v-col cols="4">
                          <v-card color="grey lighten-3" elevation="0">
                            <v-card-title>Frequencies in 1000 Genomes Project</v-card-title>
                            <v-card-text>
                              <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                <v-list-item v-for="item in dat.normalFreqDbProjection.x1000g" :key="item.key">
                                  <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                  <v-list-item-icon>
                                    <v-icon color="teal">
                                      mdi-hexagon-slice-6
                                    </v-icon>
                                  </v-list-item-icon>
                                  <v-list-item-content>
                                    {{ item.name }}: &nbsp;&nbsp; {{
                                      (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]) || "NA"
                                    }}
                                  </v-list-item-content>
                                </v-list-item>
                              </v-list>
                            </v-card-text>
                          </v-card>
                        </v-col>
                        <v-col cols="4">
                          <v-card color="grey lighten-3" elevation="0">
                            <v-card-title>Frequencies in gnomAD database</v-card-title>
                            <v-card-text>
                              <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                <v-list-item v-for="item in dat.normalFreqDbProjection.gnomad" :key="item.key">
                                  <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                  <v-list-item-icon>
                                    <v-icon color="teal">
                                      mdi-hexagon-slice-6
                                    </v-icon>
                                  </v-list-item-icon>
                                  <v-list-item-content>
                                    {{ item.name }}: &nbsp;&nbsp; {{
                                      (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]) || "NA"
                                    }}
                                  </v-list-item-content>
                                </v-list-item>
                              </v-list>
                            </v-card-text>
                          </v-card>
                        </v-col>
                        <v-col cols="4">
                          <v-card color="grey lighten-3" elevation="0">
                            <v-card-title>Frequencies in ExAC database</v-card-title>
                            <v-card-text>
                              <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                <v-list-item v-for="item in dat.normalFreqDbProjection.exac" :key="item.key">
                                  <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                  <v-list-item-icon>
                                    <v-icon color="teal">
                                      mdi-hexagon-slice-6
                                    </v-icon>
                                  </v-list-item-icon>
                                  <v-list-item-content>
                                    {{ item.name }}: &nbsp;&nbsp; {{
                                      (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]) || "NA"
                                    }}
                                  </v-list-item-content>
                                </v-list-item>
                              </v-list>
                            </v-card-text>
                          </v-card>
                        </v-col>
                      </v-row>
                    </v-sheet>
                  </v-col>

                  <!--                  跟上边的normal frequency 是一级别，里边分3个，是更低一层级别-->
                  <v-col cols="12">
                    <v-row>
                      <v-col cols="4">
                        <v-row>
                          <v-col class=" text-body-1  " cols="12">
                            <v-sheet class="mt-4 mb-2 font-weight-bold text-left" style="text-align: center">
                              <v-icon color="teal"> mdi-label-variant-outline</v-icon>
                              Variant spots(Cancer Hotspot v2) <span><common-help-message>
                              This content shows whether the variant is a hotspot in various cancers.
                            </common-help-message></span>
                            </v-sheet>
                          </v-col>
                          <v-col>
                            <v-divider></v-divider>
                          </v-col>
                          <v-col cols="12">

                            <v-sheet align="center" class="pa-4" color="grey lighten-4 " outlined rounded>
                              <v-row align="center">
                                <v-col>
                                  <v-card color="grey lighten-3" elevation="0">
                                    <v-card-text>
                                      <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                        <v-list-item
                                          v-for="item in (  (row.cancerhotspots.CancerHotposts_TumorsCount != 'NULL') &&  row.cancerhotspots.CancerHotposts_TumorsCount.split('//') || [])"
                                          :key="item">
                                          <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                          <v-list-item-icon>
                                            <v-icon color="teal">
                                              mdi-hexagon-slice-6
                                            </v-icon>
                                          </v-list-item-icon>
                                          <v-list-item-content>
                                            {{ item.split(":")[0] }}: &nbsp;&nbsp; {{ item.split(":")[1] }}
                                          </v-list-item-content>
                                        </v-list-item>
                                      </v-list>
                                    </v-card-text>
                                  </v-card>
                                </v-col>
                              </v-row>
                            </v-sheet>
                          </v-col>
                        </v-row>

                      </v-col>
                      <v-col cols="4">

                        <!--                        {-->
                        <!--                          UMLS: {-->
                        <!--                              C0279680: {-->
                        <!--                                  ID: "",-->
                        <!--                                  effect: {-->
                        <!--                                      Likely_pathogenic: [-->
                        <!--                                      "PMID12345"-->
                        <!--                                      ]-->
                        <!--                                  }-->
                        <!--                              }-->
                        <!--                          },-->
                        <!--                          MeSH: {-->
                        <!--                              C0279680: {-->
                        <!--                                  ID: "",-->
                        <!--                                  effect: {-->
                        <!--                                      Likely_pathogenic: [-->
                        <!--                                      "PMID12345"-->
                        <!--                                      ]-->
                        <!--                                    }-->
                        <!--                                  }-->
                        <!--                              }-->
                        <!--                        }-->

                        <v-row align="center">
                          <v-col class=" text-body-1  align--center" cols="12">
                            <v-sheet align="center" class="mt-4 mb-2 font-weight-bold text-left">
                              <v-icon color="teal"> mdi-label-variant-outline</v-icon>
                              Variant spots(DoCM) <span><common-help-message>
                              This content shows whether the variant is a curated mutations in DoCM(Database of Curated Mutations) database.
                            </common-help-message></span>
                            </v-sheet>
                          </v-col>
                          <v-col>
                            <v-divider></v-divider>
                          </v-col>
                          <v-col cols="12">

                            <v-sheet align="center" class="pa-4" color="grey lighten-4 " outlined rounded>
                              <v-row align="center">
                                <v-col>
                                  <v-card color="grey lighten-3" elevation="0">
                                    <v-card-text>
                                      <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                        <v-list-item
                                          v-for="item in ( row.DOCM && Object.values(row.DOCM.UMLS ) || []  )"
                                          :key="item.ID">
                                          <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                          <v-list-item-icon>
                                            <v-icon color="teal">
                                              mdi-hexagon-slice-6
                                            </v-icon>
                                          </v-list-item-icon>
                                          <v-list-item-content>
                                            Source: UMLS, &nbsp;ID: {{ item.ID }},&nbsp;Effect:
                                            {{ Object.keys(item.effect) }}
                                          </v-list-item-content>
                                        </v-list-item>
                                        <v-list-item v-for="item in ( row.DOCM && Object.values(row.DOCM.MeSH) || []  )"
                                                     :key="item.ID">
                                          <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                          <v-list-item-icon>
                                            <v-icon color="teal">
                                              mdi-hexagon-slice-6
                                            </v-icon>
                                          </v-list-item-icon>
                                          <v-list-item-content>
                                            Source: MeSH, &nbsp;ID: {{ item.ID }},&nbsp; Effect:
                                            {{ Object.keys(item.effect) }}
                                          </v-list-item-content>
                                        </v-list-item>
                                      </v-list>
                                    </v-card-text>
                                  </v-card>
                                </v-col>
                              </v-row>
                            </v-sheet>
                          </v-col>
                        </v-row>

                      </v-col>
                      <v-col cols="4">
                        <v-row align="center">
                          <v-col class=" text-body-1  align--center" cols="12">
                            <v-sheet align="center" class="mt-4 mb-2 font-weight-bold text-left">
                              <v-icon color="teal"> mdi-label-variant-outline</v-icon>
                              Variant spots(Cancer Genome Interpreter) <span><common-help-message>
                              This content shows whether the variant is a hotspot in Cancer Genome Interpreter database.
                            </common-help-message></span>
                            </v-sheet>
                          </v-col>
                          <v-col>
                            <v-divider></v-divider>
                          </v-col>
                          <v-col cols="12">

                            <v-sheet align="baseline" class="pa-4" color="grey lighten-4 " outlined rounded>
                              <v-row align="baseline">
                                <v-col>
                                  <v-card color="grey lighten-3" elevation="0">
                                    <v-card-text>
                                      <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                        <v-list-item v-for="entry in ( Object.entries( row.cgi )||  [] )" :key="entry">
                                          <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                          <v-list-item-icon>
                                            <v-icon color="teal">
                                              mdi-hexagon-slice-6
                                            </v-icon>
                                          </v-list-item-icon>
                                          <v-list-item-content>
                                            {{ entry[0] }} :&nbsp;{{ entry[1] != "NULL" ? entry[1] : "Not Report" }}

                                          </v-list-item-content>
                                        </v-list-item>
                                        <!--                                        {{row.cgi}}-->

                                      </v-list>
                                    </v-card-text>
                                  </v-card>
                                </v-col>
                              </v-row>
                            </v-sheet>
                          </v-col>
                        </v-row>
                      </v-col>
                      <v-col cols="4">
                        <v-row align="center">
                          <v-col class=" text-body-1  align--center" cols="12">
                            <v-sheet align="center" class="mt-4 mb-2 font-weight-bold text-left">
                              <v-icon color="teal"> mdi-label-variant-outline</v-icon>
                              Variant Damage Prediction(dbNSFP) <span><common-help-message>
                              This content shows whether the variant is predicted as a damaged variant. Data are from dbNSFP. For each score or phred, you can find description at
                              <a href="https://drive.google.com/file/d/1VINShZQYN63HvigJA_SiuOYIk8TWl5Fh/view" target="_blank" style="text-decoration: none" class="teal--text">here</a>

                            </common-help-message></span>
                            </v-sheet>
                          </v-col>
                          <v-col>
                            <v-divider></v-divider>
                          </v-col>
                          <v-col cols="12">

                            <v-sheet align="baseline" class="pa-4" color="grey lighten-4 " outlined rounded>
                              <v-row align="baseline">
                                <v-col>
                                  <v-card color="grey lighten-3" elevation="0">
                                    <v-card-text>
                                      <v-list class="overflow-y-auto" color="grey lighten-3" dense height="250">
                                        <v-list-item v-for="entry in ( dat.DamagePrediction )" :key="entry">
                                          <!--                                 <v-icon color="teal" >mdi-menu-right</v-icon> {{item.name}}:  {{ (row.annovar[item.key] == "NULL" ? "Not Report" : row.annovar[item.key]  ) || "NA" }}-->
                                          <v-list-item-icon>
                                            <v-icon color="teal">
                                              mdi-hexagon-slice-6
                                            </v-icon>
                                          </v-list-item-icon>
                                          <v-list-item-content>
                                            {{entry}}  :&nbsp;{{ row.annovar[entry] != "NULL" ? row.annovar[entry]  : "Not Report" }}

                                          </v-list-item-content>
                                        </v-list-item>
                                        <!--                                        {{row.cgi}}-->

                                      </v-list>
                                    </v-card-text>
                                  </v-card>
                                </v-col>
                              </v-row>
                            </v-sheet>
                          </v-col>
                        </v-row>
                      </v-col>

                    </v-row>
                  </v-col>


                </v-row>
                <v-row>
                  <v-col>
                    <v-sheet height="50"></v-sheet>
                  </v-col>
                </v-row>
              </template>

            </vxe-column>
            <vxe-column show-overflow="tooltip" sortable title="Position" width="15%">
              <template #default="{row}">
                {{ row.origin.chrom }}:{{ row.origin.pos }}
              </template>


            </vxe-column>
            <vxe-column field="origin.REF" show-overflow="tooltip" sortable title="Reference" width="10%">
            </vxe-column>
            <vxe-column field="origin.ALT" show-overflow="tooltip" sortable title="Alteration" width="10%">
            </vxe-column>
            <vxe-column show-overflow="tooltip" sortable title="Amino Acids" width="5%">
              <template #default="{row}">
                {{ row.vep[0].Amino_acids != "NULL" ? row.vep[0].Amino_acids : "" }}
              </template>
            </vxe-column>
            <vxe-column show-overflow="tooltip" sortable title="dbSNP Accession" width="5%">
              <template #default="{row}">
                {{ row.annovar.avsnp150 != "NULL" ? row.annovar.avsnp150 : "" }}
              </template>
            </vxe-column>
            <vxe-column field="vep[0].STRAND" show-overflow="tooltip" sortable title="Strand" width="10%">
              <template #default="{row}">
                {{ row.vep[0].STRAND == -1 ? "minus" : "plus" }}
              </template>
            </vxe-column>
            <vxe-column field="vep[0].Consequence" show-overflow="tooltip" sortable title="Consequence" width="10%">
              <template #header="{column}">
                {{column.title}} <span><common-help-message>The Consequences are calculated by VEP. The detailed descriptions can be found <a style="text-decoration: none" class="teal--text" href="http://grch37.ensembl.org/info/genome/variation/prediction/predicted_data.html" target="_blank">here</a></common-help-message></span>
              </template>

            </vxe-column>
            <vxe-column field="vep[0].IMPACT" show-overflow="tooltip" sortable title="IMPACT" width="10%">
              <template #header="{column}">
                {{column.title}} <span><common-help-message>The IMPACT are calculated by VEP. The detailed descriptions can be found <a style="text-decoration: none" class="teal--text" href="http://grch37.ensembl.org/info/genome/variation/prediction/predicted_data.html" target="_blank">here</a></common-help-message></span>
              </template>
            </vxe-column>
            <vxe-column field="vep[0].HGVSc" show-overflow="tooltip" sortable title="HGVSc" width="15%">
            </vxe-column>
            <!--            <vxe-column sortable width="15%" show-overflow="tooltip"  title="Disease Name">-->
            <!--            </vxe-column>-->
            <!--            &lt;!&ndash;            <vxe-column sortable width="5%" sort-type="number" show-overflow="tooltip"  field="phase" title="Phase">&ndash;&gt;-->
            <!--            &lt;!&ndash;            </vxe-column>&ndash;&gt;-->
            <!--            <vxe-column sortable width="25%"    title="Clinical Trials">-->
            <!--              <template #default="{ row }">-->


            <!--              </template>-->
            <!--            </vxe-column>-->


          </vxe-table>
        </v-sheet>
      </v-col>
      <v-col class="mt-8" cols="12">

        <v-sheet    rounded>
          <v-row>
            <v-col cols="4">
              <v-sheet class="text-h5 align-self-center">
                <v-icon class="mdi-24px" color="teal"> mdi-label-variant-outline</v-icon>
                <span>Expression</span>
              </v-sheet>
              <v-divider class="my-2"></v-divider>
              <v-sheet color="grey lighten-4"  rounded outlined >
                <v-list color="grey lighten-4" height="200">
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Type: &nbsp; {{expTableData[0] &&(expTableData[0].regions == null ? "gene":"region") || "NA"}}</v-list-item-content>
                  </v-list-item>
                  <v-list-item v-show="expTableData[0] && ( expTableData[0].regions != null) || false">
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Region: &nbsp; {{expTableData[0] && expTableData[0].regions && expTableData[0].regions.split(":").slice(0,3)|| "NA"}}</v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Value: &nbsp; {{expTableData[0] && expTableData[0].value || "NA"}}</v-list-item-content>
                  </v-list-item>
                </v-list>

              </v-sheet>
            </v-col>
            <v-col cols="4">
              <v-sheet class="text-h5 align-self-center">
                <v-icon class="mdi-24px" color="teal"> mdi-label-variant-outline</v-icon>
                <span>CNV</span>
              </v-sheet>
              <v-divider class="my-2"></v-divider>
              <v-sheet color="grey lighten-4"  rounded outlined >
                <v-list color="grey lighten-4" height="200">
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Type: &nbsp; {{cnvTableData[0] && (cnvTableData[0].regions == null ? "gene":"region") || "NA"}}</v-list-item-content>
                  </v-list-item>
                  <v-list-item v-show="cnvTableData[0] && ( cnvTableData[0].regions != null) || false">
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Region: &nbsp; {{cnvTableData[0] &&  cnvTableData[0].regions && cnvTableData[0].regions.split(":").slice(0,3).join(":")|| "NA"}}</v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Value: &nbsp; {{cnvTableData[0] && cnvTableData[0].value || "NA"}}</v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-sheet>
            </v-col>
            <v-col cols="4">
              <v-sheet class="text-h5 align-self-center">
                <v-icon class="mdi-24px" color="teal"> mdi-label-variant-outline</v-icon>
                <span>Methylation</span>
              </v-sheet>
              <v-divider class="my-2"></v-divider>
              <v-sheet color="grey lighten-4"  rounded outlined >
                <v-list color="grey lighten-4" height="200">
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Type: &nbsp; {{methTableData[0] && (methTableData[0].regions == null ? "gene":"region") || "NA"}}</v-list-item-content>
                  </v-list-item>
                  <v-list-item v-show="methTableData[0] && ( methTableData[0].regions != null) || false">
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Region: &nbsp; {{methTableData[0] && methTableData[0].regions && methTableData[0].regions.split(":").slice(0,3).join(":")|| "NA"}}</v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="teal">
                        mdi-hexagon-slice-6
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Value: &nbsp; {{methTableData[0]  && methTableData[0].value || "NA"}}</v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-sheet>
            </v-col>
          </v-row>
        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2 text-end" cols="12">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://www.ensembl.org/index.html" small style="text-transform: none"
          target="_blank"> Variant Effect Predictor
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://annovar.openbioinformatics.org/en/latest/" small style="text-transform: none"
          target="_blank"> ANNOVAR
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://www.cancerhotspots.org/#/home" small style="text-transform: none"
          target="_blank"> Cancer Hotspot V2
        </v-btn>
<!--        <v-btn-->
<!--          color="teal lighten-3" dark elevation="0" href="https://reactome.org/" small style="text-transform: none"-->
<!--          target="_blank"> DoCM-->
<!--        </v-btn>-->
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://www.cancergenomeinterpreter.org/" small style="text-transform: none"
          target="_blank"> Cancer Genome Interpreter
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://www.genome.gov/27528684/1000-genomes-project" small style="text-transform: none"
          target="_blank"> 1000 Genome Project
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://gnomad.broadinstitute.org/" small style="text-transform: none"
          target="_blank"> gnomAD
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://gnomad.broadinstitute.org/" small style="text-transform: none"
          target="_blank"> ExAC
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import CommonHelpMessage from "../sub/commonHelpMessage";

export default {
  name: "geneDetailAbnomalUserUploaded",
  components: {CommonHelpMessage},
  props: ["snvTableData", "cnvTableData", "expTableData", "methTableData"],

  data() {
    return {
      dat: {
        tableData: [],
        allAlign: null,
        tablePage1: {
          currentPage: 1,
          pageSize: 10,
          totalPage: null,
        },
        normalFreqDbProjection: {
          x1000g: [
            {key: "1000g2015aug_afr", name: "African"},
            {key: "1000g2015aug_eas", name: "East Asian"},
            {key: "1000g2015aug_eur", name: "European"},
            {key: "1000g2015aug_sas", name: "South Asian"},
            {key: "1000g2015aug_amr", name: "American"},
          ],
          gnomad: [
            {key: "AF_afr", name: "African/African American"},
            {key: "AF_ami", name: "Amish"},
            {key: "AF_amr", name: "GnomAD American"},
            {key: "AF_asj", name: "Ashkenazi Jewish"},
            {key: "AF_eas", name: "East Asian"},
            {key: "AF_fin", name: "Finnish"},
            {key: "AF_nfe", name: "Non-Finnish European"},
            {key: "AF_oth", name: "Others"},
            {key: "AF_sas", name: "South Asian"},
          ],
          exac: [
            {key: "ExAC_AFR", name: "African/African American"},
            {key: "ExAC_AMR", name: "American"},
            {key: "ExAC_EAS", name: "East Asian"},
            {key: "ExAC_FIN", name: "Finnish"},
            {key: "ExAC_NFE", name: "Non-Finnish European"},
            {key: "ExAC_OTH", name: "Others"},
            {key: "ExAC_SAS", name: "South Asian"},
          ]
        },
        DamagePrediction:["MetaSVM_pred","MetaLR_pred","DamagePredCount", "SIFT_pred",
          "SIFT4G_pred", "Polyphen2_HDIV_pred",
          "Polyphen2_HVAR_pred", "LRT_pred",
          "MutationTaster_pred", "MutationAssessor_pred",
          "FATHMM_pred", "PROVEAN_pred",
          "VEST4_score", "M-CAP_pred",
          "REVEL_score", "MutPred_score",
          "MVP_score", "MPC_score",
          "PrimateAI_pred", "DEOGEN2_pred",
          "BayesDel_addAF_pred", "BayesDel_noAF_pred",
          "ClinPred_pred", "LIST-S2_pred", "CADD_raw",
          "CADD_phred", "DANN_score", "fathmm-MKL_coding_pred",
          "fathmm-XF_coding_pred", "Eigen-raw_coding",
          "Eigen-phred_coding", "Eigen-PC-raw_coding",
          "Eigen-PC-phred_coding", "GenoCanyon_score",
          "integrated_fitCons_score", "GM12878_fitCons_score",
          "H1-hESC_fitCons_score", "HUVEC_fitCons_score", "LINSIGHT",
          "GERP++_NR", "GERP++_RS", "phyloP100way_vertebrate",
          "phyloP30way_mammalian", "phyloP17way_primate",
          "phastCons100way_vertebrate", "phastCons30way_mammalian",
          "phastCons17way_primate",],

      }
    }
  },
  watch: {
    tableData: {
      handler: function () {

        this.dat.tableData = this.snvTableData
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
