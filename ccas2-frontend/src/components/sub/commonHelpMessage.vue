<template>

  <v-menu
    open-on-hover
    bottom
    offset-y

  >
    <template v-slot:activator="{ on, attrs }">

      <v-icon
        color="teal"
        dark
        v-bind="attrs"
        v-on="on"
        small
      >mdi-help-circle-outline</v-icon>

    </template>
    <v-sheet rounded max-width="600" color="white" elevation="99" class="pa-2 text-justify" >
      <slot>

      </slot>
    </v-sheet>

  </v-menu>
</template>

<script>
export default {
  name: "commonHelpMessage"
}
</script>

<style scoped>

</style>
