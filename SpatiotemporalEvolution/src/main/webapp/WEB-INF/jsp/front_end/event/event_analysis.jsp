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
                    <label >饼图</label>
                </span>
        </div>
        <div class="bar-group price-bar" onclick="Check_box('dia',this)">
                <span>
                    <input  id="check_dia" type="checkbox">
                    <label >二部图</label>
                </span>
        </div>
        <div class="bar-group price-bar" onclick="Check_box('his',this)">
                <span>
                    <input  id="check_his" type="checkbox">
                    <label >直方图</label>
                </span>
        </div>
    </div>
</div>
<div id="left_chart" class="div-one">
    <div id="PieChart" class="div-one"></div>
    <div id="Diagram" class="div-none"></div>
</div>
<div id="Histogram" class="div-none"></div>
<script type="text/javascript">
    //Pie
    var chartDomPie = document.getElementById('PieChart');
    var myChartPie = echarts.init(chartDomPie);
    var Pieoption;

    //
    var chartDomDia = document.getElementById('Diagram');
    var myChartDia = echarts.init(chartDomDia);
    var Diaoption;

    //
    var app = {};
    var chartDomHis = document.getElementById('Histogram');
    var myChartHis = echarts.init(chartDomHis);
    var Hisoption;
    var posList;

    //Pie
    Pieoption = {
        title: {
            text: '事件类型占比',
            subtext: '',
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [
            {
                name: '类型',
                type: 'pie',
                radius: '50%',
                data: [
                    {value: 1048, name: '演习'},
                    {value: 735, name: '交易'},
                    {value: 580, name: '冲突'},
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 0,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    //Diagram
    Diaoption = {
        title: {
            text: '二部图',
            subtext: '',
            left: 'center'
        },
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
            {
                type: 'graph',
                layout: 'none',
                symbolSize: 50,
                roam: true,
                label: {
                    show: true
                },
                edgeSymbol: ['circle', 'arrow'],
                edgeSymbolSize: [4, 10],
                edgeLabel: {
                    fontSize: 20
                },
                data: [{
                    name: '飞机',
                    x: 100,
                    y: 400
                }, {
                    name: '坦克',
                    x: 300,
                    y: 400
                }, {
                    name: '火炮',
                    x: 500,
                    y: 400
                }, {
                    name: '演习',
                    x: 100,
                    y: 100
                },{
                    name: '交易',
                    x: 300,
                    y: 100
                },{
                    name: '冲突',
                    x: 500,
                    y: 100
                }],
                // links: [],
                links: [{
                    source: '演习',
                    target: '飞机',
                }, {
                    source: '演习',
                    target: '火炮'
                }, {
                    source: '交易',
                    target: '坦克'
                }, {
                    source: '冲突',
                    target: '飞机'
                }],
                lineStyle: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0
                }
            }
        ]
    };

    //Histogram
    posList = [
        'left', 'right', 'top', 'bottom',
        'inside',
        'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
        'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
    ];

    app.configParameters = {
        rotate: {
            min: -90,
            max: 90
        },
        align: {
            options: {
                left: 'left',
                center: 'center',
                right: 'right'
            }
        },
        verticalAlign: {
            options: {
                top: 'top',
                middle: 'middle',
                bottom: 'bottom'
            }
        },
        position: {
            options: posList.reduce(function (map, pos) {
                map[pos] = pos;
                return map;
            }, {})
        },
        distance: {
            min: 0,
            max: 100
        }
    };

    app.config = {
        rotate: 90,
        align: 'left',
        verticalAlign: 'middle',
        position: 'insideBottom',
        distance: 15,
        onChange: function () {
            var labelOption = {
                normal: {
                    rotate: app.config.rotate,
                    align: app.config.align,
                    verticalAlign: app.config.verticalAlign,
                    position: app.config.position,
                    distance: app.config.distance
                }
            };
            myChart.setOption({
                series: [{
                    label: labelOption
                }, {
                    label: labelOption
                }, {
                    label: labelOption
                }, {
                    label: labelOption
                }]
            });
        }
    };


    var labelOption = {
        show: true,
        position: app.config.position,
        distance: app.config.distance,
        align: app.config.align,
        verticalAlign: app.config.verticalAlign,
        rotate: app.config.rotate,
        formatter: '{c}  {name|{a}}',
        fontSize: 16,
        rich: {
            name: {
            }
        }
    };

    Hisoption = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['演习', '交易', '冲突']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: ['2020.01', '2020.02', '2020.03', '2020.04', '2020.05']
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '演习',
                type: 'bar',
                barGap: 0,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390]
            },
            {
                name: '交易',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290]
            },
            {
                name: '冲突',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190]
            }
        ]
    };
    //Pie
    Pieoption && myChartPie.setOption(Pieoption);
    //Dia
    Diaoption && myChartDia.setOption(Diaoption);
    //His
    Hisoption && myChartHis.setOption(Hisoption);
    function Check_box(witch,checkbox){
        var ck_all = document.getElementById('check_all');
        var lb_all = document.getElementById('label_all');
        var ck_pie = document.getElementById('check_pie');
        var ck_dia = document.getElementById('check_dia');
        var ck_his = document.getElementById('check_his');
        var crt_left = document.getElementById('left_chart');
        var crt_pie = document.getElementById('PieChart');
        var crt_dia = document.getElementById('Diagram');
        var crt_his = document.getElementById('Histogram');
        if (witch == 'all') {
            if (checkbox.checked==true) {
                ck_pie.checked=true;
                ck_dia.checked=true;
                ck_his.checked=true;
            }else{
                ck_pie.checked=false;
                ck_dia.checked=false;
                ck_his.checked=false;
                lb_all.innerText="全部勾选";
                crt_left.className = "";
                crt_pie.className = "";
                crt_pie.className = "";
                crt_his.className = "";
            }
        }else if (witch == 'pie') {
            if (ck_pie.checked==true) {
                if (ck_his.checked) {
                    crt_left.className = "div-left-all";
                    crt_his.className = "div-left-all";
                    if (ck_dia.checked) {
                        crt_dia.className = "div-top";
                        crt_pie.className = "div-bottom";
                    }else{
                        crt_pie.className = "div-one";
                    }
                }else{
                    crt_left.className = "div-one";
                    if (ck_dia.checked) {
                        crt_dia.className = "div-left-all";
                        crt_pie.className = "div-left-all";
                    }else{
                        crt_pie.className = "div-one";
                    }
                }
            }else{
                ck_all.checked=false;
                lb_all.innerText="全部勾选";
                if (ck_his.checked) {
                    if (ck_dia.checked) {
                        crt_dia.className = "div-one";
                        crt_pie.className = "div-none";
                    }else{
                        crt_his.className = "div-one";
                        crt_pie.className = "div-none";
                    }
                }else{
                    if (ck_dia.checked) {
                        crt_dia.className = "div-one";
                        crt_pie.className = "div-none";
                    }else{
                        crt_pie.className = "div-none";
                    }
                }
            }
        }else if (witch == 'dia') {
            if (ck_dia.checked==true) {
                if (ck_his.checked) {
                    crt_left.className = "div-left-all";
                    crt_his.className = "div-left-all";
                    if (ck_pie.checked) {
                        crt_pie.className = "div-top";
                        crt_dia.className = "div-bottom";
                    }else{
                        crt_dia.className = "div-one";
                    }
                }else{
                    crt_left.className = "div-one";
                    if (ck_pie.checked) {
                        crt_pie.className = "div-left-all";
                        crt_dia.className = "div-left-all";
                    }else{
                        crt_dia.className = "div-one";
                    }
                }
            }else{
                ck_all.checked=false;
                lb_all.innerText="全部勾选";
                if (ck_his.checked) {
                    if (ck_pie.checked) {
                        crt_pie.className = "div-one";
                        crt_dia.className = "div-none";
                    }else{
                        crt_his.className = "div-one";
                        crt_dia.className = "div-none";
                    }
                }else{
                    if (ck_pie.checked) {
                        crt_pie.className = "div-one";
                        crt_dia.className = "div-none";
                    }else{
                        crt_dia.className = "div-none";
                    }
                }
            }
        }else if (witch == 'his') {
            if (ck_his.checked==true) {
                if (ck_dia.checked || ck_pie.checked) {
                    crt_left.className = "div-left-all";
                    crt_his.className = "div-left-all";
                }else{
                    crt_his.className = "div-one";
                }
            }else{
                ck_all.checked=false;
                lb_all.innerText="全部勾选";
                if (ck_dia.checked || ck_pie.checked) {
                    crt_left.className = "div-one";
                    crt_his.className = "";
                    if (ck_dia.checked && ck_pie.checked) {
                        crt_dia.className = "div-left-all";
                        crt_pie.className = "div-left-all";
                    }else if (ck_dia.checked) {
                        crt_dia.className = "div-one";
                    }else{
                        crt_pie.className = "div-one";
                    }
                }else{
                    crt_his.className = "";
                }
            }
        }else{
            console.log(witch+checkbox);
        }
        if (ck_dia.checked && ck_pie.checked && ck_his.checked) {
            ck_all.checked = true;
            lb_all.innerText="取消勾选";
            crt_left.className = "div-left-all";
            crt_pie.className = "div-top";
            crt_dia.className = "div-bottom";
            crt_his.className = "div-left-all";
        };
        /*if (ck_pie.checked) {
            //Pie
            Pieoption && myChartPie.setOption(Pieoption);
            console.log("111")
        };
        if (ck_dia.checked) {
            //Dia
            Diaoption && myChartDia.setOption(Diaoption);
            console.log("222")
        };
        if (ck_his.checked) {
            //His
            Hisoption && myChartHis.setOption(Hisoption);
            console.log("333")
        };*/
        myChartPie.resize();
        myChartDia.resize();
        myChartHis.resize();
    }
</script>
</body>
</html>