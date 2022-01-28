<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="${pageContext.request.contextPath}/icons/favicon.ico" type="image/ico" />
    <title>新闻分析</title>
    <link href="${pageContext.request.contextPath}/css/news/myblog.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/news/bundle-codinglife.min.css" rel="stylesheet">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap/bootstrap.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/backstage/font-awesome.min.css">
    <link href="${pageContext.request.contextPath}/css/alert/sweetalert.min.css" rel="stylesheet">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/toastr.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
</head>

<body>
<div class="back-to-top no-fix">
    <a id="select-btn-1" class="btn btn-default" value="1">时间</a>
    <a id="select-btn-2" class="btn btn-default" value="2">地点</a>
    <a id="select-btn-3" class="btn btn-default" value="3">国家</a>
    <a id="select-btn-4" class="btn btn-default" value="4">武器</a>
    <a id="select-btn-5-1" class="btn btn-default" value="5-1">触发词</a>
    <a id="select-btn-5-2" class="btn btn-default" value="5-2">主体</a>
    <a id="select-btn-5-3" class="btn btn-default" value="5-3">客体</a>
</div>
<div class="contain-boder">
    <div id="cnblogs_post_body" class="cnblogs-markdown">
        <h2><c:forEach var="line" items="${requestScope.get('newsTittle')}"><span class="tittle" id="line${line.get('lineID')}" value="${line.get('lineID')}">${line.get('seq')}</span></c:forEach></h2>
        <p>新闻地址<code><a href="${requestScope.get('url')}">${requestScope.get('url')}</a></code>来源<code>@${requestScope.get('newsSource')}</code>时间<code>${requestScope.get('Date')}</code></p>
        <pre><code class="language-java">
            <c:forEach  var="line" items="${requestScope.get('article_lines')}"><p><c:forEach var="seq" items="${line.get('seqs')}"><span class="seqs" id="line${seq.get('lineID')}" value="${seq.get('lineID')}" >${seq.get('seq')}</span></c:forEach></p></c:forEach>
</code></pre>
        <p>已标注事件元素：</p>
        <ul>
            <li style="font-size: 14px;">
                <small>时间：
                    <c:forEach  var="item" items="${requestScope.get('timeList')}">
                        <span class="label label-info">${item}</span> &nbsp;
                    </c:forEach>
                    <span class="input-icon-tag-contain-1" style="display: none;">
                        <label>
                            <input class="form-control input-sm input-icon-tag-1">
                        </label>
                        <i class="fa fa-times-circle input-icon-tag-close-1" aria-hidden="true" style="text-shadow: none;cursor: pointer;"></i>
                    </span>
                    <span class="label label-danger input-icon-tag-add-1" style="text-shadow: none;cursor: pointer;"><i class="fa fa-plus"></i></span>
                    &nbsp;
                </small>
            </li>
            <li style="font-size: 14px;">
                <small>地点：
                    <c:forEach  var="item" items="${requestScope.get('locList')}">
                        <span class="label label-info">${item}</span> &nbsp;
                    </c:forEach>
                    <span class="input-icon-tag-contain-2" style="display: none;">
                        <label>
                            <input class="form-control input-sm input-icon-tag-2">
                        </label>
                        <i class="fa fa-times-circle input-icon-tag-close-2" aria-hidden="true" style="text-shadow: none;cursor: pointer;"></i>
                    </span>
                    <span class="label label-danger input-icon-tag-add-2" style="text-shadow: none;cursor: pointer;"><i class="fa fa-plus"></i></span>
                    &nbsp;
                </small>
            </li>
            <li style="font-size: 14px;">
                <small>国家：
                    <c:forEach  var="item" items="${requestScope.get('countryList')}">
                        <span class="label label-info">${item}</span> &nbsp;
                    </c:forEach>
                    <span class="input-icon-tag-contain-3" style="display: none;">
                        <label>
                            <input class="form-control input-sm input-icon-tag-3">
                        </label>
                        <i class="fa fa-times-circle input-icon-tag-close-3" aria-hidden="true" style="text-shadow: none;cursor: pointer;"></i>
                    </span>
                    <span class="label label-danger input-icon-tag-add-3" style="text-shadow: none;cursor: pointer;"><i class="fa fa-plus"></i></span>
                    &nbsp;
                </small>
            </li>
            <li style="font-size: 14px;">
                <small>武器：
                    <c:forEach  var="item" items="${requestScope.get('weaponList')}">
                        <span class="label label-info">${item}</span> &nbsp;
                    </c:forEach>
                    <span class="input-icon-tag-contain-4" style="display: none;">
                        <label>
                            <input class="form-control input-sm input-icon-tag-4">
                        </label>
                        <i class="fa fa-times-circle input-icon-tag-close-4" aria-hidden="true" style="text-shadow: none;cursor: pointer;"></i>
                    </span>
                    <span class="label label-danger input-icon-tag-add-4" style="text-shadow: none;cursor: pointer;"><i class="fa fa-plus"></i></span>
                    &nbsp;
                </small>
            </li>
            <li style="font-size: 14px;">
                <small>【主体】触发词【客体】：
                    <c:forEach  var="item" items="${requestScope.get('triggerList')}">
                        <span class="label label-info">${item}</span>
                    </c:forEach>
                    <span class="input-icon-tag-contain-5" style="display: none;">
                        <label>
                            <input class="form-control input-sm input-icon-tag-5">
                        </label>
                        <i class="fa fa-times-circle input-icon-tag-close-5" aria-hidden="true" style="text-shadow: none;cursor: pointer;"></i>
                    </span>
                    <span class="label label-danger input-icon-tag-add-5" style="text-shadow: none;cursor: pointer;"><i class="fa fa-plus"></i></span>
                    &nbsp;
                </small>
            </li>
        </ul>
    </div>
</div>
<div style="position: fixed;width: 100px;right: 50px;bottom: 150px;border: 1px #1d2124;">
    第<input id="goto" type="text" style="width: 30px" value="${requestScope.get("NewsID")}">篇<input type="button" onclick="gotoNews()" value="转到">
</div>
<a value="0" onclick="deletetext()" class="btn btn-default right-top-left" role="button">
    <i class="fa fa-trash-o" aria-hidden="true"></i>
</a>
<a value="0" onclick="deleteAll()" class="btn btn-default right-top-middim" role="button">
    <i class="fa fa-refresh" aria-hidden="true"></i>
</a>
<a value="0" href="${pageContext.request.contextPath}/Admin/general/human/download" class="btn btn-default right-top" role="button">
    <i class="fa fa-download" aria-hidden="true"></i>
</a>
<a id="back-to-top" value="0" href="#" class="btn btn-default back-to-top" role="button" aria-label="Scroll to top">
    <i class="fa fa-angle-up" aria-hidden="true"></i>
</a>
<a href="${pageContext.request.contextPath}/Admin/general/human" onclick="lastNews()" value="0" style="position: fixed;width: 100px;right: 50px;bottom: 100px;" class="btn btn-default" role="button">上一篇</a>
<a href="${pageContext.request.contextPath}/Admin/general/human" onclick="nextNews()" value="0" style="position: fixed;width: 100px;right: 50px;bottom: 50px" class="btn btn-default" role="button">下一篇</a>

<!-- jQuery -->
<script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
<script src="${pageContext.request.contextPath}/js/alert/sweetalert.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
<script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
<script>
    var event_sign = 1;
    $('a.btn').click(function() {
        if ($(this).attr("value")==="0"){
            return;
        }
        var myvalue = $(this).attr("value");
        setCookie("select_btn",$(this).attr("id"),1);
        var myText = $(this).text();
        var styles = {"时间":"btn-success","地点":"btn-success","国家":"btn-primary","武器":"btn-info","触发词":"btn-danger","主体":"btn-primary","客体":"btn-info"};
        for (var key in styles) {
            $('a.btn').removeClass(styles[key]);
        }
        //$('a.btn').addClass("btn-default");
        if ($(this).attr("class").indexOf("btn-default")>0){
            event_sign = 1;
            $('a.btn').addClass("btn-default");
            $(this).removeClass("btn-default");
            $(this).toggleClass(styles[myText]);
            function selectSubmit(e,lineID,offset,text){
                if (1 == e.which && text!="" &&event_sign) {
                    swal({
                        title:"选中",
                        text:"是否要添加“"+text+"”",
                        type:"info",
                        customClass: "sweetAlert",
                        showCancelButton:true,//是否显示取消按钮
                        cancelButtonText:'取 消',//按钮内容
                        cancelButtonColor:'#b9b9b9',

                        showConfirmButton:true,
                        confirmButtonText:'确 认',
                        confirmButtonColor:"#dd6b55",

                        closeOnConfirm:true,//点击返回上一步操作
                        closeOnCancel:true
                    },function(isConfirm){
                        if (isConfirm) {

                            $.ajax({
                                url: "${pageContext.request.contextPath}/Admin/general/human/submit",
                                type: 'POST',
                                dataType: 'JSON',
                                data: {
                                    "catelogId": myvalue,
                                    "tag": text,
                                    "lineID":lineID,
                                    "textOffset":offset
                                },
                                success: function (data) {
                                    if (data.result === "ok") {
                                        window.location.reload();
                                    } else {
                                        toastr.error("数据提交失败！");
                                    }
                                },
                                error: function () {
                                    toastr.error("系统或服务器出错！");
                                }
                            })
                        }
                    });
                }
            }
            $('span.seqs').mouseup(function(e){
                var value = $(this).attr("value");
                var lineID = parseInt(value);
                var selection = window.getSelection();
                var push_tag = selection.toString();
                var focusNode = selection.focusNode;
                var focusOffset = selection.focusOffset;
                var anchorNode = selection.anchorNode;
                var anchorOffset = selection.anchorOffset;
                //var startRangeOffset = selection.getRangeAt(0).startOffset;
                window.getSelection().setBaseAndExtent(document.getElementById($(this).attr("id")),0,anchorNode,anchorOffset);
                var otherRangeOffset = selection.toString().length;
                //console.log(otherRangeOffset+"+"+startRangeOffset);
                selection.setBaseAndExtent(anchorNode,anchorOffset,focusNode,focusOffset);
                selectSubmit(e,lineID,otherRangeOffset,push_tag);
            });
            $('span.tittle').mouseup(function(e){
                var value = $(this).attr("value");
                var lineID = parseInt(value);
                var selection = window.getSelection();
                var push_tag = selection.toString();
                var focusNode = selection.focusNode;
                var focusOffset = selection.focusOffset;
                var anchorNode = selection.anchorNode;
                var anchorOffset = selection.anchorOffset;
                //var startRangeOffset = selection.getRangeAt(0).startOffset;
                window.getSelection().setBaseAndExtent(document.getElementById($(this).attr("id")),0,anchorNode,anchorOffset);
                var otherRangeOffset = selection.toString().length;
                //console.log(otherRangeOffset+"+"+startRangeOffset);
                selection.setBaseAndExtent(anchorNode,anchorOffset,focusNode,focusOffset);
                selectSubmit(e,lineID,otherRangeOffset,push_tag);
            });
        }else{
            $('a.btn').addClass("btn-default");
            event_sign=0;
        }

    });
    $(document).ready(function () {
        $(this).keydown(function(event){
            if (event.ctrlKey){
                function clickDelete(e,lineID,offset,text){
                    if (offset!=null&& text != "") {
                        swal({
                            title:"选中",
                            text:"是否要删除“"+text+"”所在标签？",
                            type:"info",
                            customClass: "sweetAlert",
                            showCancelButton:true,//是否显示取消按钮
                            cancelButtonText:'取 消',//按钮内容
                            cancelButtonColor:'#b9b9b9',

                            showConfirmButton:true,
                            confirmButtonText:'确 认',
                            confirmButtonColor:"#dd6b55",

                            closeOnConfirm:true,//点击返回上一步操作
                            closeOnCancel:true
                        },function(isConfirm){
                            if (isConfirm) {
                                $.ajax({
                                    url: "${pageContext.request.contextPath}/Admin/general/human/mark/delete",
                                    type: 'POST',
                                    dataType: 'JSON',
                                    data: {
                                        "tag": text,
                                        "lineID":lineID,
                                        "textOffset":offset
                                    },
                                    success: function (data) {
                                        if (data.result === "ok") {
                                            window.location.reload();
                                        } else {
                                            toastr.error("数据提交失败！");
                                        }
                                    },
                                    error: function () {
                                        toastr.error("系统或服务器出错！");
                                    }
                                })
                            }
                        });
                    }
                }
                $('span.seqs').click(function(e){
                    var value = $(this).attr("value");
                    var lineID = parseInt(value);
                    var selection = window.getSelection();
                    var focusNode = selection.focusNode;
                    var focusOffset = selection.focusOffset;
                    var anchorNode = selection.anchorNode;
                    var anchorOffset = selection.anchorOffset;
                    //var startRangeOffset = selection.getRangeAt(0).startOffset;
                    window.getSelection().setBaseAndExtent(focusNode,0,focusNode,1);
                    var text = selection.toString();
                    console.log(text);
                    window.getSelection().setBaseAndExtent(document.getElementById($(this).attr("id")),0,anchorNode,anchorOffset);
                    var otherRangeOffset = selection.toString().length;
                    //console.log(otherRangeOffset+"+"+startRangeOffset);
                    selection.setBaseAndExtent(anchorNode,anchorOffset,focusNode,focusOffset);
                    clickDelete(e,lineID,otherRangeOffset,text);
                });
                $('span.tittle').click(function(e){
                    var value = $(this).attr("value");
                    var lineID = parseInt(value);
                    var selection = window.getSelection();
                    var focusNode = selection.focusNode;
                    var focusOffset = selection.focusOffset;
                    var anchorNode = selection.anchorNode;
                    var anchorOffset = selection.anchorOffset;
                    window.getSelection().setBaseAndExtent(focusNode,0,focusNode,1);
                    var text = selection.toString();
                    //var startRangeOffset = selection.getRangeAt(0).startOffset;
                    window.getSelection().setBaseAndExtent(document.getElementById($(this).attr("id")),0,anchorNode,anchorOffset);
                    var otherRangeOffset = selection.toString().length;
                    //console.log(otherRangeOffset+"+"+startRangeOffset);
                    selection.setBaseAndExtent(anchorNode,anchorOffset,focusNode,focusOffset);
                    clickDelete(e,lineID,otherRangeOffset,text);
                });
            }
        })
    });
    $('.input-icon-tag-add-1').click(function () {
        $('.input-icon-tag-contain-1').show();
        $(this).hide();
    });

    $('.input-icon-tag-1').on("change", function (e) {
        var $this = $(this);
        var lineID = 1;
        var offset = 1;
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/human/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogId": "1",
                "tag": value,
                "lineID":lineID,
                "textOffset":offset
            },
            success: function (data) {
                if (data.result === "ok") {
                    $('.input-icon-tag-contain-1').before("<span class=\"label label-info label-icon-tag\">" + value + "</span>&nbsp;  ");
                } else {
                    toastr.error("数据提交失败！");
                }
            },
            error: function () {
                toastr.error("系统或服务器出错！");
            }
        })
    });
    $('.input-icon-tag-close-1').click(function () {
        $('.input-icon-tag-contain-1').hide();
        $('.input-icon-tag-add-1').show();
    });

    $('.input-icon-tag-add-2').click(function () {
        $('.input-icon-tag-contain-2').show();
        $(this).hide();
    });
    $('.input-icon-tag-2').on("change", function (e) {
        var $this = $(this);
        var lineID = 1;
        var offset = 1;
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/human/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogId": "2",
                "tag": value,
                "lineID":lineID,
                "textOffset":offset
            },
            success: function (data) {
                if (data.result === "ok") {
                    $('.input-icon-tag-contain-2').before("<span class=\"label label-info label-icon-tag\">" + value + "</span>&nbsp;  ");
                } else {
                    toastr.error("数据提交失败！");
                }
            },
            error: function () {
                toastr.error("系统或服务器出错！");
            }
        })
    });
    $('.input-icon-tag-close-2').click(function () {
        $('.input-icon-tag-contain-2').hide();
        $('.input-icon-tag-add-2').show();
    });

    $('.input-icon-tag-add-3').click(function () {
        $('.input-icon-tag-contain-3').show();
        $(this).hide();
    });
    $('.input-icon-tag-3').on("change", function (e) {
        var $this = $(this);
        var lineID = 0;
        var offset = 0;
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/human/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogId": "3",
                "tag": value,
                "lineID":lineID,
                "textOffset":offset
            },
            success: function (data) {
                if (data.result === "ok") {
                    $('.input-icon-tag-contain-3').before("<span class=\"label label-info label-icon-tag\">" + value + "</span>&nbsp;  ");
                } else {
                    toastr.error("数据提交失败！");
                }
            },
            error: function () {
                toastr.error("系统或服务器出错！");
            }
        })
    });
    $('.input-icon-tag-close-3').click(function () {
        $('.input-icon-tag-contain-3').hide();
        $('.input-icon-tag-add-3').show();
    });

    $('.input-icon-tag-add-4').click(function () {
        $('.input-icon-tag-contain-4').show();
        $(this).hide();
    });
    $('.input-icon-tag-4').on("change", function (e) {
        var $this = $(this);
        var lineID = 0;
        var offset = 0;
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/human/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogId": "4",
                "tag": value,
                "lineID":lineID,
                "textOffset":offset
            },
            success: function (data) {
                if (data.result === "ok") {
                    $('.input-icon-tag-contain-4').before("<span class=\"label label-info label-icon-tag\">" + value + "</span>&nbsp;  ");
                } else {
                    toastr.error("数据提交失败！");
                }
            },
            error: function () {
                toastr.error("系统或服务器出错！");
            }
        })
    });
    $('.input-icon-tag-close-5').click(function () {
        $('.input-icon-tag-contain-4').hide();
        $('.input-icon-tag-add-4').show();
    });
    $('.input-icon-tag-add-5').click(function () {
        $('.input-icon-tag-contain-4').show();
        $(this).hide();
    });
    $('.input-icon-tag-5').on("change", function (e) {
        var $this = $(this);
        var lineID = 1;
        var offset = 1;
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/human/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogId": "5",
                "tag": value,
                "lineID":lineID,
                "textOffset":offset
            },
            success: function (data) {
                if (data.result === "ok") {
                    $('.input-icon-tag-contain-5').before("<span class=\"label label-info label-icon-tag\">" + value + "</span>&nbsp;  ");
                } else {
                    toastr.error("数据提交失败！");
                }
            },
            error: function () {
                toastr.error("系统或服务器出错！");
            }
        })
    });
    $('.input-icon-tag-close-5').click(function () {
        $('.input-icon-tag-contain-5').hide();
        $('.input-icon-tag-add-5').show();
    });
    function lastNews() {
        decreaseCookie("markID");
    }
    function nextNews() {
        increaseCookie("markID");
    }
    function gotoNews() {
        var num = document.getElementById("goto").value;//$('#goto').attr("value");
        //console.log(num);
        setCookie("markID",num,1);
        window.location.reload();
    }
    function deletetext() {
        swal({
            title:"删除",
            text:"是否要删除当前文章？",
            type:"info",
            customClass: "sweetAlert",
            showCancelButton:true,//是否显示取消按钮
            cancelButtonText:'取 消',//按钮内容
            cancelButtonColor:'#b9b9b9',

            showConfirmButton:true,
            confirmButtonText:'确 认',
            confirmButtonColor:"#dd6b55",

            closeOnConfirm:true,//点击返回上一步操作
            closeOnCancel:true
        },function(isConfirm){
            if (isConfirm) {
                $.ajax({
                    url: "${pageContext.request.contextPath}/Admin/general/human/delete",
                    type: 'POST',
                    success: function () {
                        window.location.reload();
                    },
                    error: function () {
                        toastr.error("系统或服务器出错！");
                    }
                })
            }
        });

    }
    function deleteAll() {
        swal({
            title:"刷新",
            text:"是否要重新标注当前页面？",
            type:"info",
            customClass: "sweetAlert",
            showCancelButton:true,//是否显示取消按钮
            cancelButtonText:'取 消',//按钮内容
            cancelButtonColor:'#b9b9b9',

            showConfirmButton:true,
            confirmButtonText:'确 认',
            confirmButtonColor:"#dd6b55",

            closeOnConfirm:true,//点击返回上一步操作
            closeOnCancel:true
        },function(isConfirm){
            if (isConfirm) {
                $.ajax({
                    url: "${pageContext.request.contextPath}/Admin/general/human/refresh",
                    type: 'POST',
                    success: function () {
                        window.location.reload();
                    },
                    error: function () {
                        toastr.error("系统或服务器出错！");
                    }
                })
            }
        });

    }
    $(document).ready(function () {
        check_mode = getCookie("select_btn");
        document.getElementById(check_mode).click();
    });
</script>
</body>
</html>

