<template>
  <v-container class="container--fluid">

    <v-row>


      <v-col class="pa-0" cols="12">
        <!--蓝色背景部分-->
        <v-sheet :style="{
           backgroundImage: 'url('+bannerimg+')',
           height:'550px',
           paddingBottom:'50px',
           marginTop:'20px',
           backgroundRepeat:'no-repeat',
           backgroundSize:'100% 150%',
           }"
                 class="mb-2"
                 elevation="4"
        >

          <v-row class="mt-8">
            <v-spacer></v-spacer>
            <v-col class="mt-16 pt-8" cols="6">
              <div class="white--text text--darken-1 text-h3"
              >
                <span class="yellow--text text--darken-2">C</span>ancer
                <span class="text--accent-3">g</span>enome
                <span class="teal--text text--accent-3">C</span>onsensus<br/>
                <span class="purple--text">A</span>nnotation
                <span class="deep-purple--text text--accent-4">S</span>ystem
              </div>
            </v-col>
            <v-spacer></v-spacer>
          </v-row>
          <v-row>
            <v-spacer></v-spacer>
            <v-col class="mt-3" cols="6">
              <div class="white--text text--darken-1 text-h5"
              >
                One-stop and comprehensive annotation system for individual cancer genome at multi-omics
                level
              </div>
            </v-col>
            <v-spacer></v-spacer>
          </v-row>
          <v-row class="mt-4">
            <v-spacer></v-spacer>
            <v-col class="mt-3" cols="12" lg="3" md="12" sm="12" xl="3">

              <v-card class="px-2 py-6 z-transparent" elevation="3" rounded
                      @click="setTabAndRouter('k_cancertype','/doc')"
              >
                <div class="white--text text-h4 py-2">395</div>
                <v-divider dark></v-divider>
                <div class="white--text text-h5 py-2">Cancer subtypes</div>
              </v-card>
            </v-col>
            <v-col class="mt-3" cols="12" lg="3" md="12" sm="12" xl="3">
              <v-card class="px-2 py-6 z-transparent " elevation="3" rounded
                      @click="setTabAndRouter('k_usage','/doc')"
              >
                <div class="white--text text-h4 py-2">6</div>
                <v-divider dark></v-divider>
                <div class="white--text text-h5 py-2">Annotation aspects</div>
              </v-card>
            </v-col>

            <v-col class="mt-3" cols="12" lg="3" md="12" sm="12" xl="3">
              <v-card class="px-2 py-6 z-transparent " elevation="3" rounded
                      @click="setTabAndRouter('k_resources','/doc')"
              >
                <div class="white--text text-h4 py-2">20</div>
                <v-divider dark></v-divider>
                <div class="white--text text-h5 py-2">Resources</div>
              </v-card>
            </v-col>

            <v-spacer></v-spacer>
          </v-row>
          <v-row>
            <v-col cols="10" offset="1">
              <div class="z-transparent white--text" style="color: white"> Recommended browsers: Chrome, MicroSoft
                Edge.
              </div>
            </v-col>
          </v-row>
        </v-sheet>


        <v-row class="mt-6">
          <v-spacer>
          </v-spacer>
          <v-col cols="11">
            <v-card class="pb-6">
              <v-row>
                <v-spacer>
                </v-spacer>
                <v-col cols='12' lg="6" md="8" sm="12">
                  <div class="text-h4 teal--text darken-4 my-6"> Start your annotation!
                    <common-help-message>Mandatory inputs for CCAS include cancer subtypes and SNV variation data. Other
                      omics data are optional. After filling in all required data and optional data, click Start to run
                      the annotation process.
                    </common-help-message>
                  </div>
                </v-col>
                <v-spacer>
                </v-spacer>

              </v-row>
              <!--            分隔符-->
              <v-row class="px-8">
                <v-spacer></v-spacer>
                <v-col cols='12' lg="6" md="8" sm="12">
                  <v-divider></v-divider>

                </v-col>
                <v-spacer></v-spacer>
              </v-row>
              <v-progress-circular
                  v-show="doid_list == null"
                  class="float-start mt-2 ml-2"
                  color="white"
                  indeterminate

              ></v-progress-circular>
              <v-row class="py-4">
                <v-col cols="12" lg="7" md="12" sm="12" xl="7">
                  <v-row>
                    <v-col class=" text-start " cols="10" offset="1">
                      <v-row>
                        <v-col cols="6">
                          <v-row class="mynarrowline">
                            <v-col cols="2" offset="1">
                              <v-switch
                                  v-model="showJobTitle"
                                  color="teal"
                                  hide-details
                              ></v-switch>
                            </v-col>
                            <v-col cols="9">
                              <v-text-field
                                  v-model="upload_data_jobtitle"
                                  :disabled="!showJobTitle"
                                  clearable
                                  label="Job title"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-col>
                        <v-col cols="6">
                          <v-row class="mynarrowline">
                            <v-col cols="2" offset="1">
                              <v-switch
                                  v-model="showEmail"
                                  color="teal"
                                  hide-details

                              ></v-switch>
                            </v-col>
                            <v-col cols="9">
                              <v-text-field
                                  v-model="upload_data_email"
                                  :disabled="!showEmail"
                                  :rules="[rules.email]"
                                  clearable
                                  label="Email"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-col>
                      </v-row>

                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class=" text-start " cols="10" offset="1">
                      <v-sheet class="teal--text text-body-1">
                        Search cancer by name or DOID <span><common-help-message>The above cancer types are from do database. Please select the cancer type as accurately as possible to ensure better annotation results. If there are two cancers with similar names, please choose the one that is more suitable.</common-help-message></span>
                      </v-sheet>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-spacer></v-spacer>
                    <v-col cols="10">
                      <v-autocomplete
                          v-model="upload_data_cancertype"
                          :items="doid_dict2list || []"
                          clearable
                          dense
                          outlined
                      >
                      </v-autocomplete>
                      <!--                  :rules="[rules.required]"-->
                    </v-col>
                    <v-spacer></v-spacer>
                  </v-row>
                  <v-row>
                    <v-col class=" text-start " cols="10" offset="1">
                      <v-sheet class="teal--text text-body-1">
                        <h4>OR</h4> Choose cancer by tissue <span><common-help-message>The above cancer types are from do database. Please select the cancer type as accurately as possible to ensure better annotation results. If there are two cancers with similar names, please choose the one that is more suitable.</common-help-message></span>
                      </v-sheet>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-spacer></v-spacer>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" ( doid_list && doid_list['Blood'] && doid_list['Blood'].children || [])"
                          :image_url="require('../assets/img/organs/blood.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Blood"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Blood</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Bone'] && doid_list['Bone'].children || []"
                          :image_url="require('../assets/img/organs/bone.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Bone"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Bone</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat="doid_list && doid_list['Gland'] && doid_list['Gland'].children || []"
                          :image_url="require('../assets/img/organs/gland.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Glands"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Glands</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Skin'] && doid_list['Skin'].children || []"
                          :image_url="require('../assets/img/organs/skin.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Skin"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Skin</div>
                    </v-col>

                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Head And Neck Regions'] && doid_list['Head And Neck Regions'].children || []"
                          :image_url="require('../assets/img/organs/head_neck.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Head and neck"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Head and neck</div>
                    </v-col>
                    <v-spacer></v-spacer>
                  </v-row>

                  <v-row>
                    <v-spacer></v-spacer>

                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Reproductive Organs'] && doid_list['Reproductive Organs'].children || []"

                          :image_url="require('../assets/img/organs/reproductive_organ.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Reproductive system"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Reproductive system</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Thoracic Organs'] && doid_list['Thoracic Organs'].children || []"
                          :image_url="require('../assets/img/organs/Thoracic_organs.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Thoracic organs"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Thoracic organs</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Urinary Organs'] && doid_list['Urinary Organs'].children || []"

                          :image_url="require('../assets/img/organs/urinary_organs.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Urinary system"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Urinary system</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Abdominal Organs'] && doid_list['Abdominal Organs'].children || []"
                          :image_url="require('../assets/img/organs/Abdominal_organs.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Abdominal organs"
                      ></common-doid-group>
                      <!--                    :image_url='baseurl+"/static/img/organs/Abdominal_organs.png"'-->
                      <div class="teal--text text-body-1">Abdminal organs</div>
                    </v-col>
                    <v-col cols="12" lg="2" md="2" sm="12" xl="2">
                      <common-doid-group
                          :dat=" doid_list && doid_list['Other'] && doid_list['Other'].children || []"
                          :image_url="require('../assets/img/organs/other.png')"
                          :imgsize="plot_canvas_styles.imgsize"
                          group-name="Others"
                      ></common-doid-group>
                      <div class="teal--text text-body-1">Others</div>
                    </v-col>
                    <v-spacer></v-spacer>
                  </v-row>
                </v-col>
                <v-divider vertical></v-divider>
                <v-col cols="12" lg="5" md="12" sm="12" xl="5">

                  <v-sheet>
                    <v-row class="mynarrowline">
                      <v-col cols="10" offset="1">
                        <v-sheet>
                          <v-select
                              v-model="upload_data_refversion"
                              :items="refversion"
                              :rules="[rules.required]"
                              label="Select reference version"
                              prepend-icon="mdi-vanish"
                          >
                          </v-select>
                        </v-sheet>
                      </v-col>
                    </v-row>

                    <v-row class="mynarrowline">
                      <v-col cols="10" offset="1">
                        <v-row align="center">
                          <v-col cols="4">
                            <v-select
                                v-model="upload_data_file_type"
                                :items="fileTypes.snvindels"
                                :rules="[rules.required]"
                                label="Select snv/indels file type"

                            >
                              <template #prepend>
                                <v-icon color="red">mdi-dna</v-icon>
                              </template>

                            </v-select>
                          </v-col>
                          <v-col cols="6">
                            <v-file-input
                                v-model="upload_data_file"
                                :rules="[rules.required]"
                                label="Upload snv/indels file"
                                prepend-icon=""
                            >


                            </v-file-input>
                          </v-col>
                          <v-col cols="2">
                            <v-btn :href="baseurl+'/static/examples/demo.SNVIndels.vcf'" class="mdi-18px" color="teal"
                                   elevation="0" fab outlined
                                   small target="_blank"
                            >
                              <v-icon>mdi-cloud-download</v-icon>
                            </v-btn>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>

                    <v-row class="mynarrowline">
                      <v-col cols="10" offset="1">
                        <v-row align="center">
                          <v-col cols="4">
                            <v-select
                                v-model="upload_data_exp_file_type"
                                :items="fileTypes.exp"
                                clearable
                                label="Select expression file type"
                                prepend-icon="mdi-dna"
                            ></v-select>
                          </v-col>
                          <v-col cols="6">
                            <v-file-input
                                v-model="upload_data_exp_file"
                                label="Upload your expression file"
                                prepend-icon=""
                            ></v-file-input>
                          </v-col>
                          <v-col cols="2">
                            <v-btn :href="baseurl+'/static/examples/demo.Exp.gene.txt'" class="mdi-18px" color="teal"
                                   elevation="0" fab outlined
                                   small target="_blank"
                            >
                              <v-icon>mdi-cloud-download</v-icon>
                            </v-btn>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>

                    <v-row class="mynarrowline">
                      <v-col cols="10" offset="1">
                        <v-row align="center">
                          <v-col cols="4">
                            <v-select
                                v-model="upload_data_cnv_file_type"
                                :items="fileTypes.cnv"
                                clearable
                                label="Select CNV file type"
                                prepend-icon="mdi-dna"
                            ></v-select>
                          </v-col>
                          <v-col cols="6">
                            <v-file-input
                                v-model="upload_data_cnv_file"
                                label="Upload your CNV file"
                                prepend-icon=""
                            ></v-file-input>
                          </v-col>
                          <v-col cols="2">
                            <v-btn :href="baseurl+'/static/examples/demo.CNV.region.txt'" class="mdi-18px" color="teal"
                                   elevation="0" fab outlined
                                   small target="_blank"
                            >
                              <v-icon>mdi-cloud-download</v-icon>
                            </v-btn>
                          </v-col>
                        </v-row>

                      </v-col>
                    </v-row>
                    <v-row class="mynarrowline">
                      <v-col cols="10" offset="1">
                        <v-row align="center">
                          <v-col cols="4">
                            <v-select
                                v-model="upload_data_meth_file_type"
                                :items="fileTypes.meth"
                                clearable
                                label="Select methylation file type"
                                prepend-icon="mdi-dna"
                            ></v-select>
                          </v-col>
                          <v-col cols="6">
                            <v-file-input
                                v-model="upload_data_meth_file"
                                label="Upload your methylation file"
                                prepend-icon=""
                            ></v-file-input>
                          </v-col>
                          <v-col cols="2">
                            <v-btn :href="baseurl+'/static/examples/demo.Meth.gene.txt'" class="mdi-18px" color="teal"
                                   elevation="0" fab outlined
                                   small target="_blank"
                            >
                              <v-icon>mdi-cloud-download</v-icon>
                            </v-btn>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>

                    <v-row>
                      <v-col cols="12">
                        <v-sheet>
                          <v-icon color="red">mdi-dna</v-icon>
                          Required &nbsp;
                          <v-icon>mdi-dna</v-icon>
                          Optional &nbsp;
                          <v-btn class="mdi-18px" color="teal" elevation="0" fab outlined small>
                            <v-icon>mdi-cloud-download</v-icon>
                          </v-btn>
                          Example file

                        </v-sheet>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col cols="12">
                        <v-sheet class="text-body-2 text-justify px-4">
                          CCAS receives multi-omics data as input for multi-dimensional annotation of tumors. In CCAS,
                          SNV/indels level data is necessary. The data at the Expression, CNV, and Methylation levels
                          are optional. The SNV/indels part accepts data in the form of VCF, MAF, or 5 column table. The
                          Expression, Copy Number Variation (CNV), and Methylation parts receive the genes-value table
                          (Ensembl Gene ID\tValue)
                          as inputs. Meanwhile, CNV and Methylation also support region format (Chr\tStart\tEnd\tValue)
                          as input.
                        </v-sheet>
                      </v-col>
                    </v-row>
                  </v-sheet>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="10" offset="1">
                  <v-divider></v-divider>
                </v-col>
              </v-row>

              <v-row align="center" class="px-3">
                <v-col cols="6" offset="3">
                  <v-row class="mynarrowline">

                    <v-col cols="4">
                      <v-btn
                          :disabled="submitting"
                          :loading="submitting"
                          color="red"
                          outlined
                          width="100%"
                          @click="upload2backend($event)"
                      >
                        <v-icon>
                          mdi-rocket-outline
                        </v-icon>
                        Start!

                      </v-btn>
                    </v-col>
                    <v-col cols="4">
                      <v-btn

                          class="mx-4"
                          color="teal"
                          dark
                          outlined
                          to="/checkresults"
                          width="100%"
                      >
                        <v-icon>mdi-chemical-weapon</v-icon>
                        Check Results
                      </v-btn>
                    </v-col>
                    <v-col cols="4">
                      <v-btn

                          class="mx-4"
                          color="teal"
                          dark
                          outlined
                          width="100%"
                          @click="loadDemo"
                      >
                        <v-icon>
                          mdi-lifebuoy
                        </v-icon>
                        Demo Results
                      </v-btn>
                    </v-col>

                  </v-row>
                </v-col>
              </v-row>

              <v-row>
                <v-spacer></v-spacer>
                <v-col cols="10">
                  <v-card
                      v-show="msgshow"
                      class="px-2 py-4 mt-4"
                      color="teal lighten-2"
                  >
                    <v-btn v-show="submitOK" class="float-end mr-1 mt-1 lighten-2" color="teal" dark elevation="0" fab
                           small
                           @click="doCopy">
                      <v-icon>mdi-content-copy</v-icon>
                    </v-btn>
                    <v-btn class="float-end mr-1 mt-1 lighten-2" color="teal" dark elevation="0" fab small
                           @click="msgshow = !msgshow">
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                    <v-sheet
                        color="teal lighten-2"
                        dark
                        v-html="response_msg"
                    >

                    </v-sheet>
                  </v-card>
                </v-col>
                <v-spacer></v-spacer>
              </v-row>
            </v-card>


          </v-col>
          <v-spacer>
          </v-spacer>

        </v-row>


      </v-col>
    </v-row>
    <v-row>
      <v-spacer></v-spacer>
      <v-col lg="11" md="11" sm="12">
        <v-row>

          <v-col class="pl-0 pr-2" cols="12" lg="3" md="3" sm="12">
            <v-sheet class=" pt-6  overflow-y-auto" elevation="4" height="100%" rounded>
              <v-sheet class="teal--text text-h5 my-6 text-start mx-6"> Recent events</v-sheet>
              <v-divider></v-divider>
              <v-list
                  v-for="itm in homeNews"
                  :key="itm.title"
                  class=" text-start overflow-y-auto mb-2"
                  max-height="400"
              >
                <v-list-item two-line>
                  <v-list-item-content>
                    <v-list-item-title>{{ itm.title }}</v-list-item-title>
                    <v-list-item-subtitle>{{ itm.content }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>
          <v-col class="px-2" cols="12" lg="3" md="3" sm="12">
            <v-sheet class=" pt-6 " elevation="4" height="100%" rounded>
              <v-sheet class="mx-6">
                <div class="teal--text text-h5 my-6 text-start"> Contact</div>

              </v-sheet>
              <v-divider></v-divider>
              <v-sheet class="text-start pl-4 text-body-2 my-3">

                <p>
                  <b>If you would like to learn more about CCAS, please feel free to contact us.</b>
                </p>
                <b>Email:</b><br/>
                zhengxinchang(AT)big.ac.cn<br/><br/>
                <b>Address</b><br/>
                National Genomics Data Center<br/>
                Beijing Institute of Genomics<br/>
                Chinese Academy of Sciences<br/>
                1 Beichen West Road, Chaoyang District<br/>
                Beijing 100101, China<br/>
              </v-sheet>
            </v-sheet>
          </v-col>
          <v-col class="pl-2 pr-0" cols="12" lg="3" md="3" sm="12">
            <v-sheet class=" pt-6 " elevation="4" height="100%" rounded>
              <v-sheet class="mx-6">
                <div class="teal--text text-h5 my-6 text-start"> How to cite</div>
              </v-sheet>
              <v-divider></v-divider>
              <v-sheet class="text-justify text-body-2 pa-3">
                1. Zheng X, Zong W, Li Z, Ma Y, Sun Y, Xiong Z, Wu S, Yang F, Zhao W, Bu C, Du Z. CCAS: One-stop and
                comprehensive annotation system for individual cancer genome at multi-omics level. Front Genet. 2022 Aug
                11;13:956781. <br/>doi: 10.3389/fgene.2022.956781. eCollection 2022. PMID: <a
                  href="https://pubmed.ncbi.nlm.nih.gov/36035123/" style="text-decoration: none" target="_blank">36035123</a>
                <br/><br/>
                2. Database Resources of the National Genomics Data Center, China National Center for Bioinformation in
                2022 Nucleic Acids Res
                . 2022 Jan 7;50(D1):D27-D38. <br/>doi: 10.1093/nar/gkab951. PMID: <a
                  href="https://pubmed.ncbi.nlm.nih.gov/34718731/" style="text-decoration: none" target="_blank">34718731</a>
              </v-sheet>
            </v-sheet>
          </v-col>
          <v-col class="pl-2 pr-0" cols="12" lg="3" md="3" sm="12">
            <v-sheet class=" pt-6 " elevation="4" height="100%" rounded>
              <v-sheet class="mx-6">
                <div class="teal--text text-h5 my-6 text-start"> Related resource</div>
              </v-sheet>
              <v-divider></v-divider>
              <v-sheet class="text-justify text-body-2 pa-3">
                <v-list class="overflow-y-auto overflow-x-hidden" max-height="220">
                  <v-list-item v-for="(item,idx) in relatedlinks" :key="idx" :href="item.href" class="align--center"
                               target="_blank">
                    <v-sheet class="text-left">
                      <v-icon>mdi-link-variant</v-icon> &nbsp;
                      <span class="black--text font-weight-bold mr-3" style="white-space: nowrap">{{ item.name }}</span>

                      <img :src="item.logo" height="20" style="display: inline-block;border: 1px solid darkgrey"></img>

                    </v-sheet>

                  </v-list-item>


                </v-list>
              </v-sheet>
            </v-sheet>
          </v-col>

        </v-row>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>

  </v-container>
</template>

<script>
import {mapState} from 'vuex';
import CommonDoidGroup from "./sub/commonDoidGroup";
import Axios from 'axios'
import CommonHelpMessage from "./sub/commonHelpMessage";


export default {
  name: "home",
  components: {CommonHelpMessage, CommonDoidGroup},
  data() {
    return {
      bannerimg: require('../assets/img/bg.jpeg'),
      baseurl: window.BASE_URL,
      relatedlinks: [
        {
          href: "https://ngdc.cncb.ac.cn/macdb/home",
          icon: "mdi-link-variant",
          name: "MACdb",
          logo: require('../../static/img/macdb.png'),
        },
        {
          href: "https://ngdc.cncb.ac.cn/cancerscem/",
          icon: "mdi-link-variant",
          name: "CancerSCEM",
          logo: require('../../static/img/cancerscem.png'),
        },
        {
          href: "https://ngdc.cncb.ac.cn/ascancer/home",
          icon: "mdi-link-variant",
          name: "ASCancer Atlas",
          logo: require('../../static/img/ascancer.png'),
        },
      ],
      homeNews: [

        {
          title: "2021-11-20",
          content: "CCAS is publicly avaliable.",
        },
        {
          title: "2022-04-28",
          content: "CCAS v2 is publicly avaliable.",
        },

      ],
      rules: {
        required: value => !!value || 'Required.',
        counter: value => value.length <= 20 || 'Max 20 characters',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          const pattern_white_space = /^ *$/
          return (pattern.test(value) || pattern_white_space.test(value)) || 'Invalid e-mail.'
        },
      },
      plot_canvas_styles: {
        position: "absolute",
        gap: "25",
        gap_width: "40",
        imgsize: "100",
        left_point: "230",
        right_point: "670"
      },
      refversion: ["hg38", "hg19"],
      fileTypes: {
        "snvindels": ["vcf", "maf", "5coltsv"],
        "exp": ['gene'],
        "cnv": ['gene', 'region'],
        "meth": ['gene', 'region']
      },
      upload_data_file: null,
      upload_data_cancertype: null,
      upload_data_cancertype_doid: null,
      upload_data_refversion: "hg38",
      upload_data_email: null,
      upload_data_file_type: "vcf",
      upload_data_exp_file: null,
      upload_data_exp_file_type: null,
      upload_data_cnv_file: null,
      upload_data_cnv_file_type: null,
      upload_data_meth_file: null,
      upload_data_meth_file_type: null,
      upload_data_jobtitle: null,
      msgshow: false,
      response_msg: "",
      submitting: false,
      submitOK: false,
      submitUUID: null,
      showEmail: true,
      showJobTitle: true,
    }
  },
  computed: {
    ...mapState(["doid_list", "doid_dict", "doid_dict2list", "selected_doid"]),
  },
  watch: {
    selected_doid(newval, oldval) {
      this.upload_data_cancertype = this.doid_dict[newval][newval]
    },
    upload_data_cancertype(newval, oldval) {
      let doidNumber = newval.split("DOID:")[1].replace(")", "");
      // console.log(doidNumber);
      this.upload_data_cancertype_doid = "DOID:" + doidNumber;
    }
  },
  mounted() {
    // this.loadDiseaseTree();
    this.$store.dispatch("loadingDiseaseTree");
    // console.log(this.$store.state.doid_list)
  },
  methods: {
    // ...mapMutations(["setTabWith"]),
    loadDemo() {
      // this.jobid = "20220426165759_396258a7-c7f3-4337-99b5-f757fb9f69d6"
      let jobid = this.$store.state.demoJobid  //demo jobid
      if (jobid != null) {

        // this.$router.push('/annoresults/'+this.jobid)
        this.$router.push({name: 'annoresults', params: {jobid: jobid}})
      } else {
        alert("Job id is emtpy! Please provide job id before click check button.")
      }
    },
    setTabAndRouter(tab, r) {
      this.setTabWith(tab)
      this.$router.push(r)
    },
    doCopy: function () {
      this.$copyText(this.submitUUID).then(function (e) {
        alert('Copied')
      }, function (e) {
        alert('Can not copy')
      })
    },

    upload2backend(event) {
      event.preventDefault(); //event 是一个默认变量，是click的事件，preventDefault就是阻止click默认的事件。
      this.submitOK = false;
      let erromsg = {
        "cancertype": "Please choose cancer type.",
        "file": "Please upload snv file.",
        "refversion": "Please specify reference version.",
        "expcoExists": "Please provide both expression file type and expression file!",
        "cnvcoExists": "Please provide both CNV file type and CNV file!",
        "methcoExists": "Please provide both methylation file type and methylation file!",
      };

      let formData = new FormData();
      let pramasList = {
        "snvindeltype": this.upload_data_file_type,
        "doid": this.upload_data_cancertype_doid,
        "refver": this.upload_data_refversion,
        "email": this.upload_data_email,
        "jobtitle": this.upload_data_jobtitle
      }


      if (this.upload_data_file != null) {
        delete erromsg.file
      }

      if (this.upload_data_cancertype_doid != null) {
        delete erromsg.cancertype
      }


      if (this.upload_data_refversion != null) {
        delete erromsg.refversion
      }

      if ((this.upload_data_exp_file_type == null && this.upload_data_exp_file == null) || (this.upload_data_exp_file_type != null && this.upload_data_exp_file != null)) {
        delete erromsg.expcoExists;
        if (this.upload_data_exp_file_type != null && this.upload_data_exp_file != null) {
          formData.append("expFile", this.upload_data_exp_file);
          pramasList.exptype = this.upload_data_exp_file_type
        }

      } else {

      }

      if ((this.upload_data_meth_file_type == null && this.upload_data_meth_file == null) || (this.upload_data_meth_file_type != null && this.upload_data_meth_file != null)) {
        delete erromsg.methcoExists;
        if (this.upload_data_meth_file_type != null && this.upload_data_meth_file != null) {
          formData.append("methFile", this.upload_data_meth_file);
          pramasList.methtype = this.upload_data_meth_file_type
        }

      }

      if ((this.upload_data_cnv_file_type == null && this.upload_data_cnv_file == null) || (this.upload_data_cnv_file_type != null && this.upload_data_cnv_file != null)) {

        delete erromsg.cnvcoExists;

        if (this.upload_data_cnv_file_type != null && this.upload_data_cnv_file != null) {
          formData.append("cnvFile", this.upload_data_cnv_file);
          pramasList.cnvtype = this.upload_data_cnv_file_type

        }

      }


      if (Object.values(erromsg).length > 0) {
        this.response_msg = Object.values(erromsg).join("<br/>");
        this.msgshow = true;
        return;
      }


      if (this.upload_data_file != null &&
          this.upload_data_cancertype_doid != null &&
          this.upload_data_refversion != null) {
        this.submitting = true;

        let submit_email = null
        if (this.upload_data_email == "" || this.upload_data_email == null) {
          submit_email = "NotProvide";
        } else {
          submit_email = this.upload_data_email;
        }

        console.log(this.upload_data_exp_file)

        formData.append("snvindelFile", this.upload_data_file);
        pramasList.snvindeltype = this.upload_data_file_type;
        console.log(formData)
        Axios.post(
            window.BASE_URL + "/api/home_submit",
            formData,
            {
              // headers: {
              //   'Accept': 'application/json',
              //   'Content-Type': 'enctype=multipart/form-data'
              // },
              params: pramasList
            }
        ).then(res => {
              if (res.status == "200") {
                this.submitOK = true;
                this.submitting = false;
                this.msgshow = true;
                this.submitUUID = res.data.jobid;
                this.response_msg = `Your data is submitted! <br/>Please wait about 10 minutes until revieve the email notification for job completeness.<br/>Or you can check your job in "<a href="#/results">Check Results</a>" page with the job ID: ${res.data.jobid}`
              } else {
                this.submitting = false;
                this.msgshow = true;
                this.response_msg = `Submission failed!</br>In most cases, this is because the file you provide is in the wrong format. Please check your file format and try again. If you still encounter problems, please contact CCAs team (zhenxinchang@big.ac.cn)`
              }
            }
        ).catch(reason => {
          this.submitting = false;
          this.msgshow = true;
          this.response_msg = `Submit failed!</br>Please check your network or contact CCAS team.`
        })
      }

    },

  }
}
</script>

<style scoped>
.z-transparent {
  background-color: transparent !important;
  opacity: 1;
  border-color: transparent !important;
}

.mynarrowline {
  margin-top: 0px;
}

.mynarrowcol {
  margin-top: 0px;
}
</style>
