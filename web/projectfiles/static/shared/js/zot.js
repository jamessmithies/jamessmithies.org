<style type="text/css" id="zoterostylesheet" scoped>
.bibshowhide {display:none;}
.abstract {display:none;}
.blink {margin:0;margin-right:15px;padding:0;display:none;}
</style>
<script type="text/javascript">
 function downloadFile(elem) {
  filename = "article.ris"
  if (elem.parentNode) {
    var elems = elem.parentNode.getElementsByTagName('*');
    for (i in elems) {
        if((' ' + elems[i].className + ' ').indexOf(' ' + 'bibshowhide' + ' ') > -1) 
           {
  var ee = elems[i]
  if (ee.childNodes[0]) { ee = ee.childNodes[0] } 
  var pom = document.createElement('a');
  pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(ee.innerHTML));
  pom.setAttribute('download', filename);
  pom.click();
}}}}
function show(elem) {
  if (elem.parentNode) {
   var elems = elem.parentNode.getElementsByTagName('*'), i;
    for (i in elems) {
        if((' ' + elems[i].className + ' ').indexOf(' ' + 'bibshowhide' + ' ') > -1) 
           { if (elems[i].style.display == 'block') {elems[i].style.display = 'none';} else {elems[i].style.display = 'block';}}}}
  return(void(0));}
function changeCSS() {
  if (!document.styleSheets) return;
  var theRules = new Array();
    //ss = document.styleSheets[document.styleSheets.length-1];
    var ss = document.getElementById('zoterostylesheet');
    if (ss) {
    ss = ss.sheet
  if (ss.cssRules)
    theRules = ss.cssRules
  else if (ss.rules)
    theRules = ss.rules
  else return;
  theRules[theRules.length-2].style.display = 'inline';
    theRules[theRules.length-1].style.display = 'inline';
    }
    }
changeCSS();</script>