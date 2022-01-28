<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html style="width: 100%;height:100%;">
<head>
    <meta charset="utf-8">
    <meta name="viewport">
    <title>事件发展</title>
    <link rel="icon" href="${pageContext.request.contextPath}/icons/favicon.ico">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
    <!-- 引入 echarts.js -->
    <script src="${pageContext.request.contextPath}/js/echarts.min.js"></script>
    <!-- jQuery -->
    <script src="${pageContext.request.contextPath}/js/container/jquery.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
    <style>
        a {font-size:16px}
        a:link {color: #17a2b8; text-decoration:none;}
        a:active{color: #007bff; }
        a:visited {color:#007bff;text-decoration:none;}
        a:hover {color: #007bff; text-decoration:none;}
    </style>
</head>
<body>
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="Link" class="iframe-develop"></div>
<!--<div id="main" hidden style="width: 600px;height:400px;"></div>-->
<script type="text/javascript">
    var chartDom = document.getElementById('Link');
    var myChart = echarts.init(chartDom);
    var option;
    var data = [];
    var links = [];
    var labels;
    var content = 1;//1为武器，2为地点

    labels = ['交易','演习','冲突','研发','事故','挑衅'];
    var now_sign = 0;
    <c:forEach var="timePoint" items="${requestScope.get('time_point')}" >
        data.push(["${timePoint.time}", ${timePoint.x}, ${timePoint.y}]);
    </c:forEach>
    console.log(data);
    links = data.map(function (item, i) {
        return {
            source: Math.round(Math.random() * (i-1) +1),
            target: i+1,
            label: {
                show: true,
                formatter: function (params) {
                    // 假设为series 1
                    if (params.seriesIndex === 1) {
                        return "事件";
                    }else if (params.seriesIndex === 0 && now_sign === 0) {
                        // 假设为series 0
                        if (content===1)
                            return '武器';
                        else if (content === 2)
                            return '地点';
                    }else{
                        // 假设为其他
                        return "武器";
                    }
                }
            }
        };
    });

    //console.log(data);
    option = {
        title: {
            left: 'center',
            text: '事件——武器关联分析',
        },
        tooltip: {
            trigger:'item',
            enterable:true,
            position:function (point, params, dom, rect, size) {
                // 假设为series 0
                if (params.seriesIndex == 0) {
                    return null;
                }else if (params.seriesIndex == 1) {
                    // 假设为series 1
                    return 'right';
                }else{
                    // 假设为其他
                    return 'right';
                }
            },
            formatter: function (params) {
                // 假设为series 1
                if (params.seriesIndex === 1) {
                    return '<p>时间some text，地点some text，武器some text（<a href="${pageContext.request.contextPath}/Show/News/Detail" onclick="setCookie(\'pageID\','+'2,0.02)">溯源</a>）</p>';
                }else if (params.seriesIndex === 0 && now_sign === 0) {
                    // 假设为series 0
                    if (content===1)
                        return '<p>武器<a href="https://www.1234.com">some text</a></p>';
                    else if (content === 2)
                        return '<p>地点<a href="https://www.1234.com">some text</a></p>';
                }else{
                    // 假设为其他
                    return '<p>武器<a href="https://www.1234.com">详细</a></p>';
                }
            }
        },
        legend: {
            orient: 'vertical',
            top: 'bottom',
            left: 'right',
        },
        xAxis: {
            type: 'time',
        },
        yAxis: {
            type: 'value',
        },
        visualMap: [{
            type : 'piecewise',
            pieces: [
                {value: 0, label: labels[0], color: 'red'},
                {value: 1, label: labels[1], color: 'yellow'},
                {value: 2, label: labels[2], color: 'green'},
                {value: 3, label: labels[3], color: 'black'},
                {value: 4, label: labels[4], color: 'cyan'},
                {value: 5, label: labels[5], color: 'purple'}
            ],
            hoverLink : true,
            dimension:2,
            seriesIndex: 1,
        },{
            type : 'piecewise',
            pieces: [
                {value: -1, label: '0', color: 'green'},
            ],
            dimension:2,
            seriesIndex: 0,
            show:false
        }],
        dataZoom: [
            {   // 这个dataZoom组件，默认控制x轴。
                type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                start: 0,      // 左边在 10% 的位置。
                end: 8         // 右边在 60% 的位置。
            },
            {   // 这个dataZoom组件，也控制x轴。
                type: 'inside', // 这个 dataZoom 组件是 inside 型 dataZoom 组件
                start: 0,      // 左边在 10% 的位置。
                end: 8         // 右边在 60% 的位置。
            }
        ],
        series: [
            {
                type: 'graph',
                coordinateSystem: 'cartesian2d',
                symbolSize: 30,
                edgeSymbol: ['circle', 'arrow'],
                edgeSymbolSize: [2, 12],
                data: data,
                links:links,
                lineStyle: {
                    color: '#2f4554'
                }
            },{
                type: 'scatter',
                symbolSize: 30,
                data: data,
                label: {
                    show: true,
                    formatter: function (params) {
                        // 假设为series 1
                        if (params.seriesIndex === 1) {
                            return '事件';
                        }else if (params.seriesIndex === 0 && now_sign === 0) {
                            // 假设为series 0
                            if (content===1)
                                return '武器';
                            else if (content === 2)
                                return '地点';
                        }else{
                            // 假设为其他
                            return '武器';
                        }
                    }
                }
            }
        ]

    };

    option && myChart.setOption(option);
    // 处理点击事件并且跳转到相应的页面
    myChart.on('click', function (params) {
        if (params.seriesIndex == 0) {
            //window.open('https://www.baidu.com')
        }else if(params.seriesIndex == 1){
            //window.open('https://www.1234.com')
        }else{
            console.log(params)
        }
        //console.log(params)
        //document.getElementById('analysis').href = 'file:///D:/htmlPages/html/date.html';
        //?wd=' + encodeURIComponent(params.name);
        //document.getElementById('analysis').click();
        //window.open('https://www.baidu.com')//?wd=' + encodeURIComponent(params.name));
    });
    function splash() {
        
    }
</script>
</body>
</html>