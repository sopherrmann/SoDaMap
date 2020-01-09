const geoServerUrl = "http://localhost:8082/geoserver";
const wfsUrl = geoServerUrl + '/wfs';

const geoserverLayers = {
    // TODO set layer index > currently not possible https://github.com/mapbox/mapbox-gl-js/issues/7016, 03.01.2020, 22:20
    // https://labs.mapbox.com/maki-icons/, 09.01.2020, 10:40
    'map_search': {
        'removeFunc': removeSingleLayer,
        'plotFunc': plotMapSearchSource,
        'additional': {'popupContentFunc': getMapSearchPopup}},
    'spatial_bookmark': {
        'removeFunc': removeLayerWithBackground,
        'plotFunc': plotPointSource,
        'additional': {'iconName': 'star-15', 'popupContentFunc': getSpatialBookmarkPopup}},
    'user_position': {
        'removeFunc': removeLayerWithBackground,
        'plotFunc': plotPointSource,
        'additional': {'iconName': 'marker-15', 'popupContentFunc': getUserPositionPopup}},
};
const mapInteractionLayers = {
    'new_bbox': {
        'plotFunc': plotNewBbox,
        'removeFunc': removeLayerWithBackground,
        'additional': {'popupContentFunc': getMapInteractionPopup},
    },
    'old_bbox': {
        'plotFunc': plotOldBbox,
        'removeFunc': removeLayerWithBackground,
        'additional': {'popupContentFunc': getMapInteractionPopup},
    },
    'where_clicked': {
        'removeFunc': removeLayerWithBackground,
        'plotFunc': plotPointSource,
        'additional': {'iconName': 'circle-11', 'popupContentFunc': getMapInteractionPopup},
    }};

function getLayerRequestData(properties) {
    return '<wfs:GetFeature service="WFS" version="1.0.0"\n' +
        '  outputFormat="JSON"\n' +
        '  xmlns:wfs="http://www.opengis.net/wfs"\n' +
        '  xmlns:ogc="http://www.opengis.net/ogc"\n' +
        '  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
        '  xsi:schemaLocation="http://www.opengis.net/wfs\n' +
        '                      http://schemas.opengis.net/wfs/1.0.0/WFS-basic.xsd">\n' +
        '  <wfs:Query typeName="soda_map:' + properties.layer + '">\n' +
        '    <ogc:Filter>\n' +
        '       <ogc:PropertyIsEqualTo>\n' +
        '          <ogc:PropertyName>mapped_session_id</ogc:PropertyName>\n' +
        '          <ogc:Literal>' + properties.mapped_session_id + '</ogc:Literal>\n' +
        '       </ogc:PropertyIsEqualTo>\n' +
        '    </ogc:Filter>\n' +
        '  </wfs:Query>\n' +
        '</wfs:GetFeature>\n'
}

function loadMappedSessionLayers(mappedSessionId) {
    console.log('Loading mapped session ' + mappedSessionId);

    let colorBoxId = $('#' + getColorBoxId(mappedSessionId));
    let miButtonId = $('#' + getMiButtonId(mappedSessionId));

    let colorArray = getRandomColor();
    // https://stackoverflow.com/questions/8587754/event-managment-replace-click-event, 09.01.2020, 11:00
    miButtonId.unbind();
    miButtonId.click(function (e) {handleMapInteraction(e, mappedSessionId, colorArray)});

    removeMapInteraction(mappedSessionId);
    for (let layerName in geoserverLayers) {
        console.log(layerName);
        let layerDict = geoserverLayers[layerName];

        if (!layerDict.removeFunc(layerName, mappedSessionId)) {
            $.ajax({
                url: wfsUrl,
                type: 'POST',
                dataType: 'json',
                contentType:"application/xml",
                data: getLayerRequestData({
                    'mapped_session_id': mappedSessionId,
                    'layer': layerName,
                }),
                success: function (mapLayer) {
                    let curId = getCurId(layerName, mappedSessionId);
                    console.log('Successfully retrieved layer ' + curId + ' from GeoServer');

                    layerDict.plotFunc(layerName, mappedSessionId, mapLayer, colorArray, layerDict.additional);

                    // Styling
                    colorBoxId.removeClass('invisible');
                    miButtonId.removeClass('invisible');
                    let colorBoxIdDoc = document.getElementById(getColorBoxId(mappedSessionId));
                    colorBoxIdDoc.style.backgroundColor = rgbToHex(colorArray);
                    colorBoxIdDoc.style.borderColor = rgbToHex(colorArray);
                    document.getElementById(getMiButtonId(mappedSessionId)).style.borderColor = rgbToHex(colorArray);
                    console.log('Successfully added layer ' + curId + ' to map');
                }
            });
        } else {
            colorBoxId.addClass('invisible');
            miButtonId.addClass('invisible');
        }
    }
    console.log('Finished layer loading')
}

function getCurId(layerName, mappedSessionId) {
    return layerName + '_ ' +  mappedSessionId;
}

function getSourceId(layerName, mappedSessionId) {
    let curId = getCurId(layerName, mappedSessionId);
    return 'source_' + curId;
}

function getLayerId(layerName, mappedSessionId) {
    let curId = getCurId(layerName, mappedSessionId);
    return 'layer_' + curId;
}

function getLayerBackgroundId(layerName, mappedSessionId) {
    let curId = getCurId(layerName, mappedSessionId);
    return 'layer_background_' + curId;
}

function removeLayerWithBackground(layerName, mappedSessionId) {
    let curId = getCurId(layerName, mappedSessionId);
    let layerId = getLayerId(layerName, mappedSessionId);
    let sourceId = getSourceId(layerName, mappedSessionId);
    let layerIdBackground = getLayerBackgroundId(layerName, mappedSessionId);

    if (map.getLayer(layerId) || map.getSource(sourceId)) {
        if (map.getLayer(layerId)) {
            map.removeLayer(layerId).removeLayer(layerIdBackground);
        }
        if (map.getSource(sourceId)) {
            map.removeSource(sourceId)
        }
        console.log('Removed Layer and source' + curId);
        return true;
    }
    return false;
}

function plotPointSource(layerName, mappedSessionId, mapLayer, colorArray, additional) {
    let layerId = getLayerId(layerName, mappedSessionId);
    let sourceId = getSourceId(layerName, mappedSessionId);
    let layerBackgroundId = getLayerBackgroundId(layerName, mappedSessionId);

    if (map.getSource(sourceId)) {
        return;
    }
    map.addSource(sourceId, {
        'type': 'geojson',
        'data': mapLayer
    });

    // https://github.com/mapbox/mapbox-gl-style-spec/issues/97, 30.12.2019, 14:00
    map.addLayer({
        "id": layerBackgroundId,
        "type": "circle",
        "source": sourceId,
        "paint": {
            'circle-radius': 10,
            'circle-color': buildRgba(colorArray, 1),
        },
    });
    map.addLayer({
        "id": layerId,
        "type": "symbol",
        "source": sourceId,
        "layout": {
            "icon-image": additional['iconName'],
            "icon-allow-overlap": true,
        },
    });
    popupAdderLayerWithBackground(layerId, layerBackgroundId, additional)
}

function removeSingleLayer(layerName, mappedSessionId) {
    let curId = getCurId(layerName, mappedSessionId);
    let layerId = getLayerId(layerName, mappedSessionId);
    let sourceId = getSourceId(layerName, mappedSessionId);

    if (map.getLayer(layerId) || map.getSource(sourceId)) {
        if (map.getLayer(layerId)) {
            map.removeLayer(layerId);
        }
        if (map.getSource(sourceId)) {
            map.removeSource(sourceId)
        }
        console.log('Removed Layer and source' + curId);
        return true;
    }
    return false;
}

function plotMapSearchSource(layerName, mappedSessionId, mapLayer, colorArray, additional) {
    let layerId = getLayerId(layerName, mappedSessionId);
    let sourceId = getSourceId(layerName, mappedSessionId);

    map.addSource(sourceId, {
        'type': 'geojson',
        'data': mapLayer
    });

    // add Layer
    map.addLayer({
        "id": layerId,
        "type": "fill",
        "source": sourceId,
        "paint": {
            'fill-color': buildRgba(colorArray, 0.3),
            'fill-outline-color': buildRgba(colorArray, 1),
        }
    });

    popupAdderSingleLayer(layerId, additional)
}

function handleMapInteraction(e, mappedSessionId, colorArray) {
    e.stopPropagation();
    console.log('MapInteraction Handler activate');

    let miButton = $('#' + getMiButtonId(mappedSessionId));
    if (miButton.hasClass('mi-button-active')) {
        removeMapInteraction(mappedSessionId);
    } else {
        addMapInteraction(mappedSessionId, colorArray);
    }
}

function addMapInteraction(mappedSessionId, colorArray) {
    console.log('MapInteraction Adder activate');

    for (let layerName in mapInteractionLayers) {
        const layerDict = mapInteractionLayers[layerName];
        $.ajax({
            url: wfsUrl,
            type: 'POST',
            dataType: 'json',
            contentType:"application/xml",
            data: getLayerRequestData({
                'mapped_session_id': mappedSessionId,
                'layer': layerName,
            }),
            success: function (mapLayer) {
                let curId = getCurId(layerName, mappedSessionId);
                console.log('Successfully retrieved layer ' + curId + ' from GeoServer');
                layerDict.plotFunc(layerName, mappedSessionId, mapLayer, colorArray, layerDict.additional);
            }
        })
    }

    let miButtonId = getMiButtonId(mappedSessionId);
    let miButton = $('#' + miButtonId);
    miButton.addClass('mi-button-active');
    document.getElementById(miButtonId).style.backgroundColor = rgbToHex(colorArray);
}

function removeMapInteraction(mappedSessionId) {
    console.log('MapInteraction Remover active');
    let remove = false;
    for (let layerName in mapInteractionLayers){
        const layerDict = mapInteractionLayers[layerName];
        if (layerDict.removeFunc(layerName, mappedSessionId)) {
            remove = true
        }
    }
    if (remove) {
        let miButtonId = getMiButtonId(mappedSessionId);
        let miButton = $('#' + miButtonId);
        miButton.removeClass('mi-button-active');
        document.getElementById(miButtonId).style.backgroundColor = null;
    }
}

function plotOldBbox(layerName, mappedSessionId, mapLayer, colorArray, additional) {
    let sourceId = getSourceId(layerName, mappedSessionId);
    let layerId = getLayerId(layerName, mappedSessionId);
    let layerBackgroundId = getLayerBackgroundId(layerName, mappedSessionId);

    map.addSource(sourceId, {
        'type': 'geojson',
        'data': mapLayer
    });

    map.addLayer({
        "id": layerBackgroundId,
        "type": "fill",
        "source": sourceId,
        "paint": {
            'fill-color': buildRgba(colorArray, 0),
            'fill-outline-color': buildRgba(colorArray, 0),
        }
    });

    map.addLayer({
        "id": layerId,
        "type": "line",
        "source": sourceId,
        "paint": {
            "line-color": buildRgba(colorArray, 1),
            "line-width": 2,
            "line-dasharray": [4, 2],
        }
    });
    popupAdderLayerWithBackground(layerId, layerBackgroundId, additional)
}

function plotNewBbox(layerName, mappedSessionId, mapLayer, colorArray, additional) {
    let sourceId = getSourceId(layerName, mappedSessionId);
    let layerId = getLayerId(layerName, mappedSessionId);
    let layerBackgroundId = getLayerBackgroundId(layerName, mappedSessionId);

    map.addSource(sourceId, {
        'type': 'geojson',
        'data': mapLayer
    });

    // add Layer
    map.addLayer({
        "id": layerBackgroundId,
        "type": "fill",
        "source": sourceId,
        "paint": {
            'fill-color': buildRgba(colorArray, 0.2),
            'fill-outline-color': buildRgba(colorArray, 0),
        }
    });

    map.addLayer({
        "id": layerId,
        "type": "line",
        "source": sourceId,
        "paint": {
            "line-color": buildRgba(colorArray, 1),
            "line-width": 4,
            "line-dasharray": [2, 1],
        }
    });
    popupAdderLayerWithBackground(layerId, layerBackgroundId, additional)
}

function popupAdderLayerWithBackground(layerId, layerBackgroundId, additional) {
    popupAdderSingleLayer(layerBackgroundId, additional);
    popupAdderSingleLayer(layerId, additional);
}

function popupAdderSingleLayer(layerId, additional) {
    // Make layer clickable
    // https://docs.mapbox.com/mapbox-gl-js/example/polygon-popup-on-click/ 30.12.2019, 15:15
    map.on('mouseenter', layerId, changeToPointer);
    map.on('mouseleave', layerId, changeToCursor);
    map.on('click', layerId, function (e) {addGeoserverLayerClickEvent(e, additional.popupContentFunc)});
}

// Change the cursor to a pointer when the mouse is over the states layer.
function changeToPointer() {
    map.getCanvas().style.cursor = 'pointer';
}

// Change it back to a pointer when it leaves.
function changeToCursor () {
    map.getCanvas().style.cursor = '';
}

function addGeoserverLayerClickEvent(e, popupContentFunc) {
    // e.stopPropagation();
    let property = e.features[0].properties;
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML(popupContentFunc(property))
        .addTo(map);
}

// Popups
function getUserPositionPopup(property) {
    let content = 'Mapped Session: ' + property.mapped_session_id + '<br>Timestamp: ' +
        property.time_stamp;
    return getLayerPopupContent('User Position', content)
}

function getSpatialBookmarkPopup(property) {
    let content = 'Mapped Session: ' + property.mapped_session_id + '<br> Timestamp: ' +
        property.time_stamp + '<br> notes: ' + property.notes;
    return getLayerPopupContent('Spatial Bookmark', content)
}

function getMapSearchPopup(property) {
    let content = 'Mapped Session: ' + property.mapped_session_id + '<br> Start Timestamp: ' +
        property.starttime_stamp + '<br> End Timestamp: ' + property.endtitme_stamp;
    return getLayerPopupContent('Map Search', content)
}

function getClickInteractionPopup(property, content) {
    return getLayerPopupContent('Map Interaction: Click', content)
}

function getPanInteractionPopup(property, content) {
    return getLayerPopupContent('Map Interaction: Pan', content)
}

function getZoomInteractionText(property, content) {
    return content + '<br> Old Zoom Level: ' + property.old_zoom_level + '<br> New Zoom Level: ' + property.new_zoom_level;
}

function getZoomInInteractionPopup(property, content) {
    content = getZoomInteractionText(property);
    return getLayerPopupContent('Map Interaction: Zoom In', content)
}

function getZoomOutInteractionPopup(property, content) {
    content = getZoomInteractionText(property);
    return getLayerPopupContent('Map Interaction: Zoom Out', content)
}

function getMapInteractionPopup(property) {
    let content = 'Id: ' + property.id + '<br> Mapped Session: ' + property.mapped_session_id + '<br> Timestamp: ' + property.time_stamp;
    if (property.is_click_interaction) {
        return getClickInteractionPopup(property, content);
    } else if (property.is_pan_interaction) {
        return getPanInteractionPopup(property, content);
    } else if (property.is_zoom_in_interaction) {
        return getZoomInInteractionPopup(property, content);
    } else if (property.is_zoom_out_interaction) {
        return getZoomOutInteractionPopup(property, content)
    }
}

function getLayerPopupContent(layerName, content) {
    return '<div><h5>' + layerName + '</h5>' + content + '</div>'
}

// https://stackoverflow.com/questions/53921589/javascript-using-math-random-to-generate-random-rgba-values-in-for-loop 30.12.2019, 15:30
// TODO maybe a list of matching color would be better then a random one
function getRandomColor() {
    // Red, green, blue should be integers in the range of 0 - 255
    const r = 128 + parseInt(Math.random() * 127);
    const g = 128 + parseInt(Math.random() * 127);
    const b = 128 + parseInt(Math.random() * 127);

    return [r, g, b]
}

function buildRgba(colorArray, alpha) {
    let r = colorArray[0];
    let g = colorArray[1];
    let b = colorArray[2];
    return "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
}

// https://stackoverflow.com/questions/5623838/rgb-to-hex-and-hex-to-rgb, 01.01.2020, 22:30
function componentToHex(c) {
    let hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(rgb) {
    let r = rgb[0];
    let g = rgb[1];
    let b = rgb[2];
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}
