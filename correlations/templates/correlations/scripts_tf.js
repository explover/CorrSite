var popup=null;
var justCreated=0;
var winXScrollPos=0;
var winYScrollPos=0;
var newScrollX=0;
var newScrollY=0;
var pictCellWidth=400;
var tableHeightExt=130;
var curImage="#";

//=============================== Put image with path here !!!
function imageFile(img,chr){
	var imgFile=img;
	if(chr=="") imgFile=imgFile+".png";
	else imgFile=imgFile+"_"+chr+".png";
	return imgFile;
}
function showImage1(img,tbId, hImg, par_hash, chr_hash){
	var imgTable=document.getElementById("imgTable");
	if(imgTable.style.visibility="hidden"){
		imgTable.style.visibility="visible";
		imgTable.style.width=(pictCellWidth-40)+"px";
		setSize();
	}
	curImage=img;
	image=document.getElementById("tImage");
	image.src=imageFile(img,"");
	var hImage=document.getElementById("hImage");
	
	var allChromImage = document.getElementById("allChromImage");
	allChromImage.src = img + "_chr.png";


	var ss = hImg.split(";");
	
	var name1 = ss[1];
	if (name1.length>20){
		name1 = name1.substring(0, 20) + "...";
	}
	
	var name2 = ss[4];
	if (name2.length>20){
		name2 = name2.substring(0, 20) + "...";
	}
	
	var rep1 = ss[2];
	if (rep1.length>5){
		rep1 = rep1.substring(0, 5) + "..";
	}
	
	var rep2 = ss[5];
	if (rep2.length>5){
		rep2 = rep2.substring(0, 5) + "..";
	}
		
	hImage.innerHTML="<table border=\"0\" cellspacing=\"0\" cellpadding=\"2\" style=\"width: 100%;\"><tr><td style=\"width:10%;\">set1:</td><td  title=\"" + ss[0] +  "\" style=\"width:20%;\">" + ss[0] + "</td><td title=\"" + ss[1] +  "\" style=\"width:50%;\">"+ name1+"</td><td title=\"" + ss[2] +  "\">" + rep1 + "</td></tr><tr style=\"height:18px;\"><td>set2:</td><td title=\"" + ss[3] +  "\">" + ss[3] + "</td><td title=\"" + ss[4] +  "\">" + name2 + "</td><td title=\"" + ss[5] + "\">" + rep2 + "</td></tr></table>";//"<b>"+hImg+"</b>";//

	var curChrom=document.getElementById("curChrom");
	curChrom.innerHTML="";
	
	var value=par_hash["corr"]
	var cor=document.getElementById("corr");
	cor.innerHTML=value;
	var ccAll = document.getElementById("cc_all");
	ccAll.innerHTML=value;
	
	value=par_hash["observ"]
	var nObs = document.getElementById("observ");
	nObs.innerHTML=value;
	var obsAll = document.getElementById("obs_all");
	obsAll.innerHTML=value;
	
	value=par_hash["stDev"]
	var dev = document.getElementById("stDev");
	dev.innerHTML=value;

	value=par_hash["bgCorr"]
	var bgCor = document.getElementById("BgCorr");
	bgCor.innerHTML=value;
	
	value=par_hash["bgStDev"]
	var bgDev = document.getElementById("BgStDev");
	bgDev.innerHTML=value;
	
	value=par_hash["pval"]
	var pv=document.getElementById("pval");
	pv.innerHTML=value
	
	value=par_hash["mW"]
	var mw=document.getElementById("mw");
	mw.innerHTML=value;

	var chrCorr=document.getElementById("chrCorr")
	chrCorr.innerHTML = ""
	
	var chrObserv=document.getElementById("chrObserv")
	chrObserv.innerHTML = ""

	
	for(var chr in chr_hash){
		var ss=(chr_hash[chr]).split(' ');

		var cc_chr=document.getElementById("cc_" + chr);
		cc_chr.innerHTML=ss[0];
		
		
		var obs_chr=document.getElementById("obs_" + chr);
		obs_chr.innerHTML=ss[1];
		
	}

}
function hideImage1(){
	var imgTable=document.getElementById("imgTable");
	imgTable.style.visibility="hidden";
	var cImage = document.getElementById("cImage");
	cImage.style.visibility="hidden";
	var chromList=document.getElementById("chromList");
	chromList.style.visibility="hidden";
	imgTable.style.width="0px";
	setSize();
}
function hideImage2(){
	var cImage = document.getElementById("cImage");
	cImage.style.visibility="hidden";
}
function showStat(){
	var statList=document.getElementById("statist");
	var pos=getAbsElmPos(document.getElementById("statButton"));
	var ww=pos.x;
	var wh=pos.y-statList.offsetHeight;
	statList.style.left=""+ww+"px";
	statList.style.top =""+wh+"px";   
	if(statList.style.visibility=="visible") statList.style.visibility="hidden";
	else statList.style.visibility="visible";	
}
function hideStat(){
	var statList=document.getElementById("statist");
	statList.style.visibility="hidden";
}

function showParam(){
	var paramList=document.getElementById("params");
	var pos=getAbsElmPos(document.getElementById("paramButton"));
	var ww=pos.x;
	var wh=pos.y-paramList.offsetHeight;
	paramList.style.left=""+ww+"px";
	paramList.style.top =""+wh+"px";   
	if(paramList.style.visibility=="visible") paramList.style.visibility="hidden";
	else paramList.style.visibility="visible";	
}
function hideParam(){
	var paramList=document.getElementById("params");
	paramList.style.visibility="hidden";
}


function showChrom(){
	
	var chromList=document.getElementById("chromList");
	var cImage = document.getElementById("cImage");
	var chromLab = document.getElementById(id="chromButLab")
	var pos=getAbsElmPos(document.getElementById("chrom"));
	chromList.style.left=""+(pos.x-200)+"px";
	chromList.style.top =""+(pos.y+30)+"px";
	if(chromList.style.visibility=="visible") {
		chromList.style.visibility="hidden"; 	
		cImage.style.visibility="hidden";
		chromLab.innerHTML="show chrom";
	}
	else {
		chromList.style.visibility="visible";
		cImage.style.visibility="visible";
		chromLab.innerHTML="hide chrom";
	}
}
function hideChrom(){
	var chromList=document.getElementById("chromList");
	chromList.style.visibility="hidden";
}
function setChrom(chr){	
	image=document.getElementById("tImage");
	image.src=imageFile(curImage,chr);
	

	var curChrom=document.getElementById("curChrom");
	curChrom.innerHTML="<font color='green' style='font-weight:700; font-size:90%;'>"+chr+"</font>";

	var corr=document.getElementById("cc_" + chr)
	var chrCorr=document.getElementById("chrCorr")
	chrCorr.innerHTML = corr.innerHTML

	var obs=document.getElementById("obs_" + chr)
	var chrObserv=document.getElementById("chrObserv")
	chrObserv.innerHTML = obs.innerHTML
}

function getPageScroll(){
	if(window.pageXOffset != undefined)
		return {left: pageXOffset, top: pageYOffset};
    var html = document.documentElement;
    var body = document.body;
    var top = html.scrollTop || body && body.scrollTop || 0;
    top -= html.clientTop;
    var left = html.scrollLeft || body && body.scrollLeft || 0;
    left -= html.clientLeft;
	if(top  < 0) top =0;
	if(left < 0) left=0;
    return {top: top, left: left};
  }


function getAbsElmPos(obj){
	var x=0, y=0;
    while(obj) 
		{
		y = y + parseInt(obj.offsetTop);
		x = x + parseInt(obj.offsetLeft);
		obj = obj.offsetParent;
		}
	return {x:x, y:y};
	}
	
//===============================================
function getScroll(content){
  var body=document.getElementById(content);
  if(body==null) alert("null "+content);
  return {vScrollPos:body.scrollTop, hScrollPos:body.scrollLeft};
}

function scrollTable(content,col,row){

	var scrollPos=getScroll(content);

	var colHeader=document.getElementById(col);  
	var rowHeader=document.getElementById(row);  

	colHeader.scrollLeft=scrollPos.hScrollPos;
	rowHeader.scrollTop=scrollPos.vScrollPos;
}


//===============================================
function winWidth(){
	if (window.innerWidth) return window.innerWidth;  
	else if (document.documentElement && document.documentElement.clientWidth)  
		return document.documentElement.clientWidth;  
	else if (document.body)  
		return document.body.clientWidth; 
	return 500;
}
function winHeight(){
	if (window.innerHeight)  return window.innerHeight;
	else if (document.documentElement && document.documentElement.clientHeight)  
		return document.documentElement.clientHeight;  
	else if (document.body)  
		return document.body.clientHeight;  
	return 400;
}

function setSize(){
  var tblScroll=document.getElementById("tblScroll");
  var colScroll=document.getElementById("colScroll");  
  var rowScroll=document.getElementById("rowScroll");  
  var bodyTable=document.getElementById("bodyTable");  
  var colHTable=document.getElementById("colHTable");  
  var rowHTable=document.getElementById("rowHTable");  
  var imgTable =document.getElementById("imgTable");

  //=================== set table size
  var ww=winWidth ();  //window width / height
  var wh=winHeight()-tableHeightExt;
  if(imgTable.style.visibility=="visible")  ww-=pictCellWidth;
  
  var totalWidth  = bodyTable.offsetWidth +rowHTable.offsetWidth+16; // Table with/height
  var totalHeight = bodyTable.offsetHeight+colHTable.offsetHeight+16;
  if(ww > totalWidth)  ww= totalWidth;         // new Table with/height
  if(wh > totalHeight) wh= totalHeight;

  //=================== set width for the table
  colHTable.style.width = bodyTable.style.width;
  rowHTable.style.height= bodyTable.style.height;


  var q=ww-rowHTable.offsetWidth;

  if(q>0)  tblScroll.style.width=""+q+"px";

  q=wh-colHTable.offsetHeight;

  if(q>0)  {tblScroll.style.height=""+q+"px";}

//  alert(""+rowScroll.style.height+"  Elm.client="+rowScroll.clientHeight);
  //=================== set width & height for headers  
  var dx=tblScroll.offsetWidth -tblScroll.clientWidth;
  var dy=tblScroll.offsetHeight-tblScroll.clientHeight;

  rowScroll.style.height=""+(tblScroll.offsetHeight-dy)+"px"; //rowHeader.style.height=""+body.clientHeight+"px";
  colScroll.style.width =""+(tblScroll.offsetWidth -dx)+"px";
}


//===============================================
function getTextSize(txt){
  var pa=document.body;
  var who= document.createElement('div');
  var atts= {fontSize:'1em',padding:'0',position:'absolute',lineHeight:'1',visibility:'hidden'};
  for(var p in atts){who.style[p]= atts[p];}
  who.appendChild(document.createTextNode(txt));
  pa.appendChild(who);
  var fs= [who.offsetWidth,who.offsetHeight];
  var width=who.offsetWidth;
  pa.removeChild(who);
  return fs;
}
