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

  <title>武器表</title>
  <!-- Google Font: Source Sans Pro -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Theme style -->
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/container/adminlte.min.css">
  <!-- 分页相关 -->
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
  <!-- 分页相关 -->
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mypage.css">
</head>
<body>
<div class="container-fluid">
  <div class="row">
    <c:if test="${empty requestScope.get('pageDetil').list}">
      <div class="no_item">
        <span>当前该数据表没有任何内容！</span>
      </div>
    </c:if>
    <c:if test="${!empty requestScope.get('pageDetil').list}">
      <div class="col-sm-12 main">
        <h2 class="sub-header">武器信息表</h2>
        <div class="table-responsive">
          <table class="table table-striped">
            <thead>
            <tr>
              <th>武器名称</th>
              <th>武器类别</th>
              <th>武器小类别</th>
              <th>武器生产国</th>
            </tr>
            </thead>
            <tbody>
            <c:forEach  var="item" items="${requestScope.get('pageDetil').list}">
              <tr>
                <td>${item.weaponName}</td>
                <td>${item.weaponClass}</td>
                <td>${item.weaponSClass}</td>
                <td>${item.weaponCountry}</td>
              </tr>
            </c:forEach>
            </tbody>
          </table>
        </div>
      </div>
    </c:if>
  </div>
</div>
<c:if test="${!empty requestScope.get('pageDetil').list}">
  <!--分页条-->
  <div style="text-align: center">
    <div class="pagination page-num" value="${requestScope.get('pageDetil').pageNum}">
      <ul>
        <c:if test="${requestScope.get('pageDetil').isFirstPage == false }">
          <li><a class="last-page" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('weapon')">上一页</a>
          </li>
        </c:if>
          <li>第${requestScope.get('pageDetil').pageNum}页</li>
        <c:if test="${requestScope.get('pageDetil').isLastPage == false}">
          <li><a class="next-page" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('weapon')">下一页</a>
          </li>
        </c:if>
      </ul>
    </div>
  </div>
</c:if>
<!-- ./wrapper -->
</body>
<script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/fileinput.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
<script>
  function seeDetail(strs) {
    setCookie("databaseName",strs,1);
  }
</script>
</html>

