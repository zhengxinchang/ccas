<template>
  <div id="ssgsea" style="width:900px;height: 2000px"></div>
</template>

<script>
import Axios from 'axios'
export default {
name: "subOverviewSSGSEA_echarts_bar",
  props:['jobid'],
  data(){
    return{
      myChart:null,
    }
  },
  mounted() {
    this.myChart = this.$echarts.init(document.getElementById('ssgsea'));
    // this.loadDataAndPlot()
  },
  methods:{
    loadDataAndPlot(){
      Axios.post(
        "/ccas/api/get_overview_ssgsea_raw",
        {},
        {
          params:{
            jobid:this.jobid
          }
        }
      ).then(res=>{
        let data = res.data.data
        console.log(data)
        console.log(data.map((x)=>{return x.Value}))
        let options = {
          dataset: {
            // 用 dimensions 指定了维度的顺序。直角坐标系中，如果 X 轴 type 为 category，
            // 默认把第一个维度映射到 X 轴上，后面维度映射到 Y 轴上。
            // 如果不指定 dimensions，也可以通过指定 series.encode
            // 完成映射，参见后文。
            dimensions: [ 'Value','Name'],
            source: data
          },
          xAxis: {
            name:"Value",
            max:"1.0",
            min:"0.0",
          },
          yAxis:  {
            name:"Name",
            type:"category",
            data:data.map((x)=>{return x.Name}),
            inverse:true,
            axisLabel:{
              interval:0,
            }

          },
          series: [
            {
            data: data.map((x)=>{return x.Value}),
            type: 'bar',
              label:{
                show: true,
                position: "right"
              }

          }
          ]
        }

        this.myChart.setOption(options)
      })
    },
  },
  watch:{
  'jobid':{
    handler:function(){
      console.log("ssgsea charts jobid change...")
      this.loadDataAndPlot()
    },
    deep:true,
    immediate:true,
  }
  }
}
</script>

<style scoped>

</style>
