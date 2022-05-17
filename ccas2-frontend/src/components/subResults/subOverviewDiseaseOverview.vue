<template>
  <v-sheet class="mx-3">
    <v-row  class="pt-6" align="center">
      <v-col cols="6">
        <v-sheet class="text-h4">Job ID:</v-sheet>
        <v-sheet class="text-h5 mt-2"> {{ dat.jobinfo && dat.jobinfo.jobid }}</v-sheet>
      </v-col>
      <v-col cols="6">
        <v-sheet class="text-h4">Job Title:</v-sheet>
        <v-sheet class="text-h5 mt-2"> {{ dat.jobinfo && dat.jobinfo.title }}</v-sheet>
      </v-col>
    </v-row>
    <v-row align="center" class="pt-6">
      <v-divider></v-divider>
    </v-row>
    <v-row align="center" class="pt-6">
      <v-col cols="2">
        <v-sheet :class="itemsClass">Reference Version:</v-sheet>
        <v-sheet :class="itemsContentClass"> {{ dat.jobinfo.refver }}</v-sheet>
      </v-col>
      <v-col cols="2">
        <v-sheet :class="itemsClass">Submit Time:</v-sheet>
        <v-sheet :class="itemsContentClass"> {{ dat.jobinfo.start_time }}</v-sheet>
      </v-col>
      <v-col cols="2">
        <v-sheet :class="itemsClass">Notification Email:</v-sheet>
        <v-sheet  :class="itemsContentClass"> {{ dat.jobinfo.email == null ? "Not provided" : dat.jobinfo.email }}</v-sheet>
      </v-col>
      <v-col cols="6">
        <!--    <v-icon>mdi-dots-vertical</v-icon> Job Title: {{dat.jobinfo.title}}-->
        <v-sheet :class="itemsClass">Submit Data Types
          <common-help-message>
            This shows the data and data types user provided in the submission.<br/>
            There are 4 categories of omics data are supported in CCAS incuding SNV/Indels, Copy number variation, Expression and Methylation.<br/>

          </common-help-message>
        </v-sheet>
        <v-sheet  :class="itemsContentClass" >
          SNV/Indels:
          <v-chip color="teal" dark label outlined small>Yes: {{ dat.jobinfo.snvindeltype }}</v-chip>
          &nbsp;&nbsp; Copy Number:
          <v-chip :color=" parseInt(dat.jobinfo.has_cnv) == 1?  'teal' :'grey' " dark label outlined small>
            {{ parseInt(dat.jobinfo.has_cnv) == 1 ? "Yes" : "No" }}: {{ dat.jobinfo.cnvtype }}
          </v-chip>
          &nbsp;&nbsp; Expression:
          <v-chip :color=" parseInt(dat.jobinfo.has_exp) == 1?  'teal' :'grey' " dark label outlined small>
            {{ parseInt(dat.jobinfo.has_exp) == 1 ? "Yes" : "No" }}: {{ dat.jobinfo.exptype }}
          </v-chip>
          &nbsp;&nbsp; Methylation:
          <v-chip :color=" parseInt(dat.jobinfo.has_meth) == 1?  'teal' :'grey' " dark label outlined small>
            {{ parseInt(dat.jobinfo.has_meth) == 1 ? "Yes" : "No" }}: {{ dat.jobinfo.methtype }}
          </v-chip>
        </v-sheet>
        <!--        </v-col>-->

      </v-col>
    </v-row>
<!--    <v-row align="center" class="pt-6">-->
<!--      <v-divider></v-divider>-->
<!--    </v-row>-->
    <v-row align="center" class="pt-6">
      <v-col cols="2">
        <v-sheet :class="itemsClass">Disease Name:</v-sheet>
        <v-sheet  :class="itemsContentClass"> {{ dat.data.name }}</v-sheet>
      </v-col>
      <v-col cols="2">
        <v-sheet :class="itemsClass">Disease Ontology ID:</v-sheet>
        <v-sheet  :class="itemsContentClass" >
          <a style="text-decoration: none" class="teal--text" :href="$commonfunc.renderLinkDOID(dat.data.doid)" target="_blank">{{ dat.data.doid }}</a>
        </v-sheet>
      </v-col>
      <v-col cols="2">
        <v-sheet :class="itemsClass">MeSH ID:</v-sheet>
        <v-sheet  :class="itemsContentClass" >
          <a  style="text-decoration: none" class="teal--text" :href="$commonfunc.renderLinkMESHID(dat.data.MESHID.replace('MESH:',''))" target="_blank">{{ dat.data.MESHID.replace('MESH:','') }} &nbsp;&nbsp;</a>
        </v-sheet>
      </v-col>
      <v-col cols="6">
        <v-sheet :class="itemsClass">Parent Disease Ontology ID:</v-sheet>
        <v-sheet  :class="itemsContentClass">
          <a :key="x" v-for="x in dat.data.is_a" style="text-decoration: none" class="teal--text" :href="$commonfunc.renderLinkDOID(x)" target="_blank">{{ x }} &nbsp;&nbsp;</a>

        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="center" class="pt-6">
      <v-col cols="4">
          <v-card elevation="0" width="100%">
            <v-card-title class="text-h5">MeSH Terms Related To The Disease:</v-card-title>
            <v-card-text>
              <v-list class="overflow-y-auto" height="200"  width="100%" >
                <v-list-item v-for="x in dat.data.MESH_Terms" :key="x">
                 <v-icon color="teal"> mdi-label-variant-outline</v-icon>&nbsp;&nbsp; {{ x }}
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
      </v-col>
      <v-col cols="4">
        <v-card elevation="0" width="100%" >
          <v-card-title class="text-h5">Synonyms Of The Disease:</v-card-title>
          <v-card-text>
            <v-list class="overflow-y-auto" height="200" width="100%">
              <v-list-item v-for="(x,idx) in dat.data.synonyms" :key="idx">
                <v-icon color="teal"> mdi-label-variant-outline</v-icon>&nbsp;&nbsp; <b>Name:</b> {{ x.name }} &nbsp;<b>Scope:</b>{{x.scope}}
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card elevation="0" width="100%" >
          <v-card-title class="text-h5" >Cross Reference To Other IDs:</v-card-title>
          <v-card-text>
            <v-list class="overflow-y-auto" height="200" width="100%">
              <v-list-item v-for="(x,idx) in dat.data.xref" :key="idx">
                <v-icon color="teal">mdi-label-variant-outline</v-icon> &nbsp;&nbsp;  {{x}}
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-spacer>

      </v-spacer>
      <v-col cols="2">
        <v-btn
        color="teal"
        rounded
        elevation="0"
        dark
        @click="downloadEvt('http://ngdc.cncb.ac.cn/ccas/api/download_sqlite3?jobid='+$route.params.jobid)"
        >Download annotation results</v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import Axios from "axios"
import CommonHelpMessage from "../sub/commonHelpMessage";
export default {
  name: "subOverviewDiseaseOverview",
  components: {CommonHelpMessage},
  props: ['dat'],
  data() {
    return {
      itemsClass: [
        "text-h5",
      ],
      itemsContentClass:[
        "mt-1",
        "text-body-1"
      ]
    }
  },
  methods:{
    downloadData(){
      Axios.post(
        "/ccas/api/download_sqlite3",
        {},
        {
          params:{
            jobid:this.route.params.jobid
          }
        }
      ).then(()=>{


      })
    },
    downloadEvt(url) {
  window.location.href = url;
  }
  }

}
</script>

<style scoped>

</style>
