
// 渲染外链
function renderBase(id, baseURL) {
  //设置如果值为 null "NULL" "NA" 的时候直接返回false
  if (id == false || id === 'NULL' || id === "NA" || id == null) return false;

  let url = baseURL + id
  return (url)
}
function renderLinkEnsemblGene(id) {
  let baseURL = "https://asia.ensembl.org/Homo_sapiens/Gene/Summary?g="
  return (renderBase(id, baseURL))
}
function renderLinkEntrezGene(id) {
  let baseURL = "https://www.ncbi.nlm.nih.gov/gene/"
  return (renderBase(id, baseURL))
}
function renderLinkNCTID(id) {
  let baseURL = "https://clinicaltrials.gov/ct2/show/"
  return (renderBase(id, baseURL))
}
function renderLinkUCSCGene(id) {
  let baseURL = "https://www.ncbi.nlm.nih.gov/gene/"
  return (renderBase(id, baseURL))
}
function renderLinkPDB(id) {
  let baseURL = "https://www.rcsb.org/structure/"
  return (renderBase(id, baseURL))
}

// function renderLinkReactome(id){
//   let baseURL = "https://reactome.org/content/detail/"
//   return (renderBase(id, baseURL))
// }

function  renderLinkDbsnp(id){
  // https://www.ncbi.nlm.nih.gov/snp/
  let baseURL = "https://www.ncbi.nlm.nih.gov/snp/"
  return (renderBase(id, baseURL))
}

function renderLinkChembl(id){
  let baseURL="https://www.ebi.ac.uk/chembl/compound_report_card/";
  return(renderBase(id,baseURL))
}

function renderLinkReactome(id) {
  let baseURL = "https://reactome.org/content/detail/"
  return (renderBase(id, baseURL))
}
function renderLinkHGNC(id) {
  let baseURL = "https://www.genenames.org/tools/search/#!/?query="
  return (renderBase(id, baseURL))
}

function renderUniport(id) {
  let baseURL = "https://www.uniprot.org/uniprot/"
  if (id.constructor == Array) {
    if (id.length > 0) {
      // console.log("idlength >0")
      let out = []
      id.forEach(oneid => {
        out.push({ name: oneid, url: renderBase(oneid, baseURL) })
      });
      return (out)
    } else {
      console.log("idlength is 0")
      return ([])
    }
  } else {
    // console.log("not an array ")
    return (renderBase(id, baseURL))
  }

}

function  renderLinkDOID(id){
  // https://www.ncbi.nlm.nih.gov/snp/
  let baseURL = "http://www.disease-ontology.org/?id="
  return (renderBase(id, baseURL))
}

function  renderLinkMESHID(id){
  // https://www.ncbi.nlm.nih.gov/snp/
  let baseURL = "https://www.ncbi.nlm.nih.gov/mesh/?term="
  return (renderBase(id, baseURL))
}

function renderPubmed(id) {

  let baseURL = "https://pubmed.ncbi.nlm.nih.gov/"
  if (id.constructor == Array) {
    if (id.length > 0) {
      console.log("idlength >0")
      let out = []
      id.forEach(oneid => {
        out.push({ name: oneid, url: renderBase(oneid, baseURL) })
      });
      return (out)
    } else {
      console.log("idlength is 0")
      return ([])
    }
  } else {
    // console.log("not an array ")
    return (renderBase(id, baseURL))
  }
}

function renderPubmedTagA(id){
  if (id.constructor == Array) {
    if (id.length > 0) {
      // console.log("idlength >0")
      let out = []
      id.forEach(oneid => {
        let link = renderPubmed(oneid)
        out.push(
          `<a href="${link}" target="_blank" >${oneid}</a>`
        )
      });
      return (out)
    } else {
      // console.log("idlength is 0")
      return ([])
    }
  } else {
    // console.log("not an array ")
    let onelink = renderPubmed(id)
    return (`<a href="${onelink}" target="_blank" >${id}</a>`)
  }
}

function renderPubmedInText(text) {
  let pmidlist = text.match(/PubMed:\d+/g) || [];
  // console.log(pmidlist)
  if (pmidlist.length > 0) {
    pmidlist = pmidlist.sort();
    pmidlist.forEach((pmid) => {
      text = text.replace(
        pmid,
        `<a href="${renderPubmed(
          pmid.replace("PubMed:", "")
        )}" target="_blank">${pmid.replace("PubMed:", "PMID:")}</a>`
      );
    });
  } else {
    return (text)
  }
}


function drugs_nct_url2nct_name_url(urlstr) {
  let datlist = urlstr.split(/\|+/) || []
  if(datlist.length == 0){
    return( [])
  }else{

    let datlistdict = datlist.map(item=>{
      let newitem = {}

      // api.fda.gov
      // clinicaltrials.gov
      // dailymed.nlm.nih.gov
      // www.accessdata.fda.gov
      // www.whocc.no

      let test_clintrailsgov = new RegExp(/clinicaltrials\.gov/)
      let test_who = new RegExp(/www\.whocc\.no/)
      let test_fda = new RegExp(/www\.accessdata\.fda\.gov/)
      let test_dailymed = new RegExp(/dailymed\.nlm\.nih\.gov/)

      newitem.url = item

      if(test_clintrailsgov.test(item)){
        // newitem.name = "ClinicalTrials.gov"
        newitem.name =item.replace("https://clinicaltrials.gov/search?id=%22","").replace("%22","")
        return newitem
      }

      if(test_who.test(item)){
        newitem.name = "WHOCC"
        return newitem
      }

      if(test_fda.test(item)){
        newitem.name = "FDA"
        return newitem
      }
      if(test_dailymed.test(item)){
        newitem.name = "Dailymed"
        return newitem
      }

      newitem.name = "Others"
      return newitem;
    }).filter(itm=>{
      return itm.name != "Others"
    })
    return datlistdict;
  }

}

export default {
  renderLinkEnsemblGene,
  renderLinkReactome,
  renderLinkHGNC,
  renderLinkDOID,
  renderUniport,
  renderLinkMESHID,
  renderPubmed,
  renderLinkChembl,
  renderPubmedInText,
  renderPubmedTagA,
  renderLinkDbsnp,
  drugs_nct_url2nct_name_url,
  renderLinkEntrezGene,
  renderLinkUCSCGene,
  renderLinkPDB,
  renderLinkNCTID,
}
