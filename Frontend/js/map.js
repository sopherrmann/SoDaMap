mapboxgl.accessToken = 'pk.eyJ1IjoiZGFuaWJlaSIsImEiOiJjand1b2VzaDIxOWI2NGJwNXBmZDE1aGg3In0.FveFwontuW06ciBJV-FZng';
let map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
    center: [16.363449, 48.210033], // starting position [lng, lat]
    zoom: 9 // starting zoom
});

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
    render: function(item) {
    // extract the item's maki icon or use a default
        var maki = item.properties.maki || 'marker';
        return "<div class='geocoder-dropdown-item'><img class='geocoder-dropdown-icon' src='https://unpkg.com/@mapbox/maki@6.1.0/icons/" + maki + "-15.svg'/>" +
            "<span class='geocoder-dropdown-text'>" + item.text + "</span></div>";
    },
    placeholder: 'Search',
    mapboxgl: mapboxgl, // Set the mapbox-gl instance
});

// search button
let value_search = 0;
document.getElementById("search").addEventListener('click', search);
function search() {
    if (value_search === 0 && value_rout === 1) {
        document.getElementById("search").style.color = "white";
        value_search = 1;
        map.addControl(geocoder);
        document.getElementById("routing").style.color = "";
        value_rout = 0;
        map.removeControl(directions)
    } else if (value_search === 0){
        document.getElementById("search").style.color = "white";
        value_search = 1;
        map.addControl(geocoder);
    } else {
        value_search = 0;
        document.getElementById("search").style.color = "";
        map.removeControl(geocoder)
    }
}

// routing button
let value_rout = 0;
const directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken
});
document.getElementById("routing").addEventListener('click', routing);
function routing() {
    if (value_rout === 0 && value_search === 1) {
        document.getElementById("routing").style.color = "white";
        value_rout = 1;
        map.addControl(directions);
        value_search = 0;
        document.getElementById("search").style.color = "";
        map.removeControl(geocoder)
    } else if (value_rout === 0) {
        document.getElementById("routing").style.color = "white";
        value_rout = 1;
        map.addControl(directions);
    } else {
        value_rout = 0;
        document.getElementById("routing").style.color = "";
        map.removeControl(directions)
    }
}

// Upload of one Element into a Server
// Get the modal
const input = document.getElementById("myInput");
document.getElementById("upload").addEventListener('click', upload);
function upload() {
    if (value_rout === 1) {
        document.getElementById("routing").style.color = "";
        map.removeControl(directions)
    } else if (value_search === 1) {
        document.getElementById("search").style.color = "";
        map.removeControl(geocoder)
    }
    input.style.display = "block";
}
// Close input window
document.getElementsByClassName("close")[0].addEventListener('click', close);
function close(){
    if (value_rout === 1) {
        document.getElementById("routing").style.color = "";
        map.addControl(directions)
    } else if (value_search === 1) {
        document.getElementById("search").style.color = "";
        map.addControl(geocoder)
    }
    input.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === input) {
        close()
    }
};

// Upload to server
const serverURL = "127.0.0.1:5000";
const form = document.querySelector('form');

form.addEventListener('submit', e => {
    e.preventDefault();
    const files = document.querySelector('[type=file]').files;
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        let file = files[i];
        formData.append('files[]', file)
    }
    fetch(serverURL, {
        method: 'POST',
        body: formData,
    }).then(response => {
        console.log(response)
    })
});

// Add information to the uploaded XML-files
document.getElementById("addInfo").addEventListener('click', addInfo);
function addInfo() {
// Todo: open a modal to write information to an uploaded XML-file --> with an open text-field
}

// Add request, to fill out diary study --> this is not possible anymore -.-
window.addEventListener("beforeunload", function (e) {
    const confirmationMessage = "Please fill out diary study before leaving the page";

    (e || window.event).returnValue = confirmationMessage; //Gecko + IE
    return confirmationMessage;                            //Webkit, Safari, Chrome
});