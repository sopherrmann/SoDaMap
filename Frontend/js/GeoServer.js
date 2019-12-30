const geoServerUrl = "http://localhost:8082/geoserver";
const wfsUrl = geoServerUrl + '/wfs';

const geoserverLayers = {
    // 'map_interaction',
    'map_search': {
        'removeFunc': removeOnlyPolygon,
        'plotFunc': plotOnlyPolygonSource,
        'additional': {'popupContentFunc': getMapSearchPopup}},
    'spatial_bookmark': {
        'removeFunc': removeOnlyPoint,
        'plotFunc': plotOnlyPointSource,
        'additional': {'iconName': 'star-15', 'popupContentFunc': getSpatialBookmarkPopup}},
    'user_position': {
        'removeFunc': removeOnlyPoint,
        'plotFunc': plotOnlyPointSource,
        'additional': {'iconName': 'marker-15', 'popupContentFunc': getUserPositionPopup}},
};

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
    console.log('mapped session loader ' + mappedSessionId);

    let colorArray = getRandomColor();
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
                    console.log('Successfully retrieved layer' + curId + 'from GeoServer');

                    let sourceId = getSourceId(layerName, mappedSessionId);
                    map.addSource(sourceId, {
                        'type': 'geojson',
                        'data': mapLayer
                    });
                    layerDict.plotFunc(layerName, mappedSessionId, colorArray, layerDict.additional);
                    console.log('Successfully added layer' + curId + 'to map')
                }
            });
        }
    }
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

function removeOnlyPoint(layerName, mappedSessionId) {
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

function plotOnlyPointSource(layerName, mappedSessionId, colorArray, additional) {
    let layerId = getLayerId(layerName, mappedSessionId);
    let sourceId = getSourceId(layerName, mappedSessionId);
    let layerIdBackground = getLayerBackgroundId(layerName, mappedSessionId);

    // https://github.com/mapbox/mapbox-gl-style-spec/issues/97, 30.12.2019, 14:00
    map.addLayer({
        "id": layerIdBackground,
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

    // Make layer clickable
    // https://docs.mapbox.com/mapbox-gl-js/example/polygon-popup-on-click/ 30.12.2019, 15:15
    map.on('click', layerId, function (e) {addGeoserverLayerClickEvent(e, additional.popupContentFunc)});
    map.on('click', layerIdBackground, function (e) {addGeoserverLayerClickEvent(e, additional.popupContentFunc)});
    map.on('mouseenter', layerId, changeToPointer);
    map.on('mouseenter', layerIdBackground, changeToPointer);
    map.on('mouseleave', layerId, changeToCursor);
    map.on('mouseleave', layerIdBackground, changeToCursor);

}

function removeOnlyPolygon(layerName, mappedSessionId) {
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

function plotOnlyPolygonSource(layerName, mappedSessionId, colorArray, additional) {
    let layerId = getLayerId(layerName, mappedSessionId);
    let sourceId = getSourceId(layerName, mappedSessionId);

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

    // Add Popup
    map.on('click', layerId, function (e) {addGeoserverLayerClickEvent(e, additional.popupContentFunc)});
    map.on('mouseenter', layerId, changeToPointer);
    map.on('mouseleave', layerId, changeToCursor);
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
    let property = e.features[0].properties;
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML(popupContentFunc(property))
        .addTo(map);
}

// Popups
function getUserPositionPopup(property) {
    let content = 'Mapped Session: ' + property.mapped_session_id + '<br>Timestamp: ' + property.time_stamp;
    return getLayerPopupContent('User Position', content)
}

function getSpatialBookmarkPopup(property) {
    let content = 'Mapped Session: ' + property.mapped_session_id + '<br> Timestamp: ' + property.time_stamp + '<br> notes: ' + property.notes;
    return getLayerPopupContent('Spatial Bookmark', content)
}

function getMapSearchPopup(property) {
    let content = 'Mapped Session: ' + property.mapped_session_id + '<br> Start Timestamp: ' + property.starttime_stamp + '<br> End Timestamp: ' + property.endtitme_stamp;
    return getLayerPopupContent('Map Search', content)
}

function getLayerPopupContent(layerName, content) {
    return '<div><h5>' + layerName + '</h5>' + content + '</div>'
}

// https://stackoverflow.com/questions/53921589/javascript-using-math-random-to-generate-random-rgba-values-in-for-loop 30.12.2019, 15:30
// TODO maybe a list of matching color would be better then a random one
function getRandomColor() {
    // Red, green, blue should be integers in the range of 0 - 255
    const r = parseInt(Math.random() * 255);
    const g = parseInt(Math.random() * 255);
    const b = parseInt(Math.random() * 255);

    return [r, g, b]
}

function buildRgba(colorArray, alpha) {
    let r = colorArray[0];
    let g = colorArray[1];
    let b = colorArray[2];
    return "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
}
