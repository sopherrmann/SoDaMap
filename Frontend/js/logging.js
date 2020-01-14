function uploadLoggingEvent(entityType, bodyJson) {
    console.log('uploading logging event');
    console.log(bodyJson);
    let webSessionId = getWebSessionId();
    $.ajax({
        url: getMappedSessionUrlWithEntity(webSessionId, entityType),
        type: 'POST',
        contentType: 'application/json',
        processData: false,
        data: JSON.stringify(bodyJson),
        success: function (response) {
            console.log('Added log ' + entityType)
        }
    })
}
