<template>
<!--  首页点击器官分类图之后，出现的页面，通过menu实现。-->

  <div >


    <v-menu
    offset-overflow
    :close-on-content-click="false"
    :close-on-click="true"
    open-on-hover
    z-index="999999999"
    >
      <template v-slot:activator="{ on, attrs }">



        <v-avatar
          v-bind="attrs"
          v-on="on"
          :width="imgsize"
          :height="imgsize"
        >
          <img
            :src="image_url"
          >
        </v-avatar>

      </template>


      <v-card
      >
        <v-toolbar
          color="teal"
          dark
          dense
        >
          <v-toolbar-title
          >{{groupName}}
<!--           {{dat}}-->
          </v-toolbar-title>
        </v-toolbar>

        <v-sheet class="pa-4 teal lighten-2">
          <v-text-field
            v-model="search"
            label="Search..."
            dark
            flat
            solo-inverted
            hide-details
            clearable
            clear-icon="mdi-close-circle-outline"
          ></v-text-field>
        </v-sheet>

        <v-treeview
          :items="dat"
          activatable
          :active="active"
          @update:active="getActiveValue"
          :search="search"
          shaped
          hoverable
          open-all
          style="max-width: 500px;max-height: 600px;overflow-y: auto"
        >
          <template v-slot:label="{ item,leaf }">

            <span
            class="float-start "

            >{{item.name}}</span>
<!--            <span-->
<!--            v-else-->
<!--            class="float-start"-->
<!--            >-->
<!--              {{item.name}}-->
<!--            </span>-->
          </template>

        </v-treeview>

      </v-card>

    </v-menu>







  </div>
</template>

<script>
export default {
  name: "commonDoidGroup",
  props:[
    "dat", // 用于绘制treeview的数据
    "groupName", // 分组名称
    "image_url",
    "imgsize"
  ],
  data: () => ({
    active: [],
    search:null
  }),
  methods:{
    getActiveValue(value){

      // console.log("-----------------------")
      // console.log(value)
      if ( value[0] && value[0].indexOf("DOID") ==-1 ) {
        this.active = [];
      } else {
        // console.log(value)

        this.$store.commit("assignDOID",value[0])

      }
    }

  }

}
</script>

<style scoped>

</style>
