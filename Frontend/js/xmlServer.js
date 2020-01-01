// Static server urls
const xmlServerURL = "http://0.0.0.0:5000";

const mappedSessionUrl = xmlServerURL + "/mapped_sessions";
const mappedUrl = mappedSessionUrl + "/mapped";
const webUrl = mappedSessionUrl + "/web";
const importUrl = mappedSessionUrl + "/import";
const newMappedSessionUrl = mappedSessionUrl + "/new";
const mappedSessionEntitiesUrl = mappedSessionUrl + "/entity_types";

const annotationUrl = xmlServerURL + "annotation";
const annotationEntitiesURL = annotationUrl + "/entity_types";

// Dynamic server urls
function get_mapped_session_url_by_id(mapped_session_id) {
    return mappedSessionUrl + "/" + mapped_session_id
}

function get_mapped_session_url_add_entity(mapped_session_id, entity_type) {
    return mappedSessionUrl + "/" + mapped_session_id + "/" + entity_type
}

function get_add_annotation_url(entity_type, entity_id) {
    return xmlServerURL + "/annotation/" + entity_type + "/" + entity_id;
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
    let rgbId = getRightBarId(elem['id']);
    let html_elem = $( '<a><div>' + elem['id'] +
        '<div class="color-box invisible" id="' + rgbId + '"></div></div>' +
        '<div class="smaller-text"> Start: ' + elem['application_start'] + '</div>' +
        '<div class="smaller-text"> End: ' + elem['application_end'] + '</div></a>');
    html_elem.click(function () {loadMappedSession(elem['id'])});

    return html_elem;
}

function getRightDropDownButtons(mappedSessionId) {
    let show_more_button = $('<span class="show-more-button button">Show More</span>');
    show_more_button.click(function () {});

    let xml_button = $('<span class="xml-button button">Get XML</span>');
    xml_button.click(getXML());

    let button = $('<div class="button-div"></div>');
    button.append(show_more_button);
    button.append(xml_button);
    return button;
}

function getXML() {
    return 'the xml';
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

function loadMappedSession(mappedSessionId) {
    loadMappedSessionLayers(mappedSessionId);
    loadMappedSessionInfo(mappedSessionId);
}

function getRightBarId(mapped_session_id) {
    return 'right_bar_' + mapped_session_id;
}

function loadMappedSessionInfo(mappedSessionId) {
    console.log('Loading Mapped Session Info');

    let rightBarId = getRightBarId(mappedSessionId);
    const right_html_tag = $('<a id="' + rightBarId + '">' + mappedSessionId + '</a>');
    $('#right-dropdown').append(right_html_tag);
    console.log('Added ' + mappedSessionId + ' to right bar ');
}
