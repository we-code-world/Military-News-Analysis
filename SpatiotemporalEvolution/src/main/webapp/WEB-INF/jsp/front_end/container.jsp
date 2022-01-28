<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html style="height: 642px;">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>首页</title>
    <link rel="icon" href="${pageContext.request.contextPath}/icons/favicon.ico">
    <link href="https://cdn.bootcss.com/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css" rel="stylesheet">

    <!-- Google Font: Source Sans Pro -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/container/all.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/container/adminlte.min.css">
    <!-- overlayScrollbars -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/container/OverlayScrollbars.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/backstage/font-awesome.min.css">

    <style>
        #aTop{
            color: #6c757d;
        }
        #aTop:hover{
            color: #007bff;
        }
        #aName{
            color: #6c757d;
        }
        #aName:hover{
            color: #007bff;
        }
        li {
            display: list-item;
            text-align: -webkit-match-parent;
        }
    </style>
</head>
<body class="hold-transition sidebar-mini layout-fixed scroller scroller-1" data-panel-auto-height-mode="height">
<div class="wrapper">

    <!-- Navbar -->
    <nav id="nav_style" class="main-header navbar navbar-expand navbar-white navbar-light">
        <!-- Left navbar links -->
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" data-widget="pushmenu" href="" role="button"><i class="fas fa-bars"></i></a>
            </li>
            <li class="nav-item d-none d-sm-inline-block">
                <a href="${pageContext.request.contextPath}/Show/index" class="nav-link">首页</a>
            </li>
            <li class="nav-item d-none d-sm-inline-block">
                <a href="${pageContext.request.contextPath}/Show/Map2d" class="nav-link">分析展示</a>
            </li>
            <li class="nav-item d-none d-sm-inline-block dropdown">
                <a href="" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">常用链接<span class="caret"></span></a>
                <ul id="dropdown-menu-ul1" class="dropdown-menu nav-item">
                    <li><a class="nav-link" href="javascript:void(0);" onclick="goto_link('http://www.81.cn/')">中国军网</a></li>
                    <li><a class="nav-link" href="javascript:void(0);" onclick="goto_link('http://mil.huanqiu.com/')">环球军事</a></li>
                    <li><a class="nav-link" href="javascript:void(0);" onclick="goto_link('http://www.xilu.com/')">西陆网</a></li>
                    <li><a class="nav-link" href="javascript:void(0);" onclick="goto_link('http://www.justoper.com/')">军事武器</a></li>
                    <li><a class="nav-link" href="javascript:void(0);" onclick="goto_link('http://www.wuqibaike.com/')">武器百科</a></li>
                </ul>
            </li>
        </ul>
        <ul id="TimeZone" class="navbar-nav" style="" onclick="time_setting()">
            <div class="pc-search-filter" data-spm="filter">
                <div class="bar-group" style="padding-left:20px;">时间区间</div>
                <div class="bar-group price-bar">
                  <span>
                    <input id="time_start" value="" class="txt" placeholder="2020-01-01">
                    <span style="margin: 0 2px;">——</span>
                    <input id="time_end" value="" class="txt" placeholder="2020-12-31">
                  </span>
                </div>
            </div>
        </ul>

        <!-- Right navbar links -->
        <ul class="navbar-nav ml-auto">

            <!-- Messages Dropdown Menu -->
            <li class="nav-item dropdown" hidden>
                <a class="nav-link" data-toggle="dropdown" href="#">
                    <i class="far fa-comments"></i>
                    <span class="badge badge-danger navbar-badge">3</span>
                </a>
                <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
                    <a href="#" class="dropdown-item">
                        <!-- Message Start -->
                        <div class="media">
                            <img src="${pageContext.request.contextPath}/face/user-black.png" alt="User Avatar" class="img-size-50 mr-3 img-circle">
                            <div class="media-body">
                                <h3 class="dropdown-item-title">
                                    梨花带鱼
                                    <span class="float-right text-sm text-danger"><i class="fas fa-star"></i></span>
                                </h3>
                                <p class="text-sm">跟我联系</p>
                                <p class="text-sm text-muted"><i class="far fa-clock mr-1"></i> 4 Hours Ago</p>
                            </div>
                        </div>
                        <!-- Message End -->
                    </a>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item">
                        <!-- Message Start -->
                        <div class="media">
                            <img src="${pageContext.request.contextPath}/face/user-black.png" alt="User Avatar" class="img-size-50 img-circle mr-3">
                            <div class="media-body">
                                <h3 class="dropdown-item-title">
                                    球球
                                    <span class="float-right text-sm text-muted"><i class="fas fa-star"></i></span>
                                </h3>
                                <p class="text-sm">你好啊！</p>
                                <p class="text-sm text-muted"><i class="far fa-clock mr-1"></i> 4 Hours Ago</p>
                            </div>
                        </div>
                        <!-- Message End -->
                    </a>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item">
                        <!-- Message Start -->
                        <div class="media">
                            <img src="${pageContext.request.contextPath}/face/user-black.png" alt="User Avatar" class="img-size-50 img-circle mr-3">
                            <div class="media-body">
                                <h3 class="dropdown-item-title">
                                   莫明奇妙
                                    <span class="float-right text-sm text-warning"><i class="fas fa-star"></i></span>
                                </h3>
                                <p class="text-sm">我来了！</p>
                                <p class="text-sm text-muted"><i class="far fa-clock mr-1"></i> 4 Hours Ago</p>
                            </div>
                        </div>
                        <!-- Message End -->
                    </a>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item dropdown-footer">查看详情</a>
                </div>
            </li>
            <!-- Notifications Dropdown Menu -->
            <li class="nav-item dropdown" hidden>
                <a class="nav-link" data-toggle="dropdown" href="#">
                    <i class="far fa-bell"></i>
                    <span class="badge badge-warning navbar-badge">15</span>
                </a>
                <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
                    <span class="dropdown-item dropdown-header">15 Notifications</span>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item">
                        <i class="fas fa-envelope mr-2"></i> 4条新消息
                        <span class="float-right text-muted text-sm">3 mins</span>
                    </a>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item">
                        <i class="fas fa-users mr-2"></i>8位好友申请
                        <span class="float-right text-muted text-sm">12 hours</span>
                    </a>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item">
                        <i class="fas fa-file mr-2"></i>&nbsp;&nbsp;3个新报告
                        <span class="float-right text-muted text-sm">2 days</span>
                    </a>
                    <div class="dropdown-divider"></div>
                    <a href="#" class="dropdown-item dropdown-footer">查看详情</a>
                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-widget="dropdown" href="${pageContext.request.contextPath}/Show/logout" role="button">
                    <i class="fa fa-sign-out" aria-hidden="true"></i>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-widget="fullscreen" href="" role="button">
                    <i class="fas fa-expand-arrows-alt"></i>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" hidden data-widget="control-sidebar" data-slide="true" href="" role="button">
                    <i class="fas fa-th-large"></i>
                </a>
            </li>
        </ul>
    </nav>
    <!-- /.navbar -->

    <!-- Main Sidebar Container -->
    <aside class="main-sidebar sidebar-white-primary elevation-4" style="background: #ffffff">
        <!-- Brand Logo -->
        <a href="${pageContext.request.contextPath}/Developer/project" id="aTop" class="brand-link">
            <img src="${pageContext.request.contextPath}/icons/logo.png" alt="Logo" class="brand-image img-circle elevation-3" style="opacity: .8">
            <span class="brand-text font-weight-light">军事分析系统</span>
        </a>

        <!-- Sidebar -->
        <div class="sidebar">
            <!-- Sidebar user panel (optional) -->
            <div class="user-panel mt-3 pb-3 mb-3 d-flex">
                <div class="image">
                    <img src="${pageContext.request.contextPath}/face/${requestScope.get('userFace')}" class="img-circle elevation-2" alt="User">
                </div>
                <div class="info">
                    <a id="aName" href="javascript:void(0)" onclick="logout()" class="d-block">${requestScope.get('username')}</a>
                </div>
            </div>

            <!-- SidebarSearch Form -->
            <div class="form-inline">
                <div class="input-group" data-widget="sidebar-search">
                    <input class="form-control form-control-sidebar" type="search" placeholder="Search" aria-label="Search">
                    <div class="input-group-append">
                        <button class="btn btn-sidebar">
                            <i class="fas fa-search fa-fw"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Sidebar Menu -->
            <nav class="mt-2">
                <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
                    <!-- Add icons to the links using the .nav-icon class
                         with font-awesome or any other icon font library -->
                    <li class="nav-item">
                        <a href="#" class="nav-link">
                            <i class="nav-icon fa fa-desktop"></i>
                            <p>
                                常用页面
                                <i class="right fas fa-angle-left"></i>
                            </p>
                        </a>
                        <ul class="nav nav-treeview">
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/index" class="nav-link">
                                    <i class="fa fa-home nav-icon"></i>
                                    <p>首页</p>
                                </a>
                            </li>
                        </ul>
                    </li>
                    <li class="nav-item" hidden>
                        <a href="" class="nav-link">
                            <i class="nav-icon fas fa-th"></i>
                            <p>
                                分析
                                <span class="right badge badge-danger">New</span>
                            </p>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link">
                            <i class="nav-icon fa fa-area-chart"></i>
                            <p>
                                事件分析
                                <i class="right fas fa-angle-left"></i>
                            </p>
                        </a>
                        <ul class="nav nav-treeview">
                            <li class="nav-item nav-margin-left">
                                <a id="start_page" href="${pageContext.request.contextPath}/Show/weapon_event" class="nav-link">
                                    <i class="fa fa-bar-chart nav-icon"></i>
                                    <p>事件-类别关联分析</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/event_weapon" class="nav-link">
                                    <i class="fa fa-line-chart nav-icon"></i>
                                    <p>事件-武器关联分析</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/Weapons" class="nav-link">
                                    <i class="fa fa-pie-chart nav-icon"></i>
                                    <p>武器参与事件统计</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/Location" class="nav-link">
                                    <i class="fa fa-pie-chart nav-icon"></i>
                                    <p>事件-地点发展分析</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left">
                                <a href="" class="nav-link">
                                    <i class="nav-icon fas fa-map-marker"></i>
                                    <p>
                                        事件空间分布分析
                                        <i class="fas fa-angle-left right"></i>
                                    </p>
                                </a>
                                <ul class="nav nav-treeview">
                                    <li class="nav-item inner-margin-left">
                                        <a href="${pageContext.request.contextPath}/Show/Map2d" onclick="setCookie('location_map','world',0.1)" class="nav-link">
                                            <i class="fa fa-map-o nav-icon"></i>
                                            <p>平面展示</p>
                                        </a>
                                    </li>
                                    <li class="nav-item inner-margin-left">
                                        <a href="${pageContext.request.contextPath}/Show/Map3d" class="nav-link">
                                            <i class="fa fa-globe nav-icon"></i>
                                            <p>三维展示</p>
                                        </a>
                                    </li>
                                    <li class="nav-item inner-margin-left" hidden>
                                        <a href="${pageContext.request.contextPath}/Show/Mapgoogle" class="nav-link">
                                            <i class="fa fa-google-plus-circle nav-icon"></i>
                                            <p>谷歌地图</p>
                                        </a>
                                    </li>
                                    <li class="nav-item inner-margin-left">
                                        <a href="${pageContext.request.contextPath}/Show/Mapbaidu" class="nav-link">
                                            <i class="fa fa-paw nav-icon"></i>
                                            <p>百度地图</p>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link">
                            <i class="nav-icon fas fa-edit"></i>
                            <p>
                                文本分析
                                <i class="fas fa-angle-left right"></i>
                            </p>
                        </a>
                        <ul class="nav nav-treeview">
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/News/Source" class="nav-link">
                                    <i class="fa fa-files-o nav-icon"></i>
                                    <p>新闻来源</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/News" onclick="setCookie('pageNum','1',0.1)" class="nav-link">
                                    <i class="fa fa-file-text-o nav-icon"></i>
                                    <p>新闻文本</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/Event" class="nav-link">
                                    <i class="fa fa-clipboard nav-icon"></i>
                                    <p>事件信息</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left" hidden>
                                <a href="" class="nav-link">
                                    <i class="fa fa-chain nav-icon"></i>
                                    <p>西陆网</p>
                                </a>
                            </li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link">
                            <i class="nav-icon fa fa-rocket"></i>
                            <p>
                                武器装备
                                <i class="fas fa-angle-left right"></i>
                            </p>
                        </a>
                        <ul class="nav nav-treeview">
                            <li class="nav-item nav-margin-left">
                                <a href="${pageContext.request.contextPath}/Show/weapon_class" class="nav-link">
                                    <i class="fa fa-plane nav-icon"></i>
                                    <p>武器类别分析</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left" hidden>
                                <a href="" class="nav-link">
                                    <i class="fa fa-fighter-jet nav-icon"></i>
                                    <p>武器百科</p>
                                </a>
                            </li>
                            <li class="nav-item nav-margin-left" hidden>
                                <a href="" class="nav-link">
                                    <i class="fa fa-space-shuttle nav-icon"></i>
                                    <p>武器百科</p>
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </nav>
            <!-- /.sidebar-menu -->
        </div>
        <!-- /.sidebar -->
    </aside>

    <!-- Content Wrapper. Contains page content -->
    <div class="content-wrapper iframe-mode" data-widget="iframe" data-loading-screen="750">
        <div class="nav navbar navbar-expand navbar-white navbar-light border-bottom p-0">
            <div class="nav-item dropdown">
                <a class="nav-link bg-danger dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">关闭</a>
                <div class="dropdown-menu mt-0">
                    <a class="dropdown-item" href="#" data-widget="iframe-close" data-type="all">关闭所有页面</a>
                    <a class="dropdown-item" href="#" data-widget="iframe-close" data-type="all-other">关闭其他页面</a>
                </div>
            </div>
            <a class="nav-link bg-light" href="#" data-widget="iframe-scrollleft"><i class="fas fa-angle-double-left"></i></a>
            <ul class="navbar-nav overflow-hidden" role="tablist"></ul>
            <a class="nav-link bg-light" href="#" data-widget="iframe-scrollright"><i class="fas fa-angle-double-right"></i></a>
            <a class="nav-link bg-light" href="#" data-widget="iframe-fullscreen"><i class="fas fa-expand"></i></a>
        </div>
        <div class="tab-content">
            <div class="tab-empty">
                <img src="${pageContext.request.contextPath}/img/index_background.jpg" style="display: block;margin: 0 auto;width: 100%;height: 100%;filter: Alpha(opacity=50);
opacity: 0.1;">
            </div>
            <div class="tab-loading">
                <div>
                    <h2 class="display-4">Tab is loading <i class="fa fa-sync fa-spin"></i></h2>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- ./wrapper -->
<!--登录  模态框（Modal） -->
<div class="modal fade" id="time_setModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title">设置时间</h4>
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class='col-sm-6'>
                        <div class="form-group">
                            <label>选择开始日期：</label>
                            <!--指定 date标记-->
                            <div class='input-group date' style="display: table" id='datetimepicker1'>
                                <input id="StartTime" type='text' class="form-control" />
                                <span class="input-group-addon">
                                    <span class="glyphicon glyphicon-calendar"></span>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class='col-sm-6'>
                        <div class="form-group">
                            <label>选择结束日期：</label>
                            <!--指定 date标记-->
                            <div class='input-group date' style="display: table" id='datetimepicker2'>
                                <input id="EndTime" type='text' class="form-control" />
                                <span class="input-group-addon">
                                    <span class="glyphicon glyphicon-calendar"></span>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal-footer" >
                <div>
                    <div>
                        <button type="button" class="btn btn-success" onclick="time_set_Pass()">确认</button>
                        <%--							<button id="log_refuse" type="button" class="btn btn-danger col-sm-4" onclick="dologRefuse()">取消</button>--%>
                    </div>
                </div>
            </div>
        </div>
        <!-- /.modal-content -->
    </div>
    <!-- /.modal -->
</div>

<!-- jQuery -->
<script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
<!-- jQuery UI 1.11.4 -->
<script src="${pageContext.request.contextPath}/js/container/jquery-ui.min.js"></script>
<script src="${pageContext.request.contextPath}/js/time/moment-with-locales.js"></script>
<script src="${pageContext.request.contextPath}/js/time/bootstrap-datetimepicker.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
<!-- Resolve conflict in jQuery UI tooltip with Bootstrap tooltip -->
<script>
    $.widget.bridge('uibutton', $.ui.button)
</script>
<script>
    var start_time = "2020-01-01";
    var end_time = "2020-12-31";
    $(function () {
        $('#datetimepicker1').datetimepicker({
            format: 'YYYY-MM-DD',
            locale: moment.locale('zh-cn')
        });
        $('#datetimepicker2').datetimepicker({
            format: 'YYYY-MM-DD',
            locale: moment.locale('zh-cn')
        });
        start_time = $('#StartTime').val();
        end_time = $('#EndTime').val();
        if (typeof start_time != "undefined"){
            document.getElementById("time_start").value = start_time;
            setCookie("start_time",start_time,1);
        }
        if (typeof end_time != "undefined"){
            document.getElementById("time_end").value = end_time;
            setCookie("end_time",end_time,1);
        }
    });
    function time_setting(){
        $('#time_setModal').modal('toggle');
    }
    function time_set_Pass(){
        $('#time_setModal').modal('hide');
        start_time = $('#StartTime').val();
        end_time = $('#EndTime').val();
        console.log(start_time);
        if (typeof start_time != "undefined"){
            document.getElementById("time_start").value = start_time;
            setCookie("start_time",start_time,1);
        }
        if (typeof end_time != "undefined"){
            document.getElementById("time_end").value = end_time;
            setCookie("end_time",end_time,1);
        }
    }
    function goto_link(link_str){
        window.open(link_str);
    }
    window.onload = function(){
        $('#start_page').click();
        setCookie("location","",0.1);
        setCookie("start_time","2020-01-01",1);
        setCookie("end_time","2020-12-31",1);
    };
    $('#iframe-box').bind('DOMAttrModified',function(){
        var iframes = document.getElementsByTagName('iframe');
        var iframei = iframes[iframes.length-1];
        var wid = iframei.style.width;
        var high = iframei.style.height;
        alert(""+wid+" "+high);
        setIframeSizeCookie2(wid,high);
    });
</script>
<!-- Bootstrap 4 -->
<script src="${pageContext.request.contextPath}/js/container/bootstrap.bundle.min.js"></script>
<!-- overlayScrollbars -->
<script src="${pageContext.request.contextPath}/js/container/jquery.overlayScrollbars.min.js"></script>
<!-- AdminLTE App -->
<script src="${pageContext.request.contextPath}/js/container/adminlte.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="${pageContext.request.contextPath}/js/container/demo.js"></script>
</body>
</html>

