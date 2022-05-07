<template>
  <v-sheet class="mx-3">
    <v-row class="pt-6">
      <v-col cols="12">
        <v-sheet>
          <v-row>
            <v-col cols="12">
              <div class="text-h6 text-left mx-12">
                Mutation signature pattern of user's uploaded somatic cancer genome

              </div>
              <div class="text-body-2 text-left mx-12">
                The profile of each signature is displayed using the six substitution subtypes: C>A, C>G, C>T, T>A, T>C,
                and T>G (all substitutions are referred to by the pyrimidine of the mutated Watson–Crick base pair).
                Further, each of the substitutions is examined by incorporating information on the bases immediately 5’
                and 3’ to each mutated base generating 96 possible mutation types. Mutational signatures are displayed
                and reported based on the observed trinucleotide frequency of the human genome.
              </div>

              <div
                id="sig_heatmap_pattern"
                ref="sig_heatmap_pattern"
                class="ma-3 mx-auto"
                style="width: 800px;height: 500px;margin:auto;"
              >

              </div>

            </v-col>
            <v-col cols="12">

              <div class="text-h6 text-left mx-12">
                Signature similarity with COSMIC
              </div>
              <div class="text-body-2 text-left mx-12">
                Takes sample information in the form of the fraction of mutations in each of 96 trinucleotide contexts
                and identifies the weighted combination of COSMIC mutation signatures to reconstruct the tumor profile.
                Signatures closer to COSMIC are marked with darker color.
              </div>

              <div
                id="sign_heatmap_polar"
                ref="sign_heatmap_polar"
                class="ma-3 mx-auto"
                style="width: 500px;height: 500px;margin:auto;"
              >
              </div>
              <div class="text-h6 text-left mx-12">
                References:
              </div>
              <div class="text-body-2 text-left mx-12">
                Rosenthal, R., McGranahan, N., Herrero, J., Taylor, B.S. and Swanton, C. (2016) DeconstructSigs:
                delineating mutational processes in single tumors distinguishes DNA repair deficiencies and patterns of
                carcinoma evolution. <b>Genome Biol.</b>, 17, 31.
              </div>

            </v-col>
          </v-row>

        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="12">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://cancer.sanger.ac.uk/signatures/signatures_v2/" small
          style="text-transform: none"
          target="_blank"> COSMIC
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="http://cran.wustl.edu/web/packages/deconstructSigs/index.html"
          small style="text-transform: none"
          target="_blank"> deconstructSigs
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import Axios from "axios"
export default {
  name: "subOverviewMutSignature",
  props: ["jobid"],
  data(){
    return{
      mutsigdata:{
        desc:{},
        pattern:[],
        similar:[],
      }
    }
  },
  watch:{
    'jobid': {
      handler: function (jobid) {
        console.log("mut sig job id chage")



      },
      deep: true,
      immediate: true
    },
  },
  mounted() {
    // let that = this
    // that.loadData(this.jobid).then(res=>{
    //   that.drawPlot()
    // }).catch(err=>{
    //   console.log(err)
    // })

    let loadTumorSigPattern = new Promise((resolve, reject) => {
      Axios.post(
        "/ccas/api/get_overview_tumor_signature",
        {},
        {
          params:{
            jobid:this.jobid
          }
        }
      ).then(res=>{
        // mutsigdata.pattern = res.data.data
        resolve(res.data.data)
      })
    })

    let loadTumorSigSimilar = new Promise((resolve, reject) => {
      Axios.post(
        "/ccas/api/get_overview_signature_similarity",
        {},
        {
          params:{
            jobid:this.jobid
          }
        }
      ).then(res=>{

        // mutsigdata.similar = res.data.data
        resolve(res.data.data)
      })
    })


    let loadSigDesc = new Promise((resolve, reject) => {
      Axios.post(
        "/ccas/api/get_overview_signature_desc",
      ).then(res=>{
        // mutsigdata.desc = res.data.data
        resolve(res.data.data)

      })
    })

    Promise.all([loadTumorSigPattern,loadTumorSigSimilar,loadSigDesc]).then(res=>{

      let mutsigdata = {

        pattern:res[0],
        similar:res[1],
        desc:res[2],
      }

      this.drawPlot(mutsigdata)
    })
  },
  methods:{
    loadData(jobid){

    },
    drawPlot(mutsigdata){
      console.log(mutsigdata)
      console.log("mutsigdata")
      const drawID = this.$refs.sign_heatmap_polar
      // if (drawID){
      let mydata = mutsigdata.similar;
      let chartDom = document.getElementById('sign_heatmap_polar');
      let myChart = this.$echarts.init(chartDom);
      let option;
      function renderItem(params, api) {
        var values = [api.value(0), api.value(1)];
        var coord = api.coord(values);
        var size = api.size([1, 1], values);
        return {
          type: 'sector',
          shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r0: coord[2] - size[0] / 2,
            r: coord[2] + size[0] / 2,
            startAngle: -(coord[3] + size[1] / 2),
            endAngle: -(coord[3] - size[1] / 2)
          },
          style: api.style({
            fill: api.visual('color')
          })
        };
      }
      let hours = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20", "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28", "S29", "S30"];
      let days = [' ', ' ', ' ', ' ', ' ', ' ', 'Signature'];
      let maxValue = mydata.reduce(function (max, item) {
        return Math.max(max, item[2]);
      }, -Infinity)

      let that = this
      option = {
        legend: {
          data: ['Punch Card'],
          // x:"right"
        },
        polar: {},
        tooltip: {
          trigger: 'item',

          formatter: function (data) {
            // return data[0]+ '<br/>' +data[1] + '：'+(data[2] * 100)+'%'; //将小数转化为百分数显示
            // console.log(Signaturedesc['S1']);
            // console.log(JSON.stringify(  mutsigdata.desc[data.value[1]]));
            // return "<b>" + data.name + '</b>: ' + data.data[1] + '<br/><br/> <b>Comments: </b>' + this.mutsigdata.desc [data.data[1]]['Comments'] + '</br> <b>Additional Features：</b>' + this.mutsigdata.desc[data.data[1]]['AdditionalFeatures'] + '</br> <b>Cancer Types：</b>' + this.mutsigdata.desc[data.data[1]]['CancerTypes'] + '</br> <b>Proposed Aetiology：</b>' + this.mutsigdata.desc[data.data[1]]['ProposedAetiology'] + '</br><b> Similarity：</b>' + data.value[2];
            return '<div class="text-left"><br/><b>Comments: </b>' + mutsigdata.desc [data.value[1]]['Comments'] + '</br> <b>Additional Features：</b>' + mutsigdata.desc[data.value[1]]['AdditionalFeatures'] + '</br> <b>Cancer Types：</b>' + mutsigdata.desc[data.value[1]]['CancerTypes'] + '</br> <b>Proposed Aetiology：</b>' + mutsigdata.desc[data.value[1]]['ProposedAetiology'] + '</br><b> Similarity：</b>' + data.value[2] +'</div>';
          },
          extraCssText: 'width:420px; white-space:pre-wrap'//额外附加到浮层的 css 样式 ;white-space:pre-wrap的作用是保留空格，并且除了碰到源码中的换行和<br/>会换行外，还会自适应容器的边界进行换行。

        },
        grid: {
          height: '70%',
          top: '10%',
          left: "15%",
          width: "75%"
        },
        visualMap: {
          type: 'continuous',
          min: 0.0,
          max: maxValue,
          top: 'middle',
          // left:"right",

          right:5,
          dimension: 2,
          calculable: true,
          precision: 0,
          padding:5
        },
        angleAxis: {
          type: 'category',
          data: hours,
          boundaryGap: false,
          splitLine: {
            show: false,
            lineStyle: {
              color: '#ddd',
              type: 'dashed'
            }
          },
          axisLine: {
            show: false
          },
          axisLabel: {
            interval: 0
          }
        },
        radiusAxis: {
          type: 'category',
          data: days,
          show: false,
          z: 100
        },
        series: [{
          name: 'Similarity',
          type: 'custom',
          coordinateSystem: 'polar',
          itemStyle: {
            color: '#dc1a47',
            shadowBlur: 4,
            shadowColor: 'rgba(0, 0, 0, 0.9)'
          },
          center: ['50%', '50%'],
          renderItem: renderItem,
          data: mydata,
          // emphasis: {
          //     itemStyle: {
          //         shadowBlur: 10,
          //         shadowColor: 'rgba(0, 0, 0, 0.9)'
          //     }
          // }
        }]
      };
      myChart.setOption(option);
      window.addEventListener("resize", function() {
        myChart.resize()
      });




      let mydataMutPattern = mutsigdata.pattern
      var chartDomMutPattern = document.getElementById('sig_heatmap_pattern');
      var myChartMutPattern = this.$echarts.init(this.$refs.sig_heatmap_pattern);
      var optionMutPattern;

      var v_axis = ["A[*]A", "A[*]C", "A[*]G", "A[*]T", "C[*]A", "C[*]C", "C[*]G", "C[*]T", "G[*]A", "G[*]C", "G[*]G", "G[*]T", "T[*]A", "T[*]C", "T[*]G", "T[*]T"];
      var h_axis = ['C>A', "C>G", "C>T", "T>A", "T>C", "T>G"];


      // console.log(data);

      let maxValueMutPattern = mydataMutPattern.reduce(function (max, item) {
        return Math.max(max, item[2]);
      }, -Infinity)

      mydataMutPattern = mydataMutPattern.map(function (item) {
        // return [item[1], item[0], item[2] || '-'];
        return [item[1], item[0], item[2]];
      });

      // console.log(data);

      optionMutPattern = {
        tooltip: {
          trigger: 'item',

          formatter: function (data) {
            // return data[0]+ '<br/>' +data[1] + '：'+(data[2] * 100)+'%'; //将小数转化为百分数显示
            // console.log(Signaturedesc['S1']);
            // console.log(data);
            // console.log(data);
            let mypattern = data.data[1].split(/\*/);

            return "<b>Pattern</b></br>" + mypattern[0] + data.data[0] + mypattern[1] + " : " + data.data[2];
          }
        },
        grid: {
          height: '70%',
          top: '10%',
          left: "15%",
          width: "75%"
        },
        xAxis: {
          type: 'category',
          data: h_axis,
          splitArea: {
            show: true
          }
        },
        yAxis: {
          type: 'category',
          data: v_axis,
          splitArea: {
            show: true
          }
        },
        visualMap: {
          min: 0,
          max: maxValueMutPattern,
          calculable: true,
          padding: 5,
          // left: "auto",
          right: 5,
          bottom: "middle",
          inRange: {
            color: ['WhiteSmoke', 'SteelBlue']
          },
          precision: 2

        },
        series: [{
          name: 'Pattern',
          type: 'heatmap',
          data: mydataMutPattern,
          center:["50%","50%"],
          label: {
            show: true
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.9)'
            }
          }
        }]
      };

      optionMutPattern && myChartMutPattern.setOption(optionMutPattern);

      window.addEventListener("resize", function() {
        myChartMutPattern.resize()
      });
    }
  }

}
</script>

<style scoped>

</style>
