<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html style="height: 100%">
<head>
    <meta charset="utf-8">
</head>
<body style="height: 100%; margin: 0">
<div id="container" style="height: 100%"></div>

<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
<script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>

<script type="text/javascript">
    var dom = document.getElementById("container");
    var myChart = echarts.init(dom);
    var app = {};
    var mycategories = ${requestScope.get("categories")};
    var option;
    var mynodes = ${requestScope.get("nodes")};
    var mylink = ${requestScope.get("links")};
    <%--$.ajax({--%>
    <%--    url: "${pageContext.request.contextPath}/Show/Mapbaidu/getdata",--%>
    <%--    type: 'POST',--%>
    <%--    dataType: 'JSON',--%>
    <%--    data: {--%>
    <%--        "catelogid": 1,--%>
    <%--        "weaponSClass":"",--%>
    <%--        "weaponClass":""--%>
    <%--    },--%>
    <%--    success: function (data) {--%>
    <%--        if (data.result === "ok") {--%>
    <%--            mynodes = data.loc_data;--%>
    <%--            geoCoordMap = data.loc_Map;--%>
    <%--            console.log(Mapdata);--%>
    <%--        } else {--%>
    <%--            toastr.error("数据提交失败！");--%>
    <%--        }--%>
    <%--    },--%>
    <%--    error: function () {--%>
    <%--        toastr.error("系统或服务器出错！");--%>
    <%--    }--%>
    <%--});--%>
    // mycategories= [{
    //     "name": "类目0"
    // }];
    // mynodes.push({
    //     "id": "0",
    //     "name": "Myriel",
    //     "symbolSize": 30,
    //     "x": 200,
    //     "y": 50,
    //     "value": 28,
    //     "category": 0
    // });
    // var res = [0,2,4,6,8,10];
    // var myres = [];
    // var sign = 0;
    // for (var j = 1 ; j < 4; j++) {
    //     var i = 0;
    //     for (i = res.length - 1; i > 0; i--) {
    //         sign =sign + 1;
    //         mynodes.push({
    //             "id": sign.toString(),
    //             "name": "Myriel",
    //             "symbolSize": 30,
    //             "x": 150+10*res[i],
    //             "y": 50*j,
    //             "value": 28,
    //             "category": 0
    //         });
    //         myres.push((res[i]+res[i-1])/2);
    //     }
    //     sign =sign + 1;
    //     mynodes.push({
    //         "id": sign.toString(),
    //         "name": "Myriel",
    //         "symbolSize": 30,
    //         "x": 150+10*res[i],
    //         "y": 50*j,
    //         "value": 28,
    //         "category": 0
    //     });
    //     res = myres;
    // }
    // console.log(mynodes);
    /*mylink = mynodes.forEach(function (node) {
        return {
        "source": node.id,
        "target": node.id
        }
    });*/
    /*graph.nodes.forEach(function (node) {
        node.label = {
            show: node.symbolSize > 30
        };
    });*/
    option = {
        title: {
            text: '武器分类展示',
            top: '5%',
            left: 'center'
        },
        tooltip: {},
        legend: [{
            // selectedMode: 'single',
            data: mycategories.map(function (a) {
                return a.name;
            }),
            orient: 'vertical',
            top: '40%',
            left: '5%'
        }],
        animationDuration: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
            {
                name: '武器',
                type: 'graph',
                layout: 'none',
                top:'10%',
                data: mynodes,
                links: mylink,
                categories: mycategories,
                roam: true,
                label: {
                    position: 'right',
                    formatter: '{b}'
                },
                lineStyle: {
                    color: 'source',
                    curveness: 0
                },
                emphasis: {
                    focus: 'adjacency',
                    lineStyle: {
                        width: 3
                    }
                }
            }
        ]
    };
    option&&myChart.setOption(option);
</script>
</body>
</html>
