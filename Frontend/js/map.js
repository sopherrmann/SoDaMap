mapboxgl.accessToken = 'pk.eyJ1IjoiZGFuaWJlaSIsImEiOiJjand1b2VzaDIxOWI2NGJwNXBmZDE1aGg3In0.FveFwontuW06ciBJV-FZng';
let map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
    center: [16.363449, 48.210033], // starting position [lng, lat]
    zoom: 9 // starting zoom
});
let nav = new mapboxgl.NavigationControl();
map.addControl(nav, 'bottom-right');

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
let geocoder = new MapboxGeocoder({
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
    placeholder: 'Search',
});

// Functions for the modals with the questionnaire
function validateForm() {
    // This function deals with validation of the form fields
    let x, i, valid = true;
    x = document.getElementsByClassName("inputBody")[0].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < x.length; i++) {
        // If a field is empty...
        if (x[i].value === "") {
            // add an "invalid" class to the field:
            x[i].className += " invalid";
            // and set the current valid status to false:
            valid = false;
        }
    }
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
const directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken
});
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
        map.removeControl(directions)
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

//* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content
// This allows the user to have multiple dropdowns without any conflict */
const dropdown = document.getElementsByClassName("dropdown-btn");
let i;
for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        let dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
            document.getElementById("exist").style.backgroundColor = "";
            document.getElementById("exist").style.color = "";
        } else {
            dropdownContent.style.display = "block";
            document.getElementById("exist").style.backgroundColor = "cornflowerblue";
            document.getElementById("exist").style.color = "white";
        }
    });
}

// Add information to the uploaded XML-files
const add_info = document.getElementById("myAppInfo");
document.getElementById("addInfo").addEventListener('click', addInfo);
function addInfo() {
    open();
    add_info.style.display = "block";
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
    add_info.style.display = "none";
    startinfo.style.display = "none";
    uploadQuest.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target===upload || event.target===diary_study || event.target===add_info || event.target===startinfo || event.target===uploadQuest) {
        close()
    }
};

// Add modal for personal infos
const startinfo = document.getElementById("personalInfo");
window.addEventListener('load', start);
function start() {
    startinfo.style.display = "block";
}

// Add request, to fill out diary study -> Not possible
// Todo: activate if wanted
// window.addEventListener("beforeunload", end);
function end(e) {
    // alert("Please fill out diary study before leaving the page");
    e.preventDefault();
    e.returnValue = '';
}

function get_index_of_first_symbol_layer() {
    const layers = map.getStyle().layers;
    // Find the index of the first symbol layer in the map style
    let firstSymbolId;
    for (let i = 0; i < layers.length; i++) {
        if (layers[i].type === 'symbol') {
            firstSymbolId = layers[i].id;
            break;
        }
    }
    return firstSymbolId
}

/* Todo: if you want multiple pages instead of one for the questionnaire modals
// Make the modals to multiple page insert
let currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form ...
    let x = document.getElementsByClassName("tab1");
    x[n].style.display = "block";
    // ... and fix the Previous/Next buttons:
    if (n === 0) {
        document.getElementsByClassName("prevBtn")[0].style.display = "none";
    } else {
        document.getElementsByClassName("prevBtn")[0].style.display = "inline";
    }
    if (n === (x.length - 1)) {
        document.getElementsByClassName("nextBtn")[0].innerHTML = "Submit";
    } else {
        document.getElementsByClassName("nextBtn")[0].innerHTML = "Next";
    }
    // ... and run a function that displays the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    let x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n === 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form... :
    if (currentTab >= x.length) {
        //...the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps
    let i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class to the current step:
    x[n].className += " active";
}
 */



