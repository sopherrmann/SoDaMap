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

// Add tracking functionality
// set start variables
global_center = [null , null];
bb_start = map.getBounds();
bb_search = null;
zoomed = false;
click = false;
startDate = new Date().toISOString();
zoomDateOld = startDate;
currentDate = null;

// geocoder all search results
geocoder.on('results', function(T) {
    searchText = T.query["0"];
    allSugest = T.features;
});

// geocoder search result clicked
geocoder.on('result', function(T) {
    currentDate = new Date().toISOString();
    global_center = T.result.center;
    bb_search = map.getBounds();
    global_result = T;
    let endSearchTime = new Date().toISOString();

    add_user_pos_event(currentDate);
    add_map_search_event(global_result, searchText, allSugest, bb_search, startSearchTime, endSearchTime)
});

directions.on('route', function (T) {
    let steps = T.route["0"].legs["0"].steps;
    startPoint = (steps["0"].name);
    endPoint = (steps[steps.length - 1].name)
});


// map click interaction
map.on('click', function (T) {
    let clickDate = new Date().toISOString();
    click = true;
    let pos = T.lngLat;
    if (bb_search === null && zoomed === false) {
        let click_event = add_map_interaction_click_event(currentDate, pos, click, bb_start, startDate, clickDate)
    }else if(bb_search === null) {
        let click_event = add_map_interaction_click_event(currentDate, pos, click, bb_start, zoomDate, clickDate)
    }else {
        let click_event = add_map_interaction_click_event(currentDate, pos, click, bb_search, zoomDate, clickDate)
    }
    click = false
});

// map zoom interaction
map.on('zoomstart', function() {
    level_old = map.getZoom();
    let bb = map.getBounds();
    ymin_old = bb.getSouth();
    ymax_old = bb.getNorth();
    xmin_old = bb.getWest();
    xmax_old = bb.getEast();
});
map.on('zoomend', function() {
    level_new = map.getZoom();
    let bb = map.getBounds();
    ymin_new = bb.getSouth();
    ymax_new = bb.getNorth();
    xmin_new = bb.getWest();
    xmax_new = bb.getEast();
    zoomDate = new Date().toISOString();
    zoomed = true;
    let zoom_event = add_map_interaction_zoom_event(zoomDate, zoomDateOld, zoomed);
    zoomed = false;
    zoomDateOld = zoomDate;
});

function add_user_pos_event(currentDate) {
    let add_user_pos_event_string = '{\n\t"time_stamp": ' + currentDate + ',\n' +
        '\t"geom": {\n' +
        '\t\t"x": ' + global_center['0'] + '\n' +
        '\t\t"y": ' + global_center['1'] + '\n' +
        '\t}\n'+
        '}';
    console.log('User position' + add_user_pos_event_string);
    return(add_user_pos_event_string)
}

function add_map_interaction_click_event(currentDate, pos, click, bb, Date, clickDate) {
    let ymin_new = bb.getSouth();
    let ymax_new = bb.getNorth();
    let xmin_new = bb.getWest();
    let xmax_new = bb.getEast();
    let add_map_interaction_click_string = '{ \n \t"time_stamp": ' + currentDate + ',\n' +
        '\t"geom": {\n' +
        '\t\t"x": ' + global_center['0'] + '\n' +
        '\t\t"y": ' + global_center['1'] + '\n' +
        '\t},\n' +
        '\t"is_click_interaction":' + click + ',\n' +
        '\t"new_bbox_time_stamp_lr":' + Date + ',\n' +
        '\t"new_bbox_time_stamp_ul":' + Date + '\n' +
        '\t"new_bbox_geom": { \n' +
        '\t\t"xmin": ' + xmin_new + ',\n' +
        '\t\t"xmax": ' + xmax_new + ',\n' +
        '\t\t"ymin": ' + ymin_new + ',\n' +
        '\t\t"ymax": ' + ymax_new + ',\n' +
        '\t},\n' +
        '\t"where_clicked_geom": {\n' +
        '\t\t"x": ' + pos.lng + '\n' +
        '\t\t"y": ' + pos.lat + '\n' +
        '\t},\n' +
        '\t"where_clicked_time_stamp":' + clickDate + '\n' +
        '}';
    console.log('Map interaction click' + add_map_interaction_click_string);
    return(add_map_interaction_click_string);
}

function add_map_interaction_zoom_event(zoomDate, zoomDateOld, zoomed) {
    let add_map_interaction_zoom_event_string = '{ \n \t"time_stamp": ' + currentDate + ',\n' +
        '\t"geom": {\n' +
        '\t\t"x": ' + global_center['0'] + '\n' +
        '\t\t"y": ' + global_center['1'] + '\n' +
        '\t},\n' +
        '\t"is_zoom_in_interaction":' + zoomed + ',\n\n' +
        '\t"old_zoom_level":' + level_old + ',\n' +
        '\t"old_bbox_time_stamp_lr":' + zoomDateOld + ',\n' +
        '\t"old_bbox_time_stamp_ul":' + zoomDateOld + '\n' +
        '\t"old_bbox_geom": { \n' +
        '\t\t"xmin": ' + xmin_old + ',\n' +
        '\t\t"xmax": ' + xmax_old + ',\n' +
        '\t\t"ymin": ' + ymin_old + ',\n' +
        '\t\t"ymax": ' + ymax_old + ',\n' +
        '\t},\n' +
        '\t"new_zoom_level":' + level_new + ',\n' +
        '\t"new_bbox_time_stamp_lr":' + zoomDate + ',\n' +
        '\t"new_bbox_time_stamp_ul":' + zoomDate + '\n' +
        '\t"new_bbox_geom": { \n' +
        '\t\t"xmin": ' + xmin_new + ',\n' +
        '\t\t"xmax": ' + xmax_new + ',\n' +
        '\t\t"ymin": ' + ymin_new + ',\n' +
        '\t\t"ymax": ' + ymax_new + ',\n' +
        '\t}\n' +
        '}';
    console.log('Zoom ' + add_map_interaction_zoom_event_string);
    return(add_map_interaction_zoom_event_string);
}

function add_map_search_event(T, searchText, allSugest, bb, startSearchTime, endSearchTime) {
    let ymin = bb.getSouth();
    let ymax = bb.getNorth();
    let xmin = bb.getWest();
    let xmax = bb.getEast();
    for( let i = allSugest.length-1; i--;){
        if ( allSugest[i].text === T.result.text) allSugest.splice(i, 1);
    }
    let add_map_search_event_string =  '{ \n \t"starttime_stamp": ' + startSearchTime + ',\n' +
        '\t"endtime_stamp": ' + endSearchTime + ',\n' +
        '\t"bbox_time_stamp_lr": ' + startSearchTime + ',\n' +
        '\t"bbox_time_stamp_ul": ' + endSearchTime + '\n' +
        '\t"bbox_geom": { \n' +
        '\t\t"xmin": ' + xmin + ',\n' +
        '\t\t"xmax": ' + xmax + ',\n' +
        '\t\t"ymin": ' + ymin + ',\n' +
        '\t\t"ymax": ' + ymax + ',\n' +
        '\t},\n' +
        '\t"text_with_suggestions": [\n' +
        '\t\t{\n' +
        '\t\t\t"text_typed":' + searchText + ',\n' +
        '\t\t\t"suggestion_chosen":' + T.result.text + ',\n' +
        '\t\t\t"suggestions": [\n' +
        '\t\t\t\t{"suggestion":' + T.result.text + '},\n' +
        '\t\t\t\t{"suggestion":' + allSugest[Math.floor(Math.random() * allSugest.length)].text + '},\n' +
        '\t\t\t]' + '\t\t}, {\n' +
        '\t\t\t"text_typed":' + searchText +
        '\t\t}\n]\n}';
    console.log('Map search' + add_map_search_event_string)
}

// Todo: Some information cannot be retrieved
function add_routing_event() {
    let add_routing_event_string = '{ \n \t"start_routing_interface_time_stamp": ' + startRoutingTime + ',\n' +
        '\t"end_routing_interface_send_request_or_interface_closed_time_sta": ' + endRoutingTime + ',\n' +
        '\t"origin_text_box_history": {\n' +
        '\t\t"text_with_suggestion": [\n' +
        '\t\t\t{\n' +
        '\t\t\t\t"text_typed": ' + '???' +',\n' +
        '\t\t\t\t"suggestion_chosen": ' + startPoint +',\n' +
        '\t\t\t\t"suggestions": [\n' +
        '\t\t\t\t\t{"suggestion": ' +  + '},\n' +
        '\t\t\t\t\t{"suggestion": ' +  + '},\n' +
        '\t\t\t\t]\n' +
        '\t\t\t}, {\n' +
        '\t\t\t\t"text_typed": ' + '???' + ',\n' +
        '\t\t\t\t"suggestion_chosen": ' +  + ',\n' +
        '\t\t\t\t"suggestions": [\n' +
        '\t\t\t\t\t{"suggestion": ' +  + '},\n' +
        '\t\t\t\t\t{"suggestion": ' +  + '},\n' +
        '\t\t\t\t]\n' +
        '\t\t\t}\n' +
        '\t\t]\n' +
        '\t},\n' +
        '\t"destination_text_box_history": {\n' +
        '\t\t"text_with_suggestion":\n' +
        '\t\t[\n' +
        '\t\t\t{' +
        '\t\t\t\t"text_typed": ' + '???' +',\n' +
        '\t\t\t\t"suggestion_chosen": ' + endPoint +',\n' +
        '\t\t\t}\n' +
        '\t\t]\n' +
        '\t}\n' +
        '}'
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

function showVal(newVal){
    document.getElementById("rangeOut").value = newVal;
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
startRoutingTime = new Date().toISOString();
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
        endRoutingTime = new Date().toISOString();
        add_routing_event();
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
document.getElementsByClassName("close")[4].addEventListener('click', close);
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
    uploadQuest.style.display = "none";
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
