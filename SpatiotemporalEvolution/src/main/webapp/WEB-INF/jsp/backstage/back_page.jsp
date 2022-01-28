<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" href="${pageContext.request.contextPath}/icons/favicon.ico" type="image/ico" />

    <title>后台管理</title>

    <!-- Bootstrap -->
    <link href="${pageContext.request.contextPath}/css/backstage/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="${pageContext.request.contextPath}/css/backstage/font-awesome.min.css" rel="stylesheet">

    <link href="${pageContext.request.contextPath}/css/mycss/mystyle.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/mycss/myCustom.css" rel="stylesheet">
  </head>

  <body class="nav-md no-scroll">
    <div class="container body">
      <div class="main_container">
        <div id="left" class="col-md-3 left_col">
          <div class="left_col scroll-view">
            <div class="navbar nav_title" style="border: 0;">
              <a href="${pageContext.request.contextPath}/Admin/detail" class="site_title"><i class="fa fa-user"></i> <span>后台管理系统</span></a>
            </div>

            <!-- menu profile quick info -->
            <div class="profile clearfix">
              <div class="profile_pic">
                <img src="${pageContext.request.contextPath}/face/user-grey.png" alt="..." class="img-circle profile_img">
              </div>
              <div class="profile_info">
                <span>欢迎你，</span>
                <h2>管理员${requestScope.get('admin_name')}</h2>
              </div>
            </div>
            <!-- /menu profile quick info -->
            <br />

            <!-- sidebar menu -->
            <div id="sidebar-menu" class="main_menu_side hidden-print main_menu">
              <div class="menu_section">
                <h3>通用</h3>
                <ul class="nav side-menu">
                  <li><a><i class="fa fa-home"></i>主页<span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/center')">展示中心</a></li>
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/change')">修改中心</a></li>
                    </ul>
                  </li>
                  <li><a><i class="fa fa-edit"></i>管理<span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/users')">用户管理</a></li>
                      <li><a href="javascript:void(0);">数据管理<span class="fa fa-chevron-down"></span></a>
                        <ul class="nav child_menu">
                          <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/crawler')">数据获取</a></li>
                          <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/news')">数据源</a></li>
                          <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/extraction')">事件抽取</a></li>
                          <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/events')">抽取结果</a></li>
                          <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/human')">人工标注</a></li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                  <li><a><i class="fa fa-desktop"></i>日志<span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/system')">系统日志</a></li>
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/server')">服务日志</a></li>
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/action')">操作日志</a></li>
                    </ul>
                  </li>
                  <li><a><i class="fa fa-commenting-o"></i>消息<span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/email')">邮箱</a></li>
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/general/feedback')">用户反馈</a></li>
                    </ul>
                  </li>
                </ul>
              </div>
              <div class="menu_section">
                <h3>其它</h3>
                <ul class="nav side-menu">
                  <li><a><i class="fa fa-windows"></i>附加功能<span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/others/load')">上传文件</a></li>
                    </ul>
                  </li>
                  <li><a><i class="fa fa-bug"></i>专业功能<span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/others/crawler')">修改爬虫</a></li>
                      <li><a href="javascript:void(0);" onclick="set_src('/Admin/others/config')">修改配置</a></li>
                    </ul>
                  </li>
                </ul>
              </div>

            </div>
            <!-- /sidebar menu -->

            <!-- /menu footer buttons -->
            <div class="sidebar-footer hidden-small" hidden>
              <a data-toggle="tooltip" data-placement="top" title="Settings">
                <span class="glyphicon glyphicon-cog" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="FullScreen">
                <span class="glyphicon glyphicon-fullscreen" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="Lock">
                <span class="glyphicon glyphicon-eye-close" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="Logout" href="${pageContext.request.contextPath}/Admin/logout">
                <span class="glyphicon glyphicon-off" aria-hidden="true"></span>
              </a>
            </div>
            <!-- /menu footer buttons -->
          </div>
        </div>

        <!-- top navigation -->
        <div class="top_nav">
          <div id="nav_top" class="nav_menu">
              <div class="nav toggle">
                <a id="menu_toggle"><i class="fa fa-bars"></i></a>
              </div>
              <nav class="nav navbar-nav">
              <ul class=" navbar-right">
                <li class="nav-item dropdown open" style="padding-left: 15px;">
                  <a href="javascript:void(0);" class="user-profile dropdown-toggle" aria-haspopup="true" id="navbarDropdown" data-toggle="dropdown" aria-expanded="false">
                    <img src="${pageContext.request.contextPath}/face/user-grey.png" alt="photo">${requestScope.get('adminname')}
                  </a>
                  <div class="dropdown-menu dropdown-usermenu pull-right" aria-labelledby="navbarDropdown">
                      <a class="dropdown-item"  href="javascript:void(0);" hidden>
                        <span class="badge bg-red pull-right">50%</span>
                        <span>设置中心</span>
                      </a>
                    <a class="dropdown-item"  href="javascript:void(0);" hidden>帮助文档</a>
                    <a class="dropdown-item"  href="${pageContext.request.contextPath}/Admin/logout"><i class="fa fa-sign-out pull-right"></i>退出登录</a>
                  </div>
                </li>

                <li role="presentation" class="nav-item dropdown open" hidden>
                  <a href="javascript:void(0);" class="dropdown-toggle info-number" id="navbarDropdown1" data-toggle="dropdown" aria-expanded="false">
                    <i class="fa fa-envelope-o"></i>
                    <span class="badge bg-green">6</span>
                  </a>
                  <ul class="dropdown-menu list-unstyled msg_list" role="menu" aria-labelledby="navbarDropdown1">
                    <li class="nav-item">
                      <a class="dropdown-item">
                        <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li class="nav-item">
                      <a class="dropdown-item">
                        <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li class="nav-item">
                      <a class="dropdown-item">
                        <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li class="nav-item">
                      <a class="dropdown-item">
                        <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li class="nav-item">
                      <div class="text-center">
                        <a class="dropdown-item" href="">
                          <strong>See All Alerts</strong>
                          <i class="fa fa-angle-right"></i>
                        </a>
                      </div>
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
          </div>
        </div>
        <!-- /top navigation -->
        <div class="right_col" role="main">
          <iframe id="iframe" width="100%" frameborder="0" src="${pageContext.request.contextPath}/Admin/general/center"></iframe>
        </div>
      </div>
    </div>

    <!-- jQuery -->
    <script src="${pageContext.request.contextPath}/js/backstage/jquery.min.js"></script>
    <!-- Bootstrap -->
    <script src="${pageContext.request.contextPath}/js/backstage/bootstrap.bundle.min.js"></script>
    <!-- Custom Theme Scripts -->
    <script src="${pageContext.request.contextPath}/js/myjs/myCustom.js"></script>

	<script>
      var iframe_body = $('#iframe');
      var win_height=$(window).height();
      var nav_height=$('#nav_top').outerHeight(true)+2;
      $('#sidebar-menu').height(win_height);
      iframe_body.height(win_height-nav_height);
      function set_src(strs) {
        document.getElementById('iframe').src="${pageContext.request.contextPath}" + strs;
      }
    </script>
  </body>
</html>
