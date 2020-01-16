// Static server urls
const xmlServerURL = "http://localhost:5000";

const mappedSessionUrl = xmlServerURL + "/mapped_sessions";
const mappedUrl = mappedSessionUrl + "/mapped";
const webUrl = mappedSessionUrl + "/web";
const importUrl = mappedSessionUrl + "/import";
const newMappedSessionUrl = mappedSessionUrl + "/new";

// Dynamic server urls
function getMappedSessionUrlById(mappedSessionId) {
    return mappedSessionUrl + "/" + mappedSessionId;
}

function getMappedSessionUrlWithEntity(mappedSessionId, entityType) {
    return getMappedSessionUrlById(mappedSessionId) + "/" + entityType;
}

function getMappedSessionXML(mappedSessionId) {
    return getMappedSessionUrlById(mappedSessionId) + "/xml";
}

function getAddAnnotationUrl(entityType, entityId) {
    return xmlServerURL + "/annotation/" + entityType + "/" + entityId;
}

document.body.onload = setWebSessionId;
function setWebSessionId () {
    $.ajax({
        url: newMappedSessionUrl,
        type: 'POST',
        dataType: 'JSON',
        success: function (response) {
            document.getElementById("web-session-id").innerHTML = response.web_session_id;
            console.log('WebSessionId set to ' + response.web_session_id);
        }
    });
}
window.onbeforeunload = setWebSessionEnd;
function setWebSessionEnd() {
    let bodyJson = {
        "end_time": new Date().toISOString(),
    };

    $.ajax({
        url: getMappedSessionUrlById(getWebSessionId()),
        type: 'PATCH',
        contentType: 'application/json',
        processData: false,
        data: JSON.stringify(bodyJson),
        success: function (respone) {
            console.log('WebSession end time added.');
        }
    })
}

function getWebSessionId() {
    return document.getElementById("web-session-id").innerHTML;
}


// Show List of already imported MappedSession Dropdown
$("#exist-mapped-sessions").click(function(){
    const right_container = $('#right-bar-container');
    const right_dropdown = $('#right-dropdown');
    const main = $('.main');

    // Loop through all dropdown buttons to toggle between hiding and showing its dropdown content
    if (right_container.hasClass('invisible')) {
        right_container.removeClass('invisible');
        main.addClass('main-reduce-width');
        right_dropdown.empty();
        setListOfMappedSessions(right_dropdown)
    } else {
        right_container.addClass('invisible');
        main.removeClass('main-reduce-width');
    }
});

function getRightDropDownElemMain(elem) {
    let dropdownElem = $('<div class="right-dropdown-elem"></div>');
    let link = getRightDropdownLink(elem);
    let buttons = getRightDropDownButtons(elem['id']);

    dropdownElem.append(link);
    dropdownElem.append(buttons);
    return dropdownElem;
}

function getRightDropdownLink(elem) {
    let colorBoxId = getColorBoxId(elem['id']);
    let miButtonId = getMiButtonId(elem['id']);
    let html_elem = $( '<a><div>' + elem['id'] +
        '<div class="color-box invisible" id="' + colorBoxId + '"></div>' +
        '<div class="mi-button invisible" id="' + miButtonId + '">MI</div>' +
        '</div>' +
        '<div class="smaller-text"> Type: ' + elem['session_type'] + '</div>' +
        '<div class="smaller-text"> Start: ' + elem['application_start'] + '</div>' +
        '<div class="smaller-text"> End: ' + elem['application_end'] + '</div></a>');
    html_elem.click(function () {loadMappedSessionLayers(elem['id'])});

    return html_elem;
}

function getRightDropDownButtons(mappedSessionId) {
    let show_more_button = $('<span class="show-more-button button">Show More</span>');
    show_more_button.click(function () {showMore(mappedSessionId)});

    let xml_button = $('<span class="xml-button button">Get XML</span>');
    xml_button.click(function () {getXML(mappedSessionId)});

    let button = $('<div class="button-div"></div>');
    button.append(show_more_button);
    button.append(xml_button);
    return button;
}

// https://stackoverflow.com/questions/19327749/javascript-blob-filename-without-link, 16.01.2020, 19:00
var saveData = (function () {
    let a = document.createElement("a");
    document.body.appendChild(a);
    a.style = "display: none";
    return function (result, fileName) {
        let xml = result.children[0].outerHTML,
            blob = new Blob([xml], {type: "text/xml"}),
            url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    };
}());

function getXML(mappedSessionId) {
    console.log('Loading XML');
    $.ajax({
        url: getMappedSessionXML(mappedSessionId),
        type: 'GET',
        dataType: 'xml',
        success: function (result) {
            console.log('Retrieved XML ' +  mappedSessionId + ' from server');
            saveData(result, 'mapped_session_' + mappedSessionId + '.xml')
        },
        error: function (result) {
            alert('The requested Mapped- or WebSession cannot be downloaded! Maybe required entities are missing')
        }
    });
}

function setListOfMappedSessions(dropdown) {
    $.ajax({
        url: mappedSessionUrl,
        type: 'GET',
        success: function(result){
            const mapped_sessions = result.mapped_sessions;
            for (let idx in mapped_sessions) {
                const elem = mapped_sessions[idx];
                const html_elem = getRightDropDownElemMain(elem);
                dropdown.append(html_elem);
            }
        }
    })
}

// Import XML
$('#submitUpload').click(function () {
    console.log('inside upload xml');
    let file = $('#upload-xml-file')[0].files[0];
    $.ajax({
        url: importUrl,
        type: 'POST',
        data: file,
        contentType: false,
        processData: false,
        success: function () {
            console.log('Successfully uploaded file')
        }
    })
});

function getColorBoxId(mappedSessionId) {
    return 'color_box_' + mappedSessionId;
}

function getMiButtonId(mappedSessionId) {
    return 'mi_button_' + mappedSessionId
}
