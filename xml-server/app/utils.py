from datetime import datetime
from typing import List

from app.xml_schema import geocoordinateWithTimeStamp
from app.models import TextWithSuggestion, Suggestion, RoutingOrigin, RoutingDestination


def create_point(x: float, y: float, srid: int = None):
    srid = srid if srid else 4326
    return f'SRID={srid};POINT({x} {y})'


def create_bbox(ul: List[float], lr: List[float], srid: int = None):
    return _create_bbox(*ul, *lr, srid)


def _create_bbox(xmin: float, ymax: float, xmax: float, ymin: float, srid: int = None):
    srid = srid if srid else 4326
    coords = f'({xmin} {ymin}, {xmin} {ymax}, {xmax} {ymax}, {xmax} {ymax}, {xmin} {ymin})'
    return f'SRID={srid};POLYGON({coords})'


def create_bbox_from_obj(ul: geocoordinateWithTimeStamp, lr: geocoordinateWithTimeStamp, srid: int = None):
    return _create_bbox(
        xmin=min(ul.longitude, lr.longitude),
        xmax=max(ul.longitude, lr.longitude),
        ymin=min(ul.latitude, lr.latitude),
        ymax=max(ul.latitude, lr.latitude),
        srid=srid,
    )


def apply_to_entity(json_dict: dict, entity):
    entity_attributes = [a for a in dir(entity) if not a.startswith('__')]
    prohibited = ['id']

    # handle geom fields (points and polygons)
    if 'geom' in entity_attributes:
        json_dict['geom'] = create_point(**json_dict['geom'])
    bbox_field_names = [b for b in entity_attributes if 'bbox' in b and 'geom' in b and b in json_dict]
    for bbox_name in bbox_field_names:
        json_dict[bbox_name] = _create_bbox(**json_dict[bbox_name])

    # Handle fancy routing TextWithSuggestion
    if 'origin_text_box_history' in entity_attributes:
        json_dict['origin_text_box_history'] = apply_to_entity(json_dict['origin_text_box_history'], RoutingOrigin())
    if 'destination_text_box_history' in entity_attributes:
        json_dict['destination_text_box_history'] = apply_to_entity(json_dict['destination_text_box_history'], RoutingDestination())

    # Handle text_with_suggestion
    # suggestion table references back to text_with_suggestion
    if 'text_with_suggestion' in entity_attributes and not isinstance(entity, Suggestion):
        json_dict['text_with_suggestion'] = [apply_to_entity(tws, TextWithSuggestion())
                                             for tws in json_dict['text_with_suggestion']]
    # Suggestions are not mandatory for a TextWithSuggestion entity
    if 'suggestions' in entity_attributes and 'suggestions' in json_dict:
        json_dict['suggestions'] = [apply_to_entity(sug, Suggestion()) for sug in json_dict['suggestions']]

    for key in entity_attributes:
        if key not in prohibited and key in json_dict:
            # transform date for columns(!) of type datetime > check needed as also relations can be set here
            if key in entity.__table__.c and str(entity.__table__.c[key].type) == 'DATETIME':
                setattr(entity, key, time_to_timestamp(json_dict[key]))
            else:
                setattr(entity, key, json_dict[key])
    return entity


def time_to_timestamp(time) -> datetime:
    # TODO: Settle on timestamp format
    fmt = '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(time, fmt)
