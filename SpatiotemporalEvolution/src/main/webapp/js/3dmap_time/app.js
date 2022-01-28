/*import Globe from "globe.gl";
import { request, getCoordinates, numberWithCommas, formatDate } from 'utils/index';
console.log("request, getCoordinates, numberWithCommas, formatDate");
import {
  GLOBE_IMAGE_URL,
  BACKGROUND_IMAGE_URL,
  GEOJSON_URL,
  // GEOJSON_URL2,
  CASES_API,
} from 'constants.js';
import * as d3 from 'd3.min';*/

// Globe container

async function request(url) {
  try {
    const res = await fetch(url);
    const data = await res.json();
    return data;
  } catch (e) {
    throw e;
  }
}
async function getCoordinates(number_i) {
  try {
    /*const { latitude, longitude } = await request(
      'https://geolocation-db.com/json/'
    );*/
    const latitude=37.550339;
    const longitude = number_i;
    return {
      latitude,
      longitude
    };
  } catch (e) {
    throw e;
  }
}
function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }

function formatDate(date, format = 'MMMM D, YYYY') {
  return date;//dayjs(date).format(format);
}

let world;
let flagName;
let mynumber_i=104.114129;
init();
async function updatePointOfView() {
  // Get coordinates
  try {
    if (mynumber_i>177 || (mynumber_i>-3 && mynumber_i<0)) {
      mynumber_i = -mynumber_i;
    }else
      mynumber_i=mynumber_i+3;
    const { latitude, longitude } = await getCoordinates(mynumber_i);

    world.pointOfView(
      {
        lat: latitude,
        lng: longitude
      },
      1000
    );
  } catch (e) {
    console.log('Unable to set point of view.');
  }
}
function init() {
  world = Globe()(globeContainer)
    .globeImageUrl(GLOBE_IMAGE_URL)
    .backgroundImageUrl(BACKGROUND_IMAGE_URL)
    .showGraticules(false)
    .polygonAltitude(0.06)
    .polygonCapColor((feat) => colorScale(getVal(feat)))
    .polygonSideColor(() => 'rgba(0, 100, 0, 0.05)')
    .polygonStrokeColor(() => '#111')
    .polygonLabel(({ properties: d, covidData: c }) => {
      if (d.ADMIN === 'France') {
        flagName = 'fr';
      } else if (d.ADMIN === 'Norway') {
        flagName = 'no';
      } else {
        flagName = d.ISO_A2.toLowerCase();
      }

      return `
        <div class="card">
          <img class="card-img" src="${flagEndpoint}/${flagName}.png" alt="flag" />
          <div class="container">
             <span class="card-title"><b>${d.NAME}</b></span> <br />
             <div class="card-spacer"></div>
             <hr />
             <div class="card-spacer"></div>
             <span>军事事件数: ${numberWithCommas(c.confirmed)}</span>  <br />
             <span>涉及武器数: ${numberWithCommas(c.deaths)}</span> <br />
          </div>
        </div>
      `;
    })
    .onPolygonHover((hoverD) =>
      world
        .polygonAltitude((d) => (d === hoverD ? 0.12 : 0.06))
        .polygonCapColor((d) =>
          d === hoverD ? 'steelblue' : colorScale(getVal(d))
        )
    )
    .polygonsTransitionDuration(200);

  getCases();
}

let dates = [];
let countries = [];
let featureCollection = [];
let featureCollection2 = [];

// Play button
const playButton = document.querySelector('.play-button');
// Slider
const slider = document.querySelector('.slider');
// Slider date
const sliderDate = document.querySelector('.slider-date');

function polygonFromCenter(center, radius=0.5, num=10) {
  let coords = [];
  for (let i = 0; i < num; i++) {
    const dx = radius*Math.cos(2*Math.PI*i/num);
    const dy = radius*Math.sin(2*Math.PI*i/num);
    coords.push([center[0] + dx, center[1] + dy]);
  }
  return [coords];
}

async function getCases() {
  countries = await request(CASES_API);
  featureCollection = (await request(GEOJSON_URL)).features;

  // featureCollection2 = (await request(GEOJSON_URL2)).features.map(d => {
  //   d.geometry.type = "Polygon";
  //   d.geometry.coordinates = polygonFromCenter(d.geometry.coordinates);
  //   return d;
  // });
  // featureCollection = featureCollection.concat(featureCollection2);

  // world.polygonsData(countriesWithCovid);
  document.querySelector('.title-desc').innerHTML =
    '将鼠标置于对应地区上，可查看累计军事事件数和涉及武器数';

  dates = Object.keys(countries.China);

  // Set slider values
  slider.max = dates.length - 1;
  slider.value = dates.length - 1;

  slider.disabled = false;
  playButton.disabled = false;

  updateCounters();
  updatePolygonsData();

  await updatePointOfView();
}

const infectedEl = document.querySelector('#infected');
const deathsEl = document.querySelector('#deaths');
// const recoveriesEl = document.querySelector('#recovered');
const updatedEl = document.querySelector('.updated');

function updateCounters() {
  sliderDate.innerHTML = dates[slider.value];

  let totalConfirmed = 0;
  let totalDeaths = 0;
  let totalRecoveries = 0;

  Object.keys(countries).forEach((item) => {
    if (countries[item][dates[slider.value]]) {
      const countryDate = countries[item][dates[slider.value]];
      totalConfirmed += +countryDate.confirmed;
      totalDeaths += +countryDate.deaths;
      totalRecoveries += countryDate.recoveries ? +countryDate.recoveries : 0;
    }
  });

  infectedEl.innerHTML = numberWithCommas(totalConfirmed);
  deathsEl.innerHTML = numberWithCommas(totalDeaths);

  updatedEl.innerHTML = `(截止 ${formatDate(dates[slider.value])})`;
}

function updatePolygonsData() {
  for (let x = 0; x < featureCollection.length; x++) {
    const country = featureCollection[x].properties.NAME;
    if (countries[country]) {
      featureCollection[x].covidData = {
        confirmed: countries[country][dates[slider.value]].confirmed,
        deaths: countries[country][dates[slider.value]].deaths,
        recoveries: countries[country][dates[slider.value]].recoveries,
      };
    } else {
      featureCollection[x].covidData = {
        confirmed: 0,
        deaths: 0,
        recoveries: 0,
      };
    }
  }

  const maxVal = Math.max(...featureCollection.map(getVal));
  colorScale.domain([0, maxVal]);
  world.polygonsData(featureCollection);
}

let interval;

playButton.addEventListener('click', () => {
  if (playButton.innerText === '播放') {
    playButton.innerText = '停止';
  } else {
    playButton.innerText = '播放';
    clearInterval(interval);
    return;
  }

  // Check if slider position is max
  if (+slider.value === dates.length - 1) {
    slider.value = 0;
  }

  sliderDate.innerHTML = dates[slider.value];

  interval = setInterval(() => {
    slider.value++;
    sliderDate.innerHTML = dates[slider.value];
    updateCounters();
    updatePolygonsData();
    updatePointOfView();
    if (+slider.value === dates.length - 1) {
      playButton.innerHTML = '播放';
      clearInterval(interval);
    }
  }, 200);
});

if ('oninput' in slider) {
  slider.addEventListener(
    'input',
    function () {
      updateCounters();
      updatePolygonsData();
    },
    false
  );
}

// Responsive globe
window.addEventListener('resize', (event) => {
  world.width([event.target.innerWidth]);
  world.height([event.target.innerHeight]);
});
