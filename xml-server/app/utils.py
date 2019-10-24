def create_point(x, y, srid=None):
    srid = srid if srid else 4326
    return f'SRID={srid};POINT({x} {y})'
