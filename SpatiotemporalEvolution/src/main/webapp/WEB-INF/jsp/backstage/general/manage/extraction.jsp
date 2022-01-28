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

    <title>事件抽取</title>
    <!-- Custom styles for this template -->
    <link href="${pageContext.request.contextPath}/css/dashboard.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/news/myblog.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/news/bundle-codinglife.min.css" rel="stylesheet">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap/bootstrap.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/backstage/font-awesome.min.css">
    <link href="${pageContext.request.contextPath}/css/alert/sweetalert.min.css" rel="stylesheet">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/toastr.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
  </head>
  <body>
  <div id="dbs" class="container-fluid">
    <div class="row">
      <div class="col-sm-12 main">
        <h2 class="sub-header">可执行操作</h2>
        <div class="table-responsive">
          <table class="table table-striped">
            <thead>
            <tr>
              <th style="text-align: center;">操作名称</th>
              <th style="text-align: center;">操作</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>模型抽取</td>
              <td>
                <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(1,1)">执行</a>
              </td>
            </tr>
            <tr>
              <td>写入关键句</td>
              <td>
                <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(1,1)">执行</a>
              </td>
            </tr>
            <tr>
              <td>写入事件</td>
              <td>
                <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(1,1)">执行</a>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  </body>
  <!-- jQuery -->
  <script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
  <script src="${pageContext.request.contextPath}/js/alert/sweetalert.min.js"></script>
  <script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
<script>
  function startCrawler(sign,num){
    if (sign===1){
      $.ajax({
        url: "${pageContext.request.contextPath}/Admin/general/crawler/start",
        type: 'POST',
        dataType: 'JSON',
        data: {
          "sign": sign,
          "pyNum": num,
          "time1": getCookie("time1"),
          "time2": getCookie("time2")
        },
        success: function (data) {
          if (data.result === "ok") {
            toastr.success("执行完成！")
          } else {
            toastr.error("操作执行失败！");
          }
        },
        error: function () {
          toastr.error("系统或服务器出错！");
        }
      })
    }
  }
</script>
</html>
