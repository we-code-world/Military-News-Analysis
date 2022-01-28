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

  <title>数据获取</title>
  <link href="https://cdn.bootcss.com/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css" rel="stylesheet">
  <link href="${pageContext.request.contextPath}/css/news/myblog.css" rel="stylesheet">
  <link href="${pageContext.request.contextPath}/css/news/bundle-codinglife.min.css" rel="stylesheet">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap/bootstrap.min.css">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/backstage/font-awesome.min.css">
  <link href="${pageContext.request.contextPath}/css/alert/sweetalert.min.css" rel="stylesheet">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/toastr.min.css">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
  <!-- Custom styles for this template -->
  <link href="${pageContext.request.contextPath}/css/dashboard.css" rel="stylesheet">
</head>
<body>
<div id="dbs" class="container-fluid">
  <div class="row">
    <div class="col-sm-12 main">
      <h2 class="sub-header">数据获取</h2>
      <div class="table-responsive">
        <table class="table table-striped">
          <thead>
          <tr>
            <th style="text-align: center;">数据来源</th>
            <th style="text-align: center;">操作</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td><a href="http://mil.huanqiu.com/">环球军事网</a></td>
            <td>
              <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(1,1)">获取文章链接</a>
              <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(1,2)">爬取文章</a>
            </td>
          </tr>
          <tr>
            <td><a href="http://www.81.cn/">中国军网</a></td>
            <td>
              <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(2,1)">获取文章链接</a>
              <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(2,2)">爬取文章</a>
            </td>
          </tr>
          <tr>
            <td><a href="http://www.xilu.com/">西陆军网</a></td>
            <td>
              <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(3,1)">获取文章链接</a>
              <a class="btn btn-success" href="javascript:void(0)" onclick="startCrawler(3,2)">爬取文章</a>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
<div class="row" style="margin-left: 100px;margin-right: 120px">
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
</body>
<!-- jQuery -->
<script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
<script src="${pageContext.request.contextPath}/js/alert/sweetalert.min.js"></script>
<script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
<script src="${pageContext.request.contextPath}/js/time/moment-with-locales.js"></script>
<script src="https://cdn.bootcss.com/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js"></script>
<script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
<script src="${pageContext.request.contextPath}/js/container/bootstrap.bundle.min.js"></script>
<script>
  var if_run = 0;
  var offset = 0;
  var num = 1;
  async function startCrawler(sign,this_num){
    if_run = 1;
    offset = 0;
    num = this_num;
    while(if_run)await runCrawler(sign);
  }
  async function runCrawler(sign) {
    if (sign===1){
      await $.ajax({
        url: "${pageContext.request.contextPath}/Admin/general/crawler/start",
        type: 'POST',
        dataType: 'JSON',
        data: {
          "sign": sign,
          "pyNum": num,
          "offset":offset,
          "time1": getCookie("time1"),
          "time2": getCookie("time2")
        },
        success: function (data) {
          if (data.result === "ok") {
            if_run = data.IF_RUN;
            offset = data.OFFSET;
            console.log(data.Content);
            toastr.success("爬取完成！")
          } else {
            toastr.error("爬取数据失败！");
          }
        },
        error: function () {
          toastr.error("系统或服务器出错！");
        }
      })
    }
  }
  var start_time = "2021-01-01";
  var end_time = "2021-12-31";
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
      setCookie("time1",start_time,1);
    }
    if (typeof end_time != "undefined"){
      setCookie("time2",end_time,1);
    }
  });
  window.onload = function(){
    setCookie("time1","2021-01-01",1);
    setCookie("time2","2021-12-31",1);
  };
</script>
</html>
