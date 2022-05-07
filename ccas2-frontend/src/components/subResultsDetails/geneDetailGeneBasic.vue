<template>
  <v-sheet class="mx-3">
    <v-row align="end" class="pt-6">
      <v-col class="text-center" cols="3">
        <v-sheet class="text-h3 mt-2">
          <!--          <v-sheet class=" grey&#45;&#45;text float-left text-body-2">Symbol</v-sheet>-->
          {{ dat.symbol || "NA" }}
        </v-sheet>
        <v-sheet class="text-h5 mt-2 ">
          {{ dat.name || "NA" }}
        </v-sheet>
      </v-col>
      <v-col class="text-left" cols="3">
        <v-sheet :class="itemsClass">Ensembl ID</v-sheet>
        <v-sheet :class="itemsContentClass">
          <a style="text-decoration: none" class="teal--text" :href="$commonfunc.renderLinkEnsemblGene(dat.geneid && dat.geneid.replace('GENEID:', ''))" target="_blank">{{ dat.geneid && dat.geneid.replace('GENEID:', '') }}</a>
        </v-sheet>
      </v-col>
      <v-col class="text-left" cols="2">
        <v-sheet :class="itemsClass">Entrez ID</v-sheet>
        <v-sheet :class="itemsContentClass">
          <a style="text-decoration: none" v-show="dat.entrezid != null" class="teal--text" :href=" dat.entrezid && $commonfunc.renderLinkEntrezGene(dat.entrezid ) || '#'" target="_blank">{{ dat.entrezid || "NA" }}</a>
          <v-sheet v-show="dat.entrezid == null" >NA</v-sheet>
        </v-sheet>
      </v-col>
      <v-col class="text-left" cols="2">
        <v-sheet :class="itemsClass">UCSC ID</v-sheet>
        <v-sheet :class="itemsContentClass">
<!--          <a style="text-decoration: none" v-show="dat.ucscid != null" class="teal&#45;&#45;text" :href=" dat.entrezid && $commonfunc.renderLinkUCSCGene(dat.ucscid ) || '#'" target="_blank">{{ dat.ucscid || "NA" }}</a>-->
<!--          <v-sheet v-show="dat.ucscid == null" >NA</v-sheet>-->

          {{ dat.ucscid || "NA" }}</v-sheet>
      </v-col>
      <v-col class="text-left" cols="2">
        <v-sheet :class="itemsClass">Uniprot ID</v-sheet>
        <v-sheet :class="itemsContentClass">
          <a style="text-decoration: none" v-show="dat.uniprotids != null" class="teal--text" :href=" dat.uniprotids && $commonfunc.renderUniport(dat.uniprotids ) || '#'" target="_blank">{{ dat.uniprotids || "NA" }}</a>
          <v-sheet v-show="dat.uniprotids == null" >NA</v-sheet>

        </v-sheet>
      </v-col>
    </v-row>
    <v-row class="pt-6">
      <v-divider></v-divider>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-col class="text-left" cols="3">
        <v-sheet :class="itemsClass">Location</v-sheet>
        <v-sheet :class="itemsContentClass">{{ dat.location || "NA" }}</v-sheet>
      </v-col>
      <v-col class="text-left" cols="3">
        <v-sheet :class="itemsClass">Locus Type</v-sheet>
        <v-sheet :class="itemsContentClass">{{ dat.locus_type || "NA" }}</v-sheet>
      </v-col>
      <v-col class="text-left" cols="3">
        <v-sheet :class="itemsClass">Gene Family</v-sheet>
        <v-sheet :class="itemsContentClass">{{
            dat.genefamily && dat.genefamily.replaceAll("|", "; ") || "NA"
          }}
        </v-sheet>
      </v-col>
      <v-col class="text-left" cols="3">
        <v-sheet :class="itemsClass">Protein Name</v-sheet>
        <v-sheet :class="itemsContentClass">{{
            dat.data.uniprot[0] && dat.data.uniprot[0].ProteinNameFull || "NA"
          }}
        </v-sheet>
      </v-col>
    </v-row>

    <v-row align="baseline" class="pt-6">

      <v-col class="text-left" cols="6">
        <v-sheet :class="itemsClass">Similarity</v-sheet>
        <v-sheet :class="itemsContentClass"> {{
            dat.data.uniprot[0] && dat.data.uniprot[0].Similarity || "NA"
          }}
        </v-sheet>
      </v-col>
      <!--      <v-col cols="6" class="text-left">-->
      <!--        <v-sheet :class="itemsClass">Accessions: </v-sheet>-->
      <!--        <v-sheet :class="itemsContentClass">{{   }}</v-sheet>-->
      <!--      </v-col>-->
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-col class="text-left" cols="3">
        <!--        {{ dat.data.uniprot[0] && dat.data.uniprot[0].SubcellualrLocation && dat.data.uniprot[0].SubcellualrLocation.replace(/\|\|+/g,", ") || "NA"  }}-->
        <v-sheet :class="itemsClass">Accessions</v-sheet>
        <v-sheet>
          <v-list :class="itemsListClass" height="200">
            <v-list-item
              v-for=" (x,idx) in (dat.data.uniprot[0] && dat.data.uniprot[0].AccesionList && dat.data.uniprot[0].AccesionList.split(/&&+/) || [] )"
              :key="idx"
              color="grey lighten-3">
              <v-icon color="teal"> mdi-label-variant-outline</v-icon>&nbsp;&nbsp;
              <a style="text-decoration: none" class="teal--text" :href=" $commonfunc.renderUniport(x )" target="_blank">{{ x || "NA" }}</a>

            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>
      <v-col class="text-left" cols="3">
        <!--        {{ dat.data.uniprot[0] && dat.data.uniprot[0].SubcellualrLocation && dat.data.uniprot[0].SubcellualrLocation.replace(/\|\|+/g,", ") || "NA"  }}-->
        <v-sheet :class="itemsClass">Related PDB ID</v-sheet>
        <v-sheet>
          <v-list :class="itemsListClass" height="200">
            <v-list-item
              v-for=" (x,idx) in (dat.data.uniprot[0] && dat.data.uniprot[0].PDBid && dat.data.uniprot[0].PDBid.split(/&&+/) || [] )"
              :key="idx">
              <v-icon color="teal"> mdi-label-variant-outline</v-icon>&nbsp;&nbsp;
              <a style="text-decoration: none" class="teal--text" :href=" $commonfunc.renderLinkPDB(x )" target="_blank">{{ x || "NA" }}</a>

            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>
      <v-col class="text-left" cols="3">
        <!--        {{ dat.data.uniprot[0] && dat.data.uniprot[0].SubcellualrLocation && dat.data.uniprot[0].SubcellualrLocation.replace(/\|\|+/g,", ") || "NA"  }}-->
        <v-sheet :class="itemsClass">SubCellular Location</v-sheet>
        <v-sheet>
          <v-list :class="itemsListClass" height="200">
            <v-list-item
              v-for=" (x,idx) in (dat.data.uniprot[0] && dat.data.uniprot[0].SubcellualrLocation && dat.data.uniprot[0].SubcellualrLocation.split(/\|\|+/) ||[])  "
              :key="idx">
              <v-icon color="teal"> mdi-label-variant-outline</v-icon>&nbsp;&nbsp;
              {{x}}
            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>


      <v-col class="text-left" cols="3">
        <v-sheet :class="itemsClass">Interactions:</v-sheet>
        <v-sheet>
          <v-list :class="itemsListClass" height="200">
            <v-list-item
              v-for=" (x,idx) in (dat.data.uniprot[0] && dat.data.uniprot[0].InteractionList && dat.data.uniprot[0].InteractionList.split(/&&+/) || [])  "
              :key="idx">
              <v-icon color="teal"> mdi-label-variant-outline</v-icon>&nbsp;&nbsp;{{ x }}
            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>


    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-col cols="6">
        <v-sheet :class="itemsClass">Function Description</v-sheet>
        <v-sheet class="overflow-y-auto text-body-2 text-justify py-2 px-4" color="grey lighten-4" height="200" rounded>
          {{ dat.data.uniprot[0] && dat.data.uniprot[0].FunctionList || "" }}
        </v-sheet>
      </v-col>
      <v-col cols="6">
        <v-sheet :class="itemsClass">Subunit Structure Description <span><common-help-message>This subsection provides information about the protein quaternary structure and interaction(s) with other proteins or protein complexes (with the exception of physiological receptor-ligand interactions which are annotated in the 'Function' section).</common-help-message></span> </v-sheet>
        <v-sheet class="overflow-y-auto text-body-2 text-justify py-2 px-4" color="grey lighten-4" height="200" rounded>
          {{ dat.data.uniprot[0] && dat.data.uniprot[0].SubunitFunctionList || "" }}
        </v-sheet>
      </v-col>
    </v-row>
    <v-row align="baseline" class="pt-6">
      <v-spacer></v-spacer>
      <v-col class="text-right font-weight-bold teal--text text--lighten-2" cols="2">Data from
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://www.uniprot.org/" small style="text-transform: none"
          target="_blank"> Uniprot
        </v-btn>
        <v-btn
          color="teal lighten-3" dark elevation="0" href="https://www.genenames.org/" small style="text-transform: none"
          target="_blank"> HGNC
        </v-btn>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import CommonHelpMessage from "../sub/commonHelpMessage";
export default {
  name: "geneDetailGeneBasic",
  components: {CommonHelpMessage},
  props: ['dat'],
  data() {
    return {
      itemsClass: [
        "text-h5",
        "text-left"
      ],
      itemsContentClass: [
        "mt-1",
        "text-body-1"
      ],
      itemsListClass: [
        "grey",
        "lighten-4",
        "rounded",
        "text-left",
        "overflow-y-auto",
        "text-body-2"
      ]
    }
  }
}
</script>

<style scoped>

</style>
