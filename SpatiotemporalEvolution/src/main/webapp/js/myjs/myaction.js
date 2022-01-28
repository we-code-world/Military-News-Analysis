function setCookie(cname,cvalue,exhours){
    var d = new Date();
    d.setTime(d.getTime()+(exhours*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires;
}
function updateCookie(cname,cvalue,exhours){
    setCookie(cname,cvalue,exhours);
}
function increaseCookie(cname){
    var value = getCookie(cname);
    if (value === "")value = "1";
    //console.log(value);
    var num = parseInt(value);
    num = num + 1;
    setCookie(cname,""+num,1);
}
function decreaseCookie(cname){
    var value = getCookie(cname);
    if (value === "")value = "1";
    //console.log(value);
    var num = parseInt(value);
    if(num>1)num = num - 1;
    setCookie(cname,""+num,1);
}
function getCookie(cname)
{
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++)
    {
        var c = ca[i].trim();
        if (c.indexOf(name)===0) return c.substring(name.length,c.length);
    }
    return "";
}
function checkCookie(cname)
{
    var cookie=getCookie(cname);
    if (cookie!="")
    {
        return true;
    }
    else return false;
}
function delCookie(cname){
    setCookie(name, "", -1);
}
function setIframeSizeCookie1(iframeID){
    var wid = document.getElementById(iframeID).style.width;
    var high = document.getElementById(iframeID).style.height;
    setCookie("Iframe-width",wid,10);
    setCookie("Iframe-height",high,10);
}
function setIframeSizeCookie2(iframewid,iframehigh){
    setCookie("Iframe-width",iframewid,10);
    setCookie("Iframe-height",iframehigh,10);
}
function setStyleByIframeSizeCookie(bodyID){
    document.getElementById(bodyID).style.width = parseInt(getCookie("Iframe-width"));
    document.getElementById(bodyID).style.height = parseInt(getCookie("Iframe-heght"));
}

//方法一： window.open()
function download(urls){
    window.open(urls);
}

var NEXT_PAGE = $('.next-page');
var PAGE_NUM = $('.page-num').attr('value');
var LAST_PAGE = $('.last-page');
LAST_PAGE.click(function () {
    updateCookie("pageNum",parseInt(PAGE_NUM) - 1,0.002);
});
NEXT_PAGE.click(function () {
    updateCookie("pageNum",parseInt(PAGE_NUM) + 1,0.002);
});
