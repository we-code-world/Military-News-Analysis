<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>二维地图</title>
    <link rel="icon" href="${pageContext.request.contextPath}/icons/favicon.ico">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/toastr.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
    <!-- 引入 echarts.js -->
    <script src="${pageContext.request.contextPath}/js/echarts.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/jquery/jquery.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/myjs/myaction.js"></script>
    <script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
</head>
<body class="scroller scroller-1">
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="ChinaMap" style="width: 1000px;height:500px;"></div>
    <a id="analysis" href="${pageContext.request.contextPath}/Show/Map2d" hidden ></a>
    <script type="text/javascript">
        var loc;
        // function randomData() {
        //     return Math.round(Math.random()*500);
        // }
        // var mydata = [
        //     {name: '北京',value: '100' },{name: '天津',value: randomData() },
        //     {name: '上海',value: randomData() },{name: '重庆',value: randomData() },
        //     {name: '河北',value: randomData() },{name: '河南',value: randomData() },
        //     {name: '云南',value: randomData() },{name: '辽宁',value: randomData() },
        //     {name: '黑龙江',value: randomData() },{name: '湖南',value: randomData() },
        //     {name: '安徽',value: randomData() },{name: '山东',value: randomData() },
        //     {name: '新疆',value: randomData() },{name: '江苏',value: randomData() },
        //     {name: '浙江',value: randomData() },{name: '江西',value: randomData() },
        //     {name: '湖北',value: randomData() },{name: '广西',value: randomData() },
        //     {name: '甘肃',value: randomData() },{name: '山西',value: randomData() },
        //     {name: '内蒙古',value: randomData() },{name: '陕西',value: randomData() },
        //     {name: '吉林',value: randomData() },{name: '福建',value: randomData() },
        //     {name: '贵州',value: randomData() },{name: '广东',value: randomData() },
        //     {name: '青海',value: randomData() },{name: '西藏',value: randomData() },
        //     {name: '四川',value: randomData() },{name: '宁夏',value: randomData() },
        //     {name: '海南',value: randomData() },{name: '台湾',value: randomData() },
        //     {name: '香港',value: randomData() },{name: '澳门',value: randomData() }
        // ];
        var mydata = ${requestScope.get('mapdata')};
        var background_color = '#FFFFFF';
        var title_text = '事件数据热力图';
        var title_x = 'center';
        var tooltip_trigger = 'item';
        var visual_map_split_list = [];
        var visual_map_color = ['#5475f5', '#9feaa5', '#85daef','#74e2ca', '#e6ac53', '#eee'];
        var optionMap;
        //初始化echarts实例
        var myChart = echarts.init(document.getElementById('ChinaMap'));
        //https://geo.datav.aliyun.com/areas_v2/bound/100000_full.json
        $.get("${pageContext.request.contextPath}/json/world/geojson/${requestScope.get('location_file')}.json", function (mapJson) {
            var maxValue = ${requestScope.get("maxValue")};
            for (var i=0;i<6;i++){
                visual_map_split_list.push({start: i*maxValue/6.0, end: (i+1)*maxValue/6.0});
            }
            myChart.hideLoading();
            echarts.registerMap('Map', mapJson);
            optionMap = {
                backgroundColor: background_color,
                title: {
                    text: title_text,
                    x: title_x
                },
                tooltip : {
                    trigger: tooltip_trigger
                },
                //左侧小导航图标
                visualMap: {
                    show : true,
                    x: '10%',
                    y: 'center',
                    splitList: visual_map_split_list,
                    color: visual_map_color
                },

                //配置属性
                series: [{
                    name: '数据',
                    type: 'map',
                    map: 'Map',
                    roam: true,
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    data:mydata  //数据
                }]
            };
            //使用制定的配置项和数据显示图表
            myChart.setOption(optionMap);
        });

        //使用制定的配置项和数据显示图表
        optionMap&&myChart.setOption(optionMap);
        // 处理点击事件并且跳转到相应的百度搜索页面
        myChart.on('click', function (params) {
            toastr.options = {
                "closeButton": false, //是否显示关闭按钮
                "debug": false, //是否使用debug模式
                "positionClass": "toast-center-center",//弹出窗的位置
                "showDuration": "300",//显示的动画时间
                "hideDuration": "1000",//消失的动画时间
                "timeOut": "5000", //展现时间
                "extendedTimeOut": "1000",//加长展示时间
                "showEasing": "swing",//显示时的动画缓冲方式
                "hideEasing": "linear",//消失时的动画缓冲方式
                "showMethod": "fadeIn",//显示时的动画方式
                "hideMethod": "fadeOut" //消失时的动画方式
            };
            console.log(params.name);
            //params.color = "#eeeeee";
            loc = "${requestScope.get('location')}";
            console.log(loc);
            if ( loc == "world" || loc == "" ){
                setCookie("location_map",encodeURIComponent(params.name),10);
                console.log(getCookie("location_map"));
                document.getElementById('analysis').click();
            }else {
                toastr.warning("没有更详细的地点信息了，更详细的信息请查看百度地图！");
                myChart.resize();
            }
            //window.open('${pageContext.request.contextPath}/Show/analysis?locations=' + encodeURIComponent(params.name));
        });
    </script>
</body>
</html>