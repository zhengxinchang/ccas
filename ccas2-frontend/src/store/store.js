import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    doid_list:null,
    doid_dict:null,
    doid_dict2list:null,
    // mainColor:'#DA664D',
    demoJobid:"20220503124420_3f197fd9-87c1-4b28-bf42-d2ad59c8ff18",
    mainColor:'#115270',
    selected_doid:null,
    currentTab:0,
    // mainColor:'#ce1c2c',
    // stats:null,
  },
  mutations: {
    setTabWith (state,tab) {
      state.currentTab=tab
    },
    assignStats(state,s){
      state.stats = s;
    },
    assignDiseaseTree(state,dtree){
      state.doid_list = dtree;
    },
    assignDiseaseDict(state,d){
      state.doid_dict = d;
    },
    assignDiseaseDict2list(state,d){
      state.doid_dict2list = d;
    },
    assignDOID(state,doid){
      state.selected_doid = doid
    },
  },

  actions:{
    // loadStats(context){
    //
    //   Axios.post(
    //     "/api/get_stats"
    //   ).then((response)=>{
    //     console.log("successfully retrival stats");
    //     context.commit("assignStats",response.data)
    //   }).catch((err)=>{
    //     console.log(err);
    //   });
    // },

    loadingDiseaseTree(context){
      Axios
        .post(
          "/ccas/api/get_home_disease_tree",
        )
        .then(function (response) {
          let data = response.data.data
          console.log("Successful reterival disease tree data...")

          context.commit("assignDiseaseTree",data.tree);
          context.commit("assignDiseaseDict",data.dict);

          let data_dict_list = []
          for(let x in data.dict){
            data_dict_list.push(
              data.dict[x][x]
            )
          }
          context.commit("assignDiseaseDict2list",data_dict_list);
        })
        .catch((err) => {
          console.log(err)
        });

    }

  },
  getters:{

  }
})
