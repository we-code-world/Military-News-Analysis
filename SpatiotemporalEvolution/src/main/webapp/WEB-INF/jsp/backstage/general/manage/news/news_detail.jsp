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
</div>
<div class="contain-boder">
    <div id="cnblogs_post_body" class="cnblogs-markdown">
        <h2>${requestScope.get('news').newsTittle}</h2>
        <p>新闻地址<code><a href="${requestScope.get('news').url}">${requestScope.get('news').url}</a></code>来源<code>@${requestScope.get('news').newsSource}</code>时间<code>${requestScope.get('news').showDate()}</code></p>
        <pre><code class="language-java">
<c:forEach  var="line" items="${requestScope.get('article_lines')}"><p>${line}</p></c:forEach>
</code></pre>
    </div>
</div>

<!-- jQuery -->
<script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
<script src="${pageContext.request.contextPath}/js/alert/sweetalert.min.js"></script>
<script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
<script>
    var event_sign = 1;
    $('a.btn').click(function() {
        var myvalue = parseInt($(this).attr("value"));
        var styles = ["btn-success","btn-primary","btn-danger","btn-info"];
        for (var i = 0; i < 4; i++) {
            $('a.btn').removeClass(styles[i]);
        }
        //$('a.btn').addClass("btn-default");
        if ($(this).attr("class").indexOf("btn-default")>0){
            event_sign = 1;
            $('a.btn').addClass("btn-default");
            $(this).removeClass("btn-default");
            $(this).toggleClass(styles[myvalue-1]);
            $('pre').mouseup(function(e){
                var push_tag = window.getSelection().toString();
                if (1 == e.which && push_tag!="" &&event_sign) {
                    swal({
                        title:"是否要添加“"+push_tag+"”",
                        text:"",
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
                                url: "${pageContext.request.contextPath}/Admin/general/news/Detail/submit",
                                type: 'POST',
                                dataType: 'JSON',
                                data: {
                                    "catelogid": myvalue,
                                    "tag": push_tag
                                },
                                success: function (data) {
                                    if (data.result === "ok") {
                                        $('.input-icon-tag-contain-'+myvalue).before("<span class=\"label label-info label-icon-tag\">" + push_tag + "</span>&nbsp;  ");
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
            });
        }else{
            $('a.btn').addClass("btn-default");
            event_sign=0;
        }

    });
    $('.input-icon-tag-add-1').click(function () {
        $('.input-icon-tag-contain-1').show();
        $(this).hide();
    });

    //$('.input-icon-tag-1').on("keydown", function (e) {
    // var $this = $(this);
    // var value = $this.val().trim();
    // if (e.keyCode == 13 && value != "") {
    //     $this.val("");
    //     $.ajax({
    //         url: "/font/icons/addtagpost.html",
    //         type: 'POST',
    //         dataType: 'JSON',
    //         data: {
    //             icon_id: '224',
    //             font_id: '1',
    //             tag: value
    //         },
    //         success: function (data) {
    //             if(data.code){
    //                 $this.before("<span class=\"label label-info label-icon-tag\">" + value + "</span>&nbsp;  ");
    //             }
    //
    //         },
    //         error:function () {
    //
    //         }
    //     })
    // }
    //});

    $('.input-icon-tag-1').on("change", function (e) {
        var $this = $(this);
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/news/Detail/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogid": "1",
                "tag": value
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
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/news/Detail/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogid": "2",
                "tag": value
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
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/news/Detail/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogid": "3",
                "tag": value
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
        var value = $this.val().trim();
        $this.val("");
        $.ajax({
            url: "${pageContext.request.contextPath}/Admin/general/news/Detail/submit",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogid": "4",
                "tag": value
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
    $('.input-icon-tag-close-4').click(function () {
        $('.input-icon-tag-contain-4').hide();
        $('.input-icon-tag-add-4').show();
    });
</script>
</body>
</html>

