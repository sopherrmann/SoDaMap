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
    const existing_dropdown = $('#existing-dropdown');

    // Loop through all dropdown buttons to toggle between hiding and showing its dropdown content
    if (existing_dropdown.hasClass('invisible')) {
        $.ajax({
            url: mappedSessionUrl,
            type: 'GET',
            success: function(result){
                existing_dropdown.empty();
                const mapped_sessions = result.mapped_sessions;
                for (let idx in mapped_sessions) {
                    const elem = mapped_sessions[idx];

                    const html_elem = $('<a>id: ' + elem['id'] + '</a>');
                    html_elem.click(function () {load_mapped_session(elem['id'])});
                    existing_dropdown.append(html_elem);
                }
                existing_dropdown.removeClass('invisible')
            }});
    } else {
        existing_dropdown.addClass('invisible')
    }
});

// Import XML
// document.querySelector('form').addEventListener('submit', function() {
$('#submitUpload').click(function () {
    console.log('inside upload xml');
    let file = $('#upload-xml-file')[0].files[0];
    file.text().then(upload_to_server);
});

function upload_to_server(xml) {
    console.log(xml);
    $.ajax({
        url: importUrl,
        type: 'POST',
        data: xml,
        contentType: false,
        processData: false,
        success: function (result) {
            console.log('Successfully uploaded file')
        }
    })
}
