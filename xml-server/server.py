from datetime import datetime

from app import app, db
from app.models import MappedSession, GeocoordinateWithTimeStamp, Bbox, UserPosition, MapInteraction, \
    MapInteractionType, ZoomInOut, Click, Pan, MapSearch, Routing, Question, SpatialBookmark, TextWithSuggestion, \
    Suggestions


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'MappedSession': MappedSession,
            'UserPosition': UserPosition,
            'GeocoordinateWithTimeStamp': GeocoordinateWithTimeStamp,
            'Bbox': Bbox,
            'MapInteraction': MapInteraction,
            'MapInteractionType': MapInteractionType,
            'ZoomInOut': ZoomInOut,
            'Click': Click,
            'Pan': Pan,
            'MapSearch': MapSearch,
            'Routing': Routing,
            'Question': Question,
            'SpatialBookmark': SpatialBookmark,
            'TextWithSuggestion': TextWithSuggestion,
            'Suggestions': Suggestions,
            'datetime': datetime,
            }
