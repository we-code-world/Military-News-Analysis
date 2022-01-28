<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta property="og:description" content="COVID-19 3D Visualization." />
    <meta
            name="monetization"
            content="$coil.xrptipbot.com/701298d5-481d-40ff-9945-336671ab2c42"
    />
    <link
            href="https://fonts.googleapis.com/css?family=Space+Mono:400,700&display=swap"
            rel="stylesheet"
    />
    <meta property="og:image" content="https://i.imgur.com/1AFEXhs.png" />
    <title>军事事件统计 3D</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/3dmap_time/main.css" />
</head>
<body>
<div id="globeViz"></div>
<div class="top-info-container">
    <div class="title">军事事件统计</div>
    <div class="title-desc">
        加载国家或地区数据
    </div>
</div>

<div class="bottom-info-container">
    <div style="display: flex; justify-content: center;">
        <div class="timeline-container">
            <button disabled style="margin-right: 10px;" class="play-button">
                播放
            </button>
            <input
                    class="slider"
                    disabled
                    type="range"
                    min="0"
                    max="1"
                    step="1"
            />
            <span
                    style="font-size: 14px; color: #ccd6f6;"
                    class="slider-date"
            ></span>
        </div>
    </div>
    <div style="font-size: 14px; color: #ccd6f6; margin-top: 35px;">
        总计<span class="updated"></span>
    </div>
    <div style="color: #e6f1ff; padding: 0 5px;">
        军事事件数：<span id="infected">0</span>涉及武器数:
        <span id="deaths">0</span>
    </div>
</div>
<script type="text/javascript" src="${pageContext.request.contextPath}/js/3dmap_time/globe.gl.min.js"></script>
<script type="text/javascript" src="${pageContext.request.contextPath}/js/3dmap_time/d3.v5.js"></script>
<script type="text/javascript">
      const globeContainer = document.getElementById('globeViz');

      const colorScale = d3.scaleSequentialPow(d3.interpolateYlOrRd).exponent(1 / 4);
      const GLOBE_IMAGE_URL =
              '${pageContext.request.contextPath}/img/background/earth-night.jpg';
      const BACKGROUND_IMAGE_URL =
              '${pageContext.request.contextPath}/img/background/night-sky.png';
      const GEOJSON_URL =//'https://www.jasondavies.com/maps/world-110m.json'
              '${pageContext.request.contextPath}/geojson/countries.geojson';
      const GEOJSON_URL2 =
              '${pageContext.request.contextPath}/geojson/tiny_countries.geojson';
      const CASES_API =
              '${pageContext.request.contextPath}/json/3dmap_data.json';
      const getVal = (feat) => {
        return feat.covidData.confirmed / feat.properties.POP_EST;
      };
      const flagEndpoint = 'https://corona.lmao.ninja/assets/img/flags';
</script>
<script type="text/javascript" src="${pageContext.request.contextPath}/js/3dmap_time/app.js"></script>
</body>
</html>
