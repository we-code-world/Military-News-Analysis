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

  <title>事件结果管理</title>
  <!-- Bootstrap core CSS -->
  <link href="${pageContext.request.contextPath}/css/bootstrap/bootstrap.min.css" rel="stylesheet">
  <!-- Custom styles for this template -->
  <link href="${pageContext.request.contextPath}/css/dashboard.css" rel="stylesheet">

</head>
<body>
<div id="dbs" class="container-fluid">
  <div class="row">
    <div class="col-sm-12 main">
      <h2 class="sub-header">抽取结果</h2>
      <div class="table-responsive">
        <table class="table table-striped">
          <thead>
          <tr>
            <th style="text-align: center;">编号</th>
            <th style="text-align: center;">结果分类</th>
            <th style="text-align: center;">操作</th>
          </tr>
          </thead>
          <tbody>
          <tr hidden>
            <td>1</td>
            <td>关键句抽取结果</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('key_sentence')">详情</a></td>
          </tr>
          <tr>
            <td>1</td>
            <td>研发类事件集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('rd')">详情</a></td>
          </tr>
          <tr>
            <td>2</td>
            <td>事故类事件集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('accident')">详情</a></td>
          </tr>
          <tr>
            <td>3</td>
            <td>冲突类事件集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('conflict')">详情</a></td>
          </tr>
          <tr>
            <td>4</td>
            <td>军事演习事件集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('practice')">详情</a></td>
          </tr>
          <tr>
            <td>5</td>
            <td>挑衅类事件集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('provocative')">详情</a></td>
          </tr>
          <tr>
            <td>6</td>
            <td>交易类事件集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('transaction')">详情</a></td>
          </tr>
          <tr hidden>
            <td>8</td>
            <td>武器信息集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('weapon')">详情</a></td>
          </tr>
          <tr hidden>
            <td>9</td>
            <td>地点信息集</td>
            <td><a class="btn btn-success" href="${pageContext.request.contextPath}/Admin/general/event/list" onclick="seeDetail('locationPage')">详情</a></td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</body>
<!-- jQuery -->
<script src="${pageContext.request.contextPath}/js/backstage/jquery.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/fileinput.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
<script>
  function seeDetail(strs) {
    setCookie("databaseName",strs,1);
  }
  function back_index() {
    delCookie("databaseName");
  }
</script>
</html>

