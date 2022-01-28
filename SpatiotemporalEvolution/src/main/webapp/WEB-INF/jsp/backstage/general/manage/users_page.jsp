<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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

    <title>用户管理</title>
    <!-- Google Font: Source Sans Pro -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
    <!-- Theme style -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/container/adminlte.min.css">
    <!-- 分页相关 -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mypage.css">
  </head>
  <body>
  <!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper" style="margin:0;">
      <!-- Main content -->
      <section class="content">
          <div class="row">
              <c:if test="${empty requestScope.get('user_list')}">
                  <div style="text-align: center;width: 100%;">
                      <br>
                      当前还没有用户使用！请耐心等待哟~
                      <br>
                  </div>
              </c:if>
              <c:forEach var="User" items="${requestScope.get('user_list')}">
                  <div class="col-md-4">
                      <!-- Widget: user widget style 1 -->
                      <div class="card card-widget widget-user">
                          <!-- Add the bg color to the header using any of the bg-* classes -->
                          <div class="widget-user-header text-white"
                               style="background: url('${pageContext.request.contextPath}/img/${User.getBackground()}') center center;">
                              <h3 class="widget-user-username text-left" style="margin:0 0 10px 0">
                                  <c:if test="${User.getSex() == 1}">
                                      <i class="fa fa-mars man-blue" aria-hidden="true"></i>
                                  </c:if>
                                  <c:if test="${User.getSex() == 0}">
                                      <i class="fa fa-mars-stroke woman-pink" aria-hidden="true"></i>
                                  </c:if>
                              </h3>
                              <h6 class="text-left">Email:${User.getEmail()}</h6>
                              <h6 class="text-left">Telephone:${User.getTelephone()}</h6>
                              <h6 class="text-left">Address:${User.getAddress()}</h6>
                          </div>
                          <div class="widget-user-image">
                              <img class="img-circle" src="${pageContext.request.contextPath}/face/${User.getPhoto()}" alt="User Avatar">
                          </div>
                          <div class="card-footer">
                              <div class="row">
                                  <div class="col-sm-4 border-right">
                                      <div class="description-block">
                                          <h5 class="description-header">${User.getDays()}</h5>
                                          <span class="description-text">Days</span>
                                      </div>
                                      <!-- /.description-block -->
                                  </div>
                                  <!-- /.col -->
                                  <div class="col-sm-4 border-right">
                                      <div class="description-block">
                                          <h5 class="description-header">${User.getFeedback()}</h5>
                                          <span class="description-text">FEEDBACK</span>
                                      </div>
                                      <!-- /.description-block -->
                                  </div>
                                  <!-- /.col -->
                                  <div class="col-sm-4">
                                      <div class="description-block">
                                          <h5 class="description-header">${User.getDownload()}</h5>
                                          <span class="description-text">DOWNLOAD</span>
                                      </div>
                                      <!-- /.description-block -->
                                  </div>
                                  <!-- /.col -->
                              </div>
                              <!-- /.row -->
                          </div>
                      </div>
                      <!-- /.widget-user -->
                  </div>
                  <!-- /.col -->
              </c:forEach>
          </div>
      </section>
  </div>
  <!--分页条-->
  <div style="text-align: center">
      <div class="pagination page-num" value="${requestScope.get('pageDetil').pageNum}">
          <ul>
              <c:if test="${requestScope.get('pageDetil').isFirstPage == false }">
                  <li><a class="btn btn-success last-page" href="${pageContext.request.contextPath}/Admin/general/users">上一页</a>
                  </li>
              </c:if>
              <li>第${requestScope.get('pageDetil').pageNum}页</li>
              <c:if test="${requestScope.get('pageDetil').isLastPage == false}">
                  <li><a class="btn btn-success next-page" href="${pageContext.request.contextPath}/Admin/general/users">下一页</a>
                  </li>
              </c:if>
          </ul>
      </div>
  </div>
  <!-- ./wrapper -->
  </body>
  <script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
  <script src="${pageContext.request.contextPath}/js/myjs/fileinput.min.js"></script>
  <script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
</html>

