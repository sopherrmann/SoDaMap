from datetime import datetime
from typing import List

from app.xml_schema import geocoordinateWithTimeStamp


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
    entity_attibutes = [a for a in dir(entity) if not a.startswith('__')]
    prohibited = ['id']
    for key in entity_attibutes:
        if key not in prohibited and key in json_dict:
            if str(entity.__table__.c[key].type) == 'DATETIME':
                setattr(entity, key, time_to_timestamp(json_dict[key]))
            else:
                setattr(entity, key, json_dict[key])
    return entity


def time_to_timestamp(time) -> datetime:
    # TODO: Settle on timestamp format
    fmt = '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(time, fmt)
