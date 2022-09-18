<template>
  <v-app id="app" style="margin-top: 0px;background-color: #ecf0f5;">
    <header-bar app style="position: fixed;width: 100%;top:0px;z-index: 999999"></header-bar>
    <v-sheet
      :color="barcolor"
      class="pb-3"
      style="position: fixed;width: 100%;z-index: 99999;top:30px"
    >
      <!--      color="#3c8dbc"-->
      <v-row align="center" style="min-height: 80px">
        <v-spacer></v-spacer>
        <v-col
          class="mx-2 pt-5" cols="12"
          lg="2"
          md="12"
          sm="12"
          xl="2"
        >
          <v-sheet :color="barcolor" @click="$router.push('/home')">
            <v-row dense align="center">
              <v-spacer></v-spacer>
              <v-col cols="6" >
                <span><v-img :src="logo" aspect-ratio="16/9" contain height="40"></v-img></span>
              </v-col>
<!--              <v-col cols="4">-->
<!--                <v-sheet :color="$store.state.mainColor" dark class="font-weight-bold text-h6" >-->
<!--                  <div class="white&#45;&#45;text text&#45;&#45;darken-1 "-->
<!--                  >-->
<!--                    <span class="yellow&#45;&#45;text text&#45;&#45;darken-2">C</span>-->
<!--                    <span class="teal&#45;&#45;text text&#45;&#45;accent-3">C</span>-->
<!--                    <span class="purple&#45;&#45;text ">A</span>-->
<!--                    <span class="deep-purple&#45;&#45;text text&#45;&#45;accent-4">S</span>-->
<!--                  </div>-->
<!--                </v-sheet>-->
<!--              </v-col>-->
              <v-spacer></v-spacer>
            </v-row>
          </v-sheet>

        </v-col>
        <v-col cols="2">
          <v-btn :color="$store.state.mainColor"
                 dark elevation="0" width="100%" height="50"
                 to="/home"
          >
            <v-icon>mdi-home</v-icon> &nbsp; Home
          </v-btn>
        </v-col>

        <v-col cols="2">
          <v-btn :color="$store.state.mainColor"
                 dark elevation="0" width="100%" height="50"
                  to="/checkresults"
          >
            <v-icon>mdi-chemical-weapon</v-icon> &nbsp; Check Results
          </v-btn>
        </v-col>
        <v-col cols="2">
          <v-btn :color="$store.state.mainColor"
                 dark elevation="0"
                 width="100%" height="50"
                @click="openExternalLink"
          >
            <v-icon>mdi-cards-heart-outline</v-icon> &nbsp; help
          </v-btn>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
    </v-sheet>
    <router-view/>
    <footer-bar class="mt-4"></footer-bar>
  </v-app>
</template>

<script>
import HeaderBar from "./components/HeaderBar";
import FooterBar from "./components/FooterBar";

export default {
  name: 'App',
  components: {FooterBar, HeaderBar},
  data() {
    return {
      logo: require('./assets/logo2.png'),
      barcolor: this.$store.state.mainColor,
      headerbarClass: []
    }
  },
  methods: {
    openExternalLink() {
      // console.log("aaaaa")
      window.open('https://ngdc.cncb.ac.cn/ccas/docs/#/')
      // console.log(this.$store.state.currentTab)
      // this.$store.commit('setTabWith', 1)
    }
  },
  watch: {
    // '$store.state.currentTab':function(){
    //   console.log(this.$store.state.currentTab)
    // }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
