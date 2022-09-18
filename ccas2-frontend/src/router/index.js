import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import checkResults from '@/components/checkResults'
import annoresults from "../components/annoresults";
import geneDetail from "../components/geneDetail";
import help from "../components/help";
import map from '../components/map'
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      meta:{
        title:"Home-CCAS-CNCB-NGDC"
      }
    },

    {
      path: '/home',
      name: 'home',
      component: home,
      meta:{
        title:"Home-CCAS-CNCB-NGDC"
      }
    },
    {
      path: '/checkresults',
      name: 'checkresults',
      component: checkResults,
      meta:{
        title:"Check Results-CCAS-CNCB-NGDC"
      }
    },
    {
      path: '/annoresults:jobid',
      name: 'annoresults',
      component: annoresults,
      meta:{
        title:"Results-CCAS-CNCB-NGDC"
      }
    },
    {
      path: '/genedetail:jobid:geneid',
      name: 'genedetail',
      component: geneDetail,
      meta:{
        title:"Gene Details-CCAS-CNCB-NGDC"
      }
    },
    {
      path: '/help',
      name: 'help',
      component: help
    },
    {
      path: '/map',
      name: 'map',
      component: map
    },
  ],

})
router.beforeEach((to,form,next)=>{
  if(to.meta.title){
    document.title = to.meta.title;
  }
  next();
})
export default  router
