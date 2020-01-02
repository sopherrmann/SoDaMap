const entityMapper = {
    'user_position': {'title': 'User Position', 'dashed': 'user-position'},
    'spatial_bookmark': {'title': 'Spatial Bookmark', 'dashed': 'spatial-bookmark'},
    'map_interaction': {'title': 'Map Interaction', 'dashed': 'map-interaction'},
    'map_search': {'title': 'Map Search', 'dashed': 'map-search'},
    'routing': {'title': 'Routing', 'dashed': 'routing'},
    'question': {'title': 'Question', 'dashed': 'question'},
};

function showMore(mappedSessionId) {
    open();
    document.getElementById('more-info').style.display = "block";

    let title = document.getElementById('more-info-title');
    title.innerHTML = 'Mapped Session ' + mappedSessionId;

    let showMoreHeader = $('#show-more-header');
    if (showMoreHeader.find('.annotation').length === 0) {
        let mappedSessionAnnotation = getAnnotationInput('mapped_session', mappedSessionId);
        showMoreHeader.append(mappedSessionAnnotation);
        addAnnotationButtonClickHandler('mapped_session', mappedSessionId);
    }
    // TODO add click handler!

    let body = document.getElementById('more-info-body');
    body.innerHTML = getShowMoreHtml();
    fillShowMoreElems(mappedSessionId);
}

function getShowMoreHtml() {
    return '<div class="show-more-body">' +
        '<div id="show-more-mapped-session"></div>' +
        '<div id="show-more-user-position"></div>' +
        '<div id="show-more-spatial-bookmark"></div>' +
        '<div id="show-more-map-search"></div>' +
        '<div id="show-more-map-interaction"></div>' +
        '<div id="show-more-question"></div>' +
        '<div id="show-more-routing"></div>' +
        '</div>'
}

function fillShowMoreElems(mappedSessionId) {
    for (let entityType in entityMapper) {
        addEntityFromServer(mappedSessionId, entityType, entityMapper[entityType])
    }
}

function addEntityFromServer(mappedSessionId, entityType, entityDict) {
    console.log('Loading mappedSession ' + mappedSessionId + ' entityType ' + entityType);
    $.ajax({
        url: getMappedSessionUrlWithEntity(mappedSessionId, entityType),
        type: 'GET',
        dataType: 'json',
        success: function (result) {
            console.log('Retrieved mappedSession ' + mappedSessionId + ' ' + entityType + ' from server');
            let htmlParent = $('#' + getShowMoreParentId(entityDict.dashed));
            htmlParent.empty();

            let htmlSingleEntityId = getSingleEntityBodyId(entityType);
            let htmlElemHeader = '<div class="entity-header">' + entityDict.title + '</div>';
            let htmlElem = '<div id="' + htmlSingleEntityId + '" class="entity-body"></div>';
            htmlParent.append(htmlElemHeader + htmlElem);
            let htmlElems = $('#' + htmlSingleEntityId);

            // entity has to be always a list > fix routing
            let entities = result.entity;
            for (let idx in entities) {
                let entity = entities[idx];
                let entityPretty = syntaxHighlight(JSON.stringify(entity, null, "\t"));

                // Annotation
                let htmlAnnotation = getAnnotationInput(entityType, entity.Id);
                let elem = '<div class="single-entity">' + entityPretty + htmlAnnotation + '</div>';
                htmlElems.append(elem);
                addAnnotationButtonClickHandler(entityType, entity.Id)
            }
        }
    });
}

function getShowMoreParentId(entityType) {
    return 'show-more-' + entityType;
}

function getSingleEntityBodyId(entityType) {
    return 'single-entity-' + entityType;
}

function getAnnotationButtonId(entityType, entityId) {
    let entityName = entityType.replace('_', '-');
    return  'annotation-' + entityName + '-button-' + entityId;
}

function getAnnotationContentId(entityType, entityId) {
    let entityName = entityType.replace('_', '-');
    return 'annotation-' + entityName + '-content-' + entityId;
}

function getAnnotationInput(entityType, entityId) {
    let htmlAnnotationButtonId = getAnnotationButtonId(entityType, entityId);
    let htmlAnnotationContentId = getAnnotationContentId(entityType, entityId);

    return '<div class="annotation">' +
        '<span class="annotation-name">Annotation: </span>' +
        '<input type="text" id="' + htmlAnnotationContentId + '"/>' +
        '<input type="button" id="' + htmlAnnotationButtonId + '" value="Add"/>' +
        '</div>';
}

function addAnnotationButtonClickHandler(entityType, entityId) {
    let htmlAnnotationButtonId = getAnnotationButtonId(entityType, entityId);
    $('#' + htmlAnnotationButtonId).click(function () {addAnnotationToServer(entityType, entityId)});
}

function addAnnotationToServer(entityType, entityId) {
    let annotationContentId = getAnnotationContentId(entityType, entityId);
    let annotationText = document.getElementById(annotationContentId).value;

    if (!annotationText) {
        console.log('No Annotation Text set, nothing is added to the Database!');
        return;
    }

    console.log('Adding annotation ' + annotationText + ' ' + entityType  + ' ' + entityId);
    $.ajax({
        url: getAddAnnotationUrl(entityType, entityId),
        type: 'POST',
        data: annotationText,
        contentType: 'application/json',
        success: function () {
            document.getElementById(annotationContentId).value = '';
            console.log('Added annotation ' + annotationText + ' ' + entityType  + ' ' + entityId);
            alert('Annotation added!');
        }
    })
}

// https://stackoverflow.com/questions/4810841/how-can-i-pretty-print-json-using-javascript, 02.01.2020, 12:45
// https://stackoverflow.com/questions/16499804/json-in-html-with-line-breaks, 02.01.2020, 13:00
function syntaxHighlight(result) {
    result = result.replace(/\n/g, "<br>");
    result = result.replace(/[ ]/g, "&nbsp;");
    return result.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        let cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}
