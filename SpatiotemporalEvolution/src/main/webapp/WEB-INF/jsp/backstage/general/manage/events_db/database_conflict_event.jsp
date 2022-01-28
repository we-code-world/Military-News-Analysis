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

  <title>研发事件表</title>
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
        <h2 class="sub-header">冲突事件表</h2>
        <div class="table-responsive">
          <table class="table table-striped">
            <thead>
            <tr>
              <th>冲突时间</th>
              <th>冲突地点</th>
              <th>造成损害的国家</th>
              <th>受到损害的国家</th>
              <th>事件触发词</th>
              <th>操作</th>
            </tr>
            </thead>
            <tbody>
            <c:forEach  var="item" items="${requestScope.get('pageDetil').list}">
              <tr>
                <td>${item.showDate()}</td>
                <td>${item.conflictEventLocation}</td>
                <td>${item.activeSubject}</td>
                <td>${item.sufferSubject}</td>
                <td>${item.conflictEventTrigger}</td>
                <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/Events/Detail"  onclick="seeID(${item.conflictEventID})">查看详情</a></td>
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
          <li><a class="last-page  btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('conflict')">上一页</a>
          </li>
        </c:if>
          <li>第${requestScope.get('pageDetil').pageNum}页</li>
        <c:if test="${requestScope.get('pageDetil').isLastPage == false}">
          <li><a class="next-page btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('conflict')">下一页</a>
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
  function seeID(strs) {
    setCookie("EventID",strs,1);
  }
</script>
</html>

