mapboxgl.accessToken = 'pk.eyJ1IjoiZGFuaWJlaSIsImEiOiJjand1b2VzaDIxOWI2NGJwNXBmZDE1aGg3In0.FveFwontuW06ciBJV-FZng';
let map = new mapboxgl.Map({
    container: 'map', // container id
    // stylesheet location  https://stackoverflow.com/questions/35248310/add-some-basic-markers-to-a-map-in-mapbox-via-mapbox-gl-js, 30.12.2019 13:30
    // https://github.com/mapbox/mapbox-gl-styles
    style: 'mapbox://styles/mapbox/basic-v8',
    center: [16.363449, 48.210033], // starting position [lng, lat]
    zoom: 9 // starting zoom
});
let nav = new mapboxgl.NavigationControl();
map.addControl(nav, 'bottom-right');

// openrouteservice.org  --> wenn mit open layer

let coordinatesGeocoder = function (query) {
// match anything which looks like a decimal degrees coordinate pair
    let matches = query.match(/^[ ]*(?:Lat: )?(-?\d+\.?\d*)[, ]+(?:Lng: )?(-?\d+\.?\d*)[ ]*$/i);
    if (!matches) {
        return null;
    }
    function coordinateFeature(lng, lat) {
        return {
            center: [lng, lat],
            geometry: {
                type: "Point",
                coordinates: [lng, lat]
            },
            place_name: 'Lat: ' + lat + ' Lng: ' + lng,
            place_type: ['coordinate'],
            properties: {},
            type: 'Feature'
        };
    }
    let coord1 = Number(matches[1]);
    let coord2 = Number(matches[2]);
    let geocodes = [];

    if (coord1 < -90 || coord1 > 90) {
// must be lng, lat
        geocodes.push(coordinateFeature(coord1, coord2));
    }

    if (coord2 < -90 || coord2 > 90) {
// must be lat, lng
        geocodes.push(coordinateFeature(coord2, coord1));
    }

    if (geocodes.length === 0) {
// else could be either lng, lat or lat, lng
        geocodes.push(coordinateFeature(coord1, coord2));
        geocodes.push(coordinateFeature(coord2, coord1));
    }

    return geocodes;
};

const geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken, // Set the access token
    localGeocoder: coordinatesGeocoder,
    // see https://docs.mapbox.com/api/search/#geocoding-response-object for information about the schema of each response feature
    render: function (item) {
        // extract the item's maki icon or use a default
        let maki = item.properties.maki || 'marker';
        return "<div class='geocoder-dropdown-item'><img class='geocoder-dropdown-icon' src='https://unpkg.com/@mapbox/maki@6.1.0/icons/" + maki + "-15.svg'/>" +
            "<span class='geocoder-dropdown-text'>" + item.text + "</span></div>";
    },
    mapboxgl: mapboxgl, // Set the mapbox-gl instance
    placeholder: 'Search for ...'
});

const directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken,
    profile: "mapbox/walking",
    unit: "metric",
    interactive: false
});

// Add tracking functionality - set start variables
// zoom
let zoomDateOld = null;
let zoomLevelOld = null;
let zoomBboxOld = null;

// map search - text with suggestions
let searchText = null;
let allSug = null;

// geocoder all search results
geocoder.on('results', function(T) {
    searchText = T.query["0"];
    allSug = T.features;
});

// geocoder search result clicked
geocoder.on('result', function(T) {
    let bbox = map.getBounds();
    let currentDate = new Date().toISOString();
    let center = T.result.center;

    addUserPosEvent(currentDate, center);
    addMapSearchEvent(T.result.text, searchText, allSug, bbox, startSearchTime, currentDate)
});

// map click interaction
map.on('click', function (T) {
    let clickDate = new Date().toISOString();
    let bbox = map.getBounds();
    let center = map.getCenter();
    let clickPos = T.lngLat;
    addMapInteractionClickEvent(clickDate, clickPos, bbox, clickDate, clickDate, center);
});

// map zoom interaction
map.on('zoomstart', function() {
    zoomDateOld = new Date().toISOString();
    zoomLevelOld = map.getZoom();
    zoomBboxOld = map.getBounds();
});
map.on('zoomend', function() {
    let bboxNew = map.getBounds();
    let center = map.getCenter();
    let levelNew = map.getZoom();
    let zoomDate = new Date().toISOString();
    addMapInteractionZoomEvent(zoomDate, zoomDate, bboxNew, levelNew, zoomDateOld, zoomBboxOld, zoomLevelOld, center);
});

function addUserPosEvent(currentDate, center) {
    console.log('userPosition event');
    let bodyJson = getUserPositionRequestTemplate(currentDate, center);
    uploadLoggingEvent('user_position', bodyJson)
}

function addMapInteractionClickEvent(currentDate, clickPos, bbox, bboxDate, clickDate, center) {
    console.log('Click event');
    let bodyJson = getClickRequestTemplate(currentDate, clickPos, bbox, bboxDate, clickDate, center);
    uploadLoggingEvent('map_interaction', bodyJson)
}

function addMapInteractionZoomEvent(currentDate, zoomDateNew, bboxNew, levelNew, zoomDateOld, bboxOld, levelOld, center) {
    console.log("zoom event");
    let bodyJson = getZoomRequestTemplate(currentDate, zoomDateNew, levelNew, bboxNew, zoomDateOld, levelOld, bboxOld, center);
    uploadLoggingEvent('map_interaction', bodyJson)
}

function addMapSearchEvent(sugChosen, textTyped, allSugest, bb, startSearchTime, endSearchTime) {
    console.log('mapSearch event');
    let bodyJson = getMapSearchRequestTemplate(textTyped, sugChosen, allSugest, bb, startSearchTime, endSearchTime);
    uploadLoggingEvent('map_search', bodyJson)
}

function isChecked(value, i) {
    // Get the output text
    let text = document.getElementsByClassName("onAgree")[i];
    // If the checkbox is checked, display the output text
    if (value === 1){
        text.style.display = "block";
        text.value = "";
    } else {
        text.style.display = "none";
        text.value = "none";
    }
}

// Submit
uploadQuest = document.getElementById("uploadQuest");
document.getElementById("submitUpload").addEventListener('click', submitU);
function submitU() {
    open();
    uploadQuest.style.display = "block"
}

// search button
let value_search = 0;
let startSearchTime = new Date().toISOString();
document.getElementById("search").addEventListener('click', search);
function search() {
    if (value_search === 0 && value_rout === 1) {
        document.getElementById("search").style.backgroundColor = "cornflowerblue";
        document.getElementById("search").style.color = "white";
        value_search = 1;
        map.addControl(geocoder);
        document.getElementById("routing").style.backgroundColor = "";
        document.getElementById("routing").style.color = "";
        value_rout = 0;
        map.removeControl(directions)
    } else if (value_search === 0){
        document.getElementById("search").style.backgroundColor = "cornflowerblue";
        document.getElementById("search").style.color = "white";
        value_search = 1;
        map.addControl(geocoder);
    } else {
        value_search = 0;
        document.getElementById("search").style.backgroundColor = "";
        document.getElementById("search").style.color = "";
        map.removeControl(geocoder)
    }
}

// routing button
let value_rout = 0;
document.getElementById("routing").addEventListener('click', routing);
function routing() {
    if (value_rout === 0 && value_search === 1) {
        document.getElementById("routing").style.backgroundColor = "cornflowerblue";
        document.getElementById("routing").style.color = "white";
        value_rout = 1;
        map.addControl(directions);
        value_search = 0;
        document.getElementById("search").style.backgroundColor = "";
        document.getElementById("search").style.color = "";
        map.removeControl(geocoder)
    } else if (value_rout === 0) {
        document.getElementById("routing").style.backgroundColor = "cornflowerblue";
        document.getElementById("routing").style.color = "white";
        value_rout = 1;
        map.addControl(directions);
    } else {
        value_rout = 0;
        document.getElementById("routing").style.backgroundColor = "";
        document.getElementById("routing").style.color = "";
        map.removeControl(directions);
    }
}

// Upload of one Element into a Server
// Get the modal
const upload = document.getElementById("myInput");
document.getElementById("upload").addEventListener('click', showUploadDialog);
function showUploadDialog() {
    open();
    upload.style.display = "block";
}

// Diary Study Modal
const diary_study = document.getElementById("myDiary");
document.getElementById("diary").addEventListener('click', diary);
function diary() {
    open();
    diary_study.style.display = "block";
}

function open() {
    if (value_rout === 1) {
        document.getElementById("routing").style.backgroundColor = "";
        document.getElementById("routing").style.color = "";
        map.removeControl(directions)
    } else if (value_search === 1) {
        document.getElementById("search").style.backgroundColor = "";
        document.getElementById("search").style.color = "";
        map.removeControl(geocoder)
    }
}

// Add modal for personal infos
const startinfo = document.getElementById("personalInfo");
window.addEventListener('load', start);
function start() {
    startinfo.style.display = "block";
}

const moreInfo = document.getElementById('more-info');

// Close input window
document.getElementsByClassName("close")[0].addEventListener('click', close);
document.getElementsByClassName("close")[1].addEventListener('click', close);
document.getElementsByClassName("close")[2].addEventListener('click', close);
document.getElementsByClassName("close")[3].addEventListener('click', close);
function close(){
    if (value_rout === 1) {
        document.getElementById("routing").style.backgroundColor = "cornflowerblue";
        document.getElementById("routing").style.color = "white";
        map.addControl(directions)
    } else if (value_search === 1) {
        document.getElementById("search").style.backgroundColor = "cornflowerblue";
        document.getElementById("search").style.color = "white";
        map.addControl(geocoder)
    }
    upload.style.display = "none";
    diary_study.style.display = "none";
    startinfo.style.display = "none";
    moreInfo.style.display = "none";

}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target===upload || event.target===diary_study || event.target===moreInfo || event.target===startinfo || event.target===uploadQuest) {
        close()
    }
};

// Add request, to fill out diary study -> Not possible
// Todo: activate if wanted
// window.addEventListener("beforeunload", end);
function end(e) {
    // alert("Please fill out diary study before leaving the page");
    e.preventDefault();
    e.returnValue = '';
}
