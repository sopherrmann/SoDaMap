from geoalchemy2.types import Geometry
from datetime import datetime

from app import db


class MappedSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inserted = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, onupdate=datetime.now)
    start_application_time_stamp = db.Column(db.DateTime, nullable=False)
    end_application_time_stamp = db.Column(db.DateTime, nullable=False)

    user_positions = db.relationship('UserPosition', back_populates='mapped_session', cascade='all, delete-orphan')
    map_interactions = db.relationship('MapInteraction', back_populates='mapped_session', cascade='all, delete-orphan')
    map_searches = db.relationship('MapSearch', back_populates='mapped_session', cascade='all, delete-orphan')
    # TODO not a list obj can only occures once!
    routing = db.relationship('Routing', back_populates='mapped_session', uselist=False, cascade='all, delete-orphan')
    questions = db.relationship('Question', back_populates='mapped_session', cascade='all, delete-orphan')
    spatial_bookmarks = db.relationship('SpatialBookmark', back_populates='mapped_session', cascade='all, delete-orphan')
    annotations = db.relationship('Annotation', back_populates='mapped_session')


class UserPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='user_positions')

    time_stamp = db.Column(db.DateTime, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)


class MapInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession')

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


class MapSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='map_searches')

    starttime_stamp = db.Column(db.DateTime, nullable=False)
    endtime_stamp = db.Column(db.DateTime, nullable=False)
    bbox_time_stamp_lr = db.Column(db.DateTime)
    bbox_time_stamp_ul = db.Column(db.DateTime)
    bbox_geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))

    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='map_search',
                                            cascade='all, delete-orphan')  # min 1


class Routing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='routing')

    start_routing_interface_time_stamp = db.Column(db.DateTime, nullable=False)
    end_routing_interface_send_request_or_interface_closed_time_sta = db.Column(db.DateTime, nullable=False)
    start_routing_time_stamp = db.Column(db.DateTime)
    end_routing_time_stamp = db.Column(db.DateTime)

    origin_text_box_history = db.relationship('RoutingOrigin', cascade='all, delete-orphan')
    destination_text_box_history = db.relationship('RoutingDestination', cascade='all, delete-orphan')


# Join Table
class RoutingOrigin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routing_id = db.Column(db.Integer, db.ForeignKey('routing.id'), nullable=False)
    routing = db.relationship('Routing', back_populates='origin_text_box_history', uselist=False)
    text_with_suggestion_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'), nullable=False)
    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='routing_origin', uselist=False,
                                           cascade='all, delete-orphan', single_parent=True)


# Join Table
class RoutingDestination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routing_id = db.Column(db.Integer, db.ForeignKey('routing.id'), nullable=False)
    routing = db.relationship('Routing', back_populates='destination_text_box_history', uselist=False)
    text_with_suggestion_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'), nullable=False)
    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='routing_destination', uselist=False,
                                           cascade='all, delete-orphan', single_parent=True)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='questions')

    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text)


class SpatialBookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='spatial_bookmarks')

    time_stamp = db.Column(db.DateTime, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    notes = db.Column(db.Text)


class TextWithSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_search_id = db.Column(db.Integer, db.ForeignKey('map_search.id'))
    map_search = db.relationship('MapSearch', back_populates='text_with_suggestion')
    routing_origin = db.relationship('RoutingOrigin', back_populates='text_with_suggestion', uselist=False)
    routing_destination = db.relationship('RoutingDestination', back_populates='text_with_suggestion', uselist=False)

    text_typed = db.Column(db.Text, nullable=False)
    suggestion_chosen = db.Column(db.Text)
    suggestions = db.relationship('Suggestion')


class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_with_suggestion_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'))
    text_with_suggestion = db.relationship('TextWithSuggestion')
    suggestion = db.Column(db.Text)


class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='annotations')
    annotation = db.Column(db.Text, nullable=False)
