<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>武器事件关联分析</title>
    <!-- Theme style -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/container/adminlte.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
    <!-- 引入 echarts.js -->
    <script src="${pageContext.request.contextPath}/js/echarts.min.js"></script>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap/bootstrap.min.css">
    <!-- jQuery -->
    <script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
    <!-- AdminLTE App -->
    <script src="${pageContext.request.contextPath}/js/container/adminlte.js"></script>
    <script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
    <script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
</head>
<body  class="scroller scroller-1" style="width:100%;height:600px">
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="Develop" class="div-one"></div>
<div class="right-top btn-default" hidden>
    <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
        <li class="nav-item">
            <a href="#" class="nav-link">
                <i class="nav-icon fa fa-desktop"></i>
                <p>
                    国家或地区
                    <i class="right fas fa-angle-left"></i>
                </p>
            </a>
            <ul class="nav nav-treeview">
                <li class="nav-item">
                    <a onclick="" class="nav-link">
                        <i class="fa fa-home nav-icon"></i>
                        <p>中国</p>
                    </a>
                </li>
            </ul>
        </li>
        <li class="nav-item">
            <a href="#" class="nav-link">
                <i class="nav-icon fa fa-desktop"></i>
                <p>
                    武器类别
                    <i class="right fas fa-angle-left"></i>
                </p>
            </a>
            <ul class="nav nav-treeview">
                <li class="nav-item">
                    <a onclick="" class="nav-link">
                        <i class="fa fa-home nav-icon"></i>
                        <p>武器</p>
                    </a>
                </li>
            </ul>
        </li>
    </ul>
</div>
<script type="text/javascript">
    var chartDom = document.getElementById('Develop');
    var myChart = echarts.init(chartDom);
    var dataMap=${requestScope.get("dataMap")};
    var yearList=${requestScope.get("yearArray")};
    //测试
    var mydata = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'];

    var myoptions = [];
    for (var i = 0; i < yearList.length; i++) {
        var yearstr = yearList[i];
        myoptions.push({
            title: {text: yearstr+'年各类军事事件数'},
            series: [
                {data: dataMap.practice[yearstr]},
                {data: dataMap.transaction[yearstr]},
                {data: dataMap.conflict[yearstr]},
                {data: dataMap.RD[yearstr]},
                {data: dataMap.accident[yearstr]},
                {data: dataMap.provocative[yearstr]},
                {data: [
                        {name: '演习', value: dataMap.practice[yearstr+'sum']},
                        {name: '交易', value: dataMap.transaction[yearstr+'sum']},
                        {name: '冲突', value: dataMap.conflict[yearstr+'sum']},
                        {name: '研发', value: dataMap.RD[yearstr+'sum']},
                        {name: '事故', value: dataMap.accident[yearstr+'sum']},
                        {name: '挑衅', value: dataMap.provocative[yearstr+'sum']}
                    ]}
            ]
        });
    }

    option = {
        baseOption: {
            timeline: {
                axisType: 'category',
                // realtime: false,
                // loop: false,
                autoPlay: true,
                // currentIndex: 2,
                playInterval: 1000,
                // controlStyle: {
                //     position: 'left'
                // },
                data: yearList,
                label: {
                    formatter : function(s) {
                        return (new Date(s)).getFullYear();
                    }
                }
            },
            title: {
                subtext: '当前为${requestScope.get('location')}地点'
            },
            tooltip: {
            },
            legend: {
                left: 'right',
                data: ['演习', '交易', '冲突', '研发', '事故', '挑衅'],
                selected: {
                    '研发': false, '事故': false, '挑衅': false
                }
            },
            calculable : true,
            grid: {
                top: 80,
                bottom: 100,
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow',
                        label: {
                            show: true,
                            formatter: function (params) {
                                return params.value.replace('\n', '');
                            }
                        }
                    }
                }
            },
            xAxis: [
                {
                    'type':'category',
                    'axisLabel':{'interval':0},
                    'data':mydata,
                    splitLine: {show: false}
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '事件数'
                }
            ],
            series: [
                {name: '演习', type: 'bar'},
                {name: '交易', type: 'bar'},
                {name: '冲突', type: 'bar'},
                {name: '研发', type: 'bar'},
                {name: '事故', type: 'bar'},
                {name: '挑衅', type: 'bar'},
                {
                    name: '事件类型占比',
                    type: 'pie',
                    center: ['45%', '15%'],
                    radius: '28%',
                    z: 100
                }
            ]
        },
        options: myoptions
    };
    option && myChart.setOption(option);
    function splash() {
        //测试
        $.ajax({
            url: "${pageContext.request.contextPath}/Show/weapon_event/getdata",
            type: 'POST',
            dataType: 'JSON',
            data: {
                "catelogid": 1,
                "weaponSClass":"",
                "weaponClass":""
            },
            success: function (data) {
                if (data.result === "ok") {
                    dataMap = data.dataMap;
                    yearList = data.yearArray;
                    console.log(dataMap);
                    myoptions = [];
                    for (var i = 0; i < yearList.length; i++) {
                        var yearstr = yearList[i];
                        myoptions.push({
                            title: {text: yearstr+'年各类军事事件数'},
                            series: [
                                {data: dataMap.practice[yearstr]},
                                {data: dataMap.transaction[yearstr]},
                                {data: dataMap.conflict[yearstr]},
                                {data: dataMap.RD[yearstr]},
                                {data: dataMap.accident[yearstr]},
                                {data: dataMap.provocative[yearstr]},
                                {data: [
                                        {name: '演习', value: dataMap.practice[yearstr+'sum']},
                                        {name: '交易', value: dataMap.transaction[yearstr+'sum']},
                                        {name: '冲突', value: dataMap.conflict[yearstr+'sum']},
                                        {name: '研发', value: dataMap.RD[yearstr+'sum']},
                                        {name: '事故', value: dataMap.accident[yearstr+'sum']},
                                        {name: '挑衅', value: dataMap.provocative[yearstr+'sum']}
                                    ]}
                            ]
                        });
                    }
                    myChart.setOption({
                        baseOption: {
                            timeline:{
                                data: yearList
                            },
                            title: {
                                subtext: '当前为'+data.location+'地点'
                            },
                            xAxis:[
                                {
                                    'type':'category',
                                    'axisLabel':{'interval':0},
                                    'data':mydata,
                                    splitLine: {show: false}
                                }
                            ]
                        },
                        options: myoptions
                    });
                } else {
                    toastr.error("数据提交失败！");
                }
            },
            error: function () {
                toastr.error("系统或服务器出错！");
            }
        });
    }
</script>
</body>
</html>