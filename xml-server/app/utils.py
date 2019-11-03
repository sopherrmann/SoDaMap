from typing import List
from app.xml_schema import geocoordinateWithTimeStamp


def create_point(x: float, y: float, srid: int=None):
    srid = srid if srid else 4326
    return f'SRID={srid};POINT({x} {y})'


def _create_bbox(xmin: float, ymax: float, xmax: float, ymin: float, srid: int=None):
    srid = srid if srid else 4326
    coords = f'({xmin} {ymin}, {xmin} {ymax}, {xmax} {ymax}, {xmax} {ymax}, {xmin} {ymin})'
    return f'SRID={srid};POLYGON({coords})'


def create_bbox_from_obj(ul: geocoordinateWithTimeStamp, lr: geocoordinateWithTimeStamp, srid: int=None):
    _create_bbox(
        xmin=ul.longitude,
        ymax=ul.latitude,
        xmax=lr.longitude,
        ymin=lr.latitude,
        srid=srid,
    )
