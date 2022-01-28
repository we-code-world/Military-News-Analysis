<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<meta charset="utf-8">
<title>谷歌地图</title>
<style>
    @import url(${pageContext.request.contextPath}/css/Globaldmaps.css);

    #control {
        width: 960px;
        margin: 0 auto;
        text-align: right;
        font-size: small;
        font-style: italic;
        color: #666;
    }
</style>


<h1>Animated World Zoom</h1>
<div id="map"></div>
<div id="control"><label for="north-up"><input type="checkbox" checked id="north-up"> North is up</label></div>

<script src="${pageContext.request.contextPath}/js/3dmapjs/d3.min.js"></script>
<script src="${pageContext.request.contextPath}/js/3dmapjs/topojson.min.js"></script>
<script src="${pageContext.request.contextPath}/js/3dmapjs/app.min.js"></script>