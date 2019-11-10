from datetime import datetime

from app import app, db
from app.models import MappedSession, UserPosition, MapInteraction, \
    MapSearch, Routing, Question, SpatialBookmark, TextWithSuggestion, Suggestion
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
            'TextWithSuggestions': TextWithSuggestion,
            'Suggestions': Suggestion,
            'datetime': datetime,
            'create_point': create_point,
            'create_polygon': create_bbox,
            }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
