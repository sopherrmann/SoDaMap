from datetime import datetime

from app import app, db
from app.models import MappedSession, UserPosition, MapInteraction, \
    MapSearch, Routing, Question, SpatialBookmark, TextWithSuggestions, Suggestions
from app.utils import create_bbox, create_point


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'MappedSession': MappedSession,
            'UserPosition': UserPosition,
            'MapInteraction': MapInteraction,
            'MapSearch': MapSearch,
            'Routing': Routing,
            'Question': Question,
            'SpatialBookmark': SpatialBookmark,
            'TextWithSuggestions': TextWithSuggestions,
            'Suggestions': Suggestions,
            'datetime': datetime,
            'create_point': create_point,
            'create_polygon': create_bbox,
            }
