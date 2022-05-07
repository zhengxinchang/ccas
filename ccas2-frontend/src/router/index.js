import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import checkResults from '@/components/checkResults'
import annoresults from "../components/annoresults";
import geneDetail from "../components/geneDetail";
import help from "../components/help";

Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },

    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/checkresults',
      name: 'checkresults',
      component: checkResults
    },
    {
      path: '/annoresults:jobid',
      name: 'annoresults',
      component: annoresults,
    },
    {
      path: '/genedetail:jobid:geneid',
      name: 'genedetail',
      component: geneDetail
    },
    {
      path: '/help',
      name: 'help',
      component: help
    },
  ]
})
