import enum
from datetime import datetime

from geoalchemy2.types import Geometry

from app import db


class SessionType(enum.Enum):
    mapped = 'MappedSession'
    web = 'WebSession'


class MappedSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.Enum(SessionType), default=SessionType.mapped, nullable=False)

    inserted = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    start_application_time_stamp = db.Column(db.DateTime, nullable=False)
    end_application_time_stamp = db.Column(db.DateTime, nullable=False)

    # relations
    user_positions = db.relationship('UserPosition', back_populates='mapped_session', cascade='all, delete-orphan')
    map_interactions = db.relationship('MapInteraction', back_populates='mapped_session', cascade='all, delete-orphan')
    map_searches = db.relationship('MapSearch', back_populates='mapped_session', cascade='all, delete-orphan')
    routing = db.relationship('Routing', back_populates='mapped_session', uselist=False, cascade='all, delete-orphan')
    questions = db.relationship('Question', back_populates='mapped_session', cascade='all, delete-orphan')
    spatial_bookmarks = db.relationship('SpatialBookmark', back_populates='mapped_session',
                                        cascade='all, delete-orphan')
    annotations = db.relationship('Annotation')


class UserPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='user_positions')
    annotation = db.relationship('Annotation')

    time_stamp = db.Column(db.DateTime, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

    def __repr__(self):
        return f'UserPosition(time={self.time_stamp}, geom={self.geom})'


class MapInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession')
    annotation = db.relationship('Annotation')

    time_stamp = db.Column(db.DateTime, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

    # type of interaction
    is_zoom_in_interaction = db.Column(db.Boolean, default=False)
    is_zoom_out_interaction = db.Column(db.Boolean, default=False)
    is_click_interaction = db.Column(db.Boolean, default=False)
    is_pan_interaction = db.Column(db.Boolean, default=False)

    # for pan and zoom (new bbox for click)
    old_bbox_time_stamp_lr = db.Column(db.DateTime)
    old_bbox_time_stamp_ul = db.Column(db.DateTime)
    old_bbox_geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))
    new_bbox_time_stamp_lr = db.Column(db.DateTime)
    new_bbox_time_stamp_ul = db.Column(db.DateTime)
    new_bbox_geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))

    # for zoom
    old_zoom_level = db.Column(db.Integer)
    new_zoom_level = db.Column(db.Integer)

    def __repr__(self):
        if self.is_click_interaction:
            return f'MapInteraction(Click, time={self.time_stamp}, geom={self.geom})'
        if self.is_zoom_in_interaction:
            return f'MapInteraction(ZoomIn, time={self.time_stamp}, zoomLevel=({self.old_zoom_level} to {self.new_zoom_level}))'
        if self.is_zoom_out_interaction:
            return f'MapInteraction(ZoomOut, time={self.time_stamp}, zoomLevel=({self.old_zoom_level} to {self.new_zoom_level}))'
        if self.is_pan_interaction:
            return f'MapInteraction(Pan, time={self.time_stamp})'


class MapSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='map_searches')
    annotation = db.relationship('Annotation')

    starttime_stamp = db.Column(db.DateTime, nullable=False)
    endtime_stamp = db.Column(db.DateTime, nullable=False)
    bbox_time_stamp_lr = db.Column(db.DateTime)
    bbox_time_stamp_ul = db.Column(db.DateTime)
    bbox_geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))

    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='map_search',
                                           cascade='all, delete-orphan')  # min 1

    def __repr__(self):
        return f'MapSearch(start_time={self.starttime_stamp}, end_time={self.endtime_stamp}, TextWithSug={self.text_with_suggestion})'


class Routing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='routing')
    annotation = db.relationship('Annotation')

    start_routing_interface_time_stamp = db.Column(db.DateTime, nullable=False)
    end_routing_interface_send_request_or_interface_closed_time_sta = db.Column(db.DateTime, nullable=False)
    start_routing_time_stamp = db.Column(db.DateTime)
    end_routing_time_stamp = db.Column(db.DateTime)

    origin_text_box_history = db.relationship('RoutingOrigin', cascade='all, delete-orphan', uselist=False)  # min 1
    destination_text_box_history = db.relationship('RoutingDestination', cascade='all, delete-orphan', uselist=False)  # min 1

    def __repr__(self):
        return f'Routing(OriginTextBox={self.origin_text_box_history}, DestinationTextBox={self.destination_text_box_history})'


# Join Table
class RoutingOrigin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routing_id = db.Column(db.Integer, db.ForeignKey('routing.id'), nullable=False)
    routing = db.relationship('Routing', back_populates='origin_text_box_history', uselist=False)
    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='routing_origin',
                                           cascade='all, delete-orphan')

    def __repr__(self):
        return f'RoutingOrigin(TextWithSug={self.text_with_suggestion})'


# Join Table
class RoutingDestination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routing_id = db.Column(db.Integer, db.ForeignKey('routing.id'), nullable=False)
    routing = db.relationship('Routing', back_populates='destination_text_box_history', uselist=False)
    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='routing_destination',
                                           cascade='all, delete-orphan')

    def __repr__(self):
        return f'RoutingDestination(TextWithSug={self.text_with_suggestion})'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='questions')

    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text)

    def __repr__(self):
        return f'Question(question={self.question}, answer={self.answer})'


class SpatialBookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='spatial_bookmarks')
    annotation = db.relationship('Annotation')

    time_stamp = db.Column(db.DateTime, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f'SpatialBookmark(time={self.time_stamp}, geom={self.geom})'


class TextWithSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_search_id = db.Column(db.Integer, db.ForeignKey('map_search.id'))
    map_search = db.relationship('MapSearch', back_populates='text_with_suggestion')
    routing_origin_id = db.Column(db.Integer, db.ForeignKey('routing_origin.id'))
    routing_origin = db.relationship('RoutingOrigin', back_populates='text_with_suggestion', uselist=False)
    routing_destination_id = db.Column(db.Integer, db.ForeignKey('routing_destination.id'))
    routing_destination = db.relationship('RoutingDestination', back_populates='text_with_suggestion', uselist=False)

    text_typed = db.Column(db.Text, nullable=False)
    suggestion_chosen = db.Column(db.Text)
    suggestions = db.relationship('Suggestion')

    def __repr__(self):
        return f'TextWithSuggestion(TextTyped={self.text_typed}, SugChosen{self.suggestion_chosen}, Suggestions={self.suggestions})'


class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_with_suggestion_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'))
    text_with_suggestion = db.relationship('TextWithSuggestion')
    suggestion = db.Column(db.Text)

    def __repr__(self):
        return f'Suggestion({self.suggestion})'


class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    user_position_id = db.Column(db.Integer, db.ForeignKey('user_position.id'))
    map_interaction_id = db.Column(db.Integer, db.ForeignKey('map_interaction.id'))
    map_search_id = db.Column(db.Integer, db.ForeignKey('map_search.id'))
    routing_id = db.Column(db.Integer, db.ForeignKey('routing.id'))
    spatial_bookmark_id = db.Column(db.Integer, db.ForeignKey('spatial_bookmark.id'))

    annotation = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Annotation({self.annotation})'
