const geoServerUrl = "http://localhost:8082/geoserver";
const wfsUrl = geoServerUrl + '/wfs';

const geoserverLayers = [
    'map_interaction',
    'map_search',
    'spatial_bookmark',
    'user_position'];

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

function load_mapped_session_layers(mapped_session_id) {
    console.log('mapped session loader ' + mapped_session_id);

    for (let layerName in geoserverLayers) {
        const curId = layerName + '_ ' +  mapped_session_id;
        const layerId = 'layer_' + curId;
        const sourceId = 'source_' + curId;

        const mapLayer = map.getLayer(layerId);
        if (typeof mapLayer !== 'undefined') {
            map.removeLayer(layerId).removeSource(sourceId);
            console.log('Removed Layer and source' + curId);
        } else {
            $.ajax({
                url: wfsUrl,
                type: 'POST',
                dataType: 'json',
                contentType:"application/xml",
                data: getLayerRequestData({
                    'mapped_session_id': mapped_session_id,
                    'layer': layerName,
                }),
                success: function (layer) {
                    console.log('Successfully retrieved layer from XmlServer');
                    let firstSymbolId = get_index_of_first_symbol_layer()

                    map.addSource('source_' + layerId, {
                        'type': 'geojson',
                        'data': layer
                    });
                    map.addLayer({
                            'id': layerId,
                            'type': 'circle',
                            'source': sourceId,
                            'paint': {
                                'circle-radius': 60,
                                'circle-color': '#B42222'
                            },
                            'filter': ['==', '$type', 'Point']
                        },
                        firstSymbolId
                    );
                    console.log('Successfully added layer to map')
                }
            });
        }
    }
}
