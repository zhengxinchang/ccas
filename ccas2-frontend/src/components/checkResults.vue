<template>
  <v-container class="container--fluid">
    <v-sheet class="z-transparent" style="margin-top: 120px;">

    </v-sheet>
    <v-row align="center">
      <v-col cols="12">
        <v-sheet min-height="60" max-height="60" rounded class="px4 mx-6" >
              <v-row dense align="center">
                <v-col>
                  <v-breadcrumbs :items="[{text:'home',disabled:false,href:'/home'},{text:'check results',disabled:true}]"></v-breadcrumbs>
                </v-col>
              </v-row>

        </v-sheet>
      </v-col>

    </v-row>
    <v-row >
      <v-col>
        <v-sheet min-height="700"  rounded class="px-4 mx-6 z-transparent" >
          <v-row align="center">
            <v-spacer></v-spacer>
            <v-col  cols="7">

              <v-card min-height="300" style="margin-top: 100px;" class="text-justify text-body-1 pa-6">

                <v-card-title ><v-sheet class="teal--text">Check Results</v-sheet></v-card-title>
                <v-divider :style="{color:$store.state.mainColor}" class="my-2"></v-divider>
                <v-sheet>
                  Please enter the jobid you received on the home page(and in the email if you provided) to retrieve all annotation results.
                </v-sheet>
                  <v-sheet rounded outlined class="pa-4 my-4" :style="{color:$store.state.mainColor}">
                    <v-row >
                      <v-col cols="2"  class="text-right">
                        <v-icon color="teal" large>mdi-identifier</v-icon>
                      </v-col>
                      <v-col cols="9" class="text-left">
                        <v-text-field
                          v-model="jobid"
                          clearable
                          dense
                          flat
                          hide-details
                          label="Job ID"
                          :rules="[rules.required]"
                          rounded
                          solo-inverted
                        ></v-text-field>
                      </v-col>
                      <v-spacer></v-spacer>
                    </v-row>
                    <v-row>
                      <v-col cols="6" class="text-right" >
                        <v-btn
                          :loading="isloadingres"
                          class="mx-auto text-body-2"
                          color="red"
                          dark
                          outlined
                          width="60%"
                          @click="loadRealReults"
                        >
                          <v-icon dense>mdi-magnify</v-icon>
                          Check
                        </v-btn>
                      </v-col>
                      <v-col cols="6"  class="text-left">
                        <v-btn

                          class="mx-auto text-body-2"
                          color="teal"
                          dark
                          width="60%"
                          outlined
                          @click="loadDemo"
                        >
                          <v-icon>
                            mdi-lifebuoy
                          </v-icon>
                          demo
                        </v-btn>
                      </v-col>
                    </v-row>

                  </v-sheet>
                <v-sheet>
                  It should be noted that:
                  <ul>
                    <li>In order to provide a user-friendly way to use CCAS, users can use all functions without logging in.</li>
                    <li>In order to protect the data uploaded by users, please don't give jobid to anyone you don't trust. </li>
                    <li>Tasks will only be saved on the server for 3 days. Please download the results in time.</li>
                  </ul>

                </v-sheet>


              </v-card>
            </v-col>
            <v-spacer></v-spacer>
          </v-row>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Axios from 'axios'
export default {
name: "checkResults",
  data(){
  return{
    isloadingres:false,
    jobid:null,
    rules:{
      required: value => !!value || 'Required.',
    }
  }
  },
  methods:{
    loadRealReults(){
      // this.$router.push('/annoresults/12345')
      // this.jobid = "20220426162231_d1b088df-ec5a-4cdb-8795-b849bfa95468"
      if(this.jobid != null){
          Axios.post(
            "/ccas/api/checkjob",
            {},
            {params:{
              jobid:this.jobid,
              }}
          ).then(res=>{
            if (res.data.status == "1:running"){

              alert("Job: "+this.jobid + " is still running. Please wait a few minutes and check it again.")
            }
            else if (res.data.status == "3:crashed"){

              alert("Job: "+this.jobid + " has some errors. This may be caused by incorrect input file format. Please check your input file and submit again. If you encounter this problem again, please contact email: zhengxichang@big.ac.cn .")
            }
            else if(res.data.status == "2:finished"){
              this.$router.push({ name: 'annoresults', params: { jobid: this.jobid }})
            }
          })
        // this.$router.push('/annoresults/'+this.jobid)

      }else{
        alert("Job id is emtpy! Please provide job id before click check button.")
      }

    },
    loadDemo(){
      // this.jobid = "20220426165759_396258a7-c7f3-4337-99b5-f757fb9f69d6"
      this.jobid = this.$store.state.demoJobid
      if(this.jobid != null){

        // this.$router.push('/annoresults/'+this.jobid)
        this.$router.push({ name: 'annoresults', params: { jobid: this.jobid }})
      }else{
        alert("Job id is emtpy! Please provide job id before click check button.")
      }
    }

  }
}
</script>

<style scoped>
.z-transparent {
  background-color: transparent !important;
  opacity: 1;
  border-color: transparent !important;
}
</style>
