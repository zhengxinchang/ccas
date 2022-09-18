// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store/store";
import vuetify from '@/plugins/vuetify' // path to vuetify export
import 'xe-utils'
import VXETable from 'vxe-table'
import 'vxe-table/lib/style.css'
import i18n from './i18n'
Vue.config.productionTip = false
window.BASE_URL="/ccas"
import * as echarts from 'echarts';
Vue.prototype.$echarts = echarts;
import commonfunc from "./plugins/commonfunc";
Vue.prototype.$commonfunc = commonfunc;

import VueClipboard from "vue-clipboard2";
Vue.use(VueClipboard);

import _ from 'lodash'
Vue.prototype.$_ = _;

VXETable.setup({
  i18n: (key, args) => i18n.t(key, args)
})

Vue.use(VXETable)

router.afterEach((to,from, next) => {
  window.scrollTo(0,0)
})

if(process.env.NODE_ENV == "production"){
  window.baseURL="/ccas"
}else{
  window.baseURL=""
}
Vue.directive('title',{
  inserted: function(el){
    document.title = el.getAttribute('title')
    // console.log(el)
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  vuetify,
  components: { App },
  template: '<App/>'
})
