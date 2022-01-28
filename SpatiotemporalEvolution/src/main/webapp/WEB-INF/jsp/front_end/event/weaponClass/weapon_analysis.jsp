<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page import="net.sf.json.JSONObject" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>事件分析</title>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <!-- 引入 echarts.js -->
    <script src="${pageContext.request.contextPath}/js/echarts.min.js"></script>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body class="scroller scroller-1" style="width:100%;height:600px;">
<div style="text-align: center;">
    <div class="pc-search-filter-check" data-spm="filter">
        <div class="bar-group price-bar">
                <span>
                    <input  id="check_all" type="checkbox" onclick="Check_box('all',this)">
                    <label id="label_all">全部勾选</label>
                </span>
        </div>
        <div class="bar-group price-bar">
                <span>
                    <input  id="check_pie" type="checkbox" checked="checked" onclick="Check_box('pie',this)">
                    <label >旭日图</label>
                </span>
        </div>
        <div class="bar-group price-bar" onclick="Check_box('dia',this)">
                <span>
                    <input  id="check_dia" type="checkbox">
                    <label >堆叠柱状图</label>
                </span>
        </div>
    </div>
</div>
<div id="left_chart" class="div-one">
    <div id="DomPie" class="div-one"></div>
    <div id="DomPie2" class="div-none"></div>
</div>
<script type="text/javascript">
    var chartDomPie = document.getElementById('DomPie');
    var myChartPie = echarts.init(chartDomPie);
    var chartDomPie2 = document.getElementById('DomPie2');
    var myChartPie2 = echarts.init(chartDomPie2);
    var mydata = [];
    var myseries = [];
    var my_inner_data = [];
    <c:forEach var="item" items="${requestScope.get('ClassJson')['data']}">
    <c:if test="${requestScope.get('WeaponJson')[item]!=0}">
    my_inner_data = [];
    <c:forEach var="inner" items="${requestScope.get('SClassJson')[item]}">
    <c:if test="${requestScope.get('WeaponJson')[inner]!=0}">
    my_inner_data.push({
        name: "${inner}",
        value:${requestScope.get('WeaponJson')[inner]}
    });
    myseries.push({
        type: 'bar',
        data: [0, 0,${requestScope.get('WeaponJson')[inner]}],
        coordinateSystem: 'polar',
        name: "${inner}",
        stack: 'a',
        emphasis: {
            focus: 'series'
        }
    });
    </c:if>
    </c:forEach>
    mydata.push({
        name: "${item}",
        value:${requestScope.get('WeaponJson')[item]},
        children:my_inner_data
    });
    myseries.push({
        type: 'bar',
        data: [0, ${requestScope.get('WeaponJson')[item]}, 0],
        coordinateSystem: 'polar',
        name: "${item}",
        stack: 'a',
        emphasis: {
            focus: 'series'
        }
    });
    </c:if>
    </c:forEach>
    option = {
        series: {
            radius: ['25%', '85%'],
            type: 'sunburst',
            data: mydata
        }
    };
    Pieoption = {
        angleAxis: {
        },
        radiusAxis: {
            type: 'category',
            data: [' ', '大类别', '小类别']
        },
        polar: {
        },
        series: myseries
    };
    myChartPie.setOption(option);
    myChartPie2.setOption(Pieoption);
    function Check_box(witch,checkbox){
        var ck_all = document.getElementById('check_all');
        var lb_all = document.getElementById('label_all');
        var ck_pie = document.getElementById('check_pie');
        var ck_dia = document.getElementById('check_dia');
        var crt_left = document.getElementById('left_chart');
        var crt_pie = document.getElementById('DomPie');
        var crt_dia = document.getElementById('DomPie2');
        if (witch == 'all') {
            if (checkbox.checked==true) {
                ck_pie.checked=true;
                ck_dia.checked=true;
            }else{
                ck_pie.checked=false;
                ck_dia.checked=false;
                lb_all.innerText="全部勾选";
                crt_left.className = "";
                crt_pie.className = "";
                crt_pie.className = "";
            }
        }else if (witch == 'pie') {
            if (ck_pie.checked==true) {
                crt_left.className = "div-one";
                if (ck_dia.checked) {
                    crt_dia.className = "div-left-all";
                    crt_pie.className = "div-left-all";
                }else{
                    crt_pie.className = "div-one";
                }
            }else{
                ck_all.checked=false;
                lb_all.innerText="全部勾选";
                if (ck_dia.checked) {
                    crt_dia.className = "div-one";
                    crt_pie.className = "div-none";
                }else{
                    crt_pie.className = "div-none";
                }
            }
        }else if (witch == 'dia') {
            if (ck_dia.checked==true) {
                crt_left.className = "div-one";
                if (ck_pie.checked) {
                    crt_pie.className = "div-left-all";
                    crt_dia.className = "div-left-all";
                }else{
                    crt_dia.className = "div-one";
                }
            }else{
                ck_all.checked=false;
                lb_all.innerText="全部勾选";
                if (ck_pie.checked) {
                    crt_pie.className = "div-one";
                    crt_dia.className = "div-none";
                }else{
                    crt_dia.className = "div-none";
                }
            }
        }else{
            console.log(witch+checkbox);
        }
        if (ck_dia.checked && ck_pie.checked) {
            ck_all.checked = true;
            lb_all.innerText="取消勾选";
            crt_left.className = "div-one";
            crt_pie.className = "div-left-all";
            crt_dia.className = "div-left-all";
        }
        myChartPie.resize();
        myChartPie2.resize();
    }
</script>
</body>
</html>