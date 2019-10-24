from app import db
from geoalchemy2.types import Geometry


class MappedSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_application_time_stamp = db.Column(db.DateTime, nullable=False)
    end_application_time_stamp = db.Column(db.DateTime, nullable=False)

    user_positions = db.relationship('UserPosition', back_populates='mapped_session')
    map_interactions = db.relationship('MapInteraction', back_populates='mapped_session')
    map_searches = db.relationship('MapSearch', back_populates='mapped_session')
    routings = db.relationship('Routing', back_populates='mapped_session')
    questions = db.relationship('Question', back_populates='mapped_session')
    spatial_bookmarks = db.relationship('SpatialBookmark', back_populates='mapped_session')
#    annotation = db.relationship('Annotation', back_populates='mapped_session')


class GeocoordinateWithTimeStamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

    user_position = db.relationship('UserPosition', back_populates='geocoord')
    map_interaction = db.relationship('MapInteraction', back_populates='geocoord')
    click = db.relationship('Click', back_populates='where_clicked')
    spatial_bookmark = db.relationship('SpatialBookmark', back_populates='geocoord')


class Bbox(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    upper_left_coordinate_id = db.Column(db.Integer, db.ForeignKey('geocoordinate_with_time_stamp.id'))
    lower_right_coordinate_id = db.Column(db.Integer, db.ForeignKey('geocoordinate_with_time_stamp.id'))

    upper_left_coordinate = db.relationship('GeocoordinateWithTimeStamp', foreign_keys=[upper_left_coordinate_id],
                                            uselist=False)  # min 1
    lower_right_coordinate = db.relationship('GeocoordinateWithTimeStamp', foreign_keys=[lower_right_coordinate_id],
                                             uselist=False)  # min 1

    click = db.relationship('Click', back_populates='bbox')
    map_search = db.relationship('MapSearch', back_populates='bbox')


class UserPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='user_positions')

    geocoord_id = db.Column(db.Integer, db.ForeignKey('geocoordinate_with_time_stamp.id'))
    geocoord = db.relationship('GeocoordinateWithTimeStamp', back_populates='user_position', uselist=False)


class MapInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession')

    geocoord_id = db.Column(db.Integer, db.ForeignKey('geocoordinate_with_time_stamp.id'))
    geocoord = db.relationship('GeocoordinateWithTimeStamp', uselist=False)

    map_interaction_type = db.relationship('MapInteractionType', back_populates='map_interaction', uselist=False)


class MapInteractionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_interaction_id = db.Column(db.Integer, db.ForeignKey('map_interaction.id'))
    map_interaction = db.relationship('MapInteraction', back_populates='map_interaction_type')

    zoom_in_interaction = db.relationship('ZoomInOut', uselist=False)
    zoom_out_interaction = db.relationship('ZoomInOut', uselist=False)
    click_interaction = db.relationship('Click', uselist=False)
    pan_interaction = db.relationship('Pan', uselist=False)


class ZoomInOut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_interaction_type_id = db.Column(db.Integer, db.ForeignKey('map_interaction_type.id'))
    map_interaction_type = db.relationship('MapInteractionType', back_populates='zoom_in_interaction') # ?

    old_zoom_level = db.Column(db.Integer, nullable=False)
    new_zoom_level = db.Column(db.Integer, nullable=False)
    old_bbox_id = db.Column(db.Integer, db.ForeignKey('bbox.id'))
    new_bbox_id = db.Column(db.Integer, db.ForeignKey('bbox.id'))
    old_bbox = db.relationship('Bbox', foreign_keys=[old_bbox_id], uselist=False)
    new_bbox = db.relationship('Bbox', foreign_keys=[new_bbox_id], uselist=False)


class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_interaction_type_id = db.Column(db.Integer, db.ForeignKey('map_interaction_type.id'))
    map_interaction_type = db.relationship('MapInteractionType', back_populates='click_interaction')

    where_clicked_id = db.Column(db.Integer, db.ForeignKey('geocoordinate_with_time_stamp.id'))
    where_clicked = db.relationship('GeocoordinateWithTimeStamp', back_populates='click', uselist=False)
    bbox_id = db.Column(db.Integer, db.ForeignKey('bbox.id'))
    bbox = db.relationship('Bbox', back_populates='click', uselist=False)


class Pan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_interaction_type_id = db.Column(db.Integer, db.ForeignKey('map_interaction_type.id'))
    map_interaction_type = db.relationship('MapInteractionType', back_populates='pan_interaction')

    old_bbox_id = db.Column(db.Integer, db.ForeignKey('bbox.id'))
    new_bbox_id = db.Column(db.Integer, db.ForeignKey('bbox.id'))
    old_bbox = db.relationship('Bbox', foreign_keys=[old_bbox_id], uselist=False)
    new_bbox = db.relationship('Bbox', foreign_keys=[new_bbox_id], uselist=False)


class MapSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='map_searches')

    starttime_stamp = db.Column(db.DateTime, nullable=False)
    endtime_stamp = db.Column(db.DateTime, nullable=False)
    bbox_id = db.Column(db.Integer, db.ForeignKey('bbox.id'))
    bbox = db.relationship('Bbox', back_populates='map_search', uselist=False)
    text_with_suggestions = db.relationship('TextWithSuggestion', back_populates='map_search')  # min 1


class Routing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
    mapped_session = db.relationship('MappedSession', back_populates='routings')

    start_routing_interface_time_stamp = db.Column(db.DateTime, nullable=False)
    end_routing_interface_send_request_or_interface_closed_time_stamp = db.Column(db.DateTime, nullable=False)
    start_routing_time_stamp = db.Column(db.DateTime)
    end_routing_time_stamp = db.Column(db.DateTime)

    origin_text_box_history_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'))
    destination_text_box_history_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'))
    origin_text_box_history = db.relationship('TextWithSuggestion', foreign_keys=[origin_text_box_history_id])
    destination_text_box_history = db.relationship('TextWithSuggestion', foreign_keys=[destination_text_box_history_id])


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

    geocoord_id = db.Column(db.Integer, db.ForeignKey('geocoordinate_with_time_stamp.id'))
    geocoord = db.relationship('GeocoordinateWithTimeStamp', back_populates='spatial_bookmark', uselist=False)
    notes = db.Column(db.Text)


class TextWithSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_search_id = db.Column(db.Integer, db.ForeignKey('map_search.id'))
    map_search = db.relationship('MapSearch', back_populates='text_with_suggestions')

    text_typed = db.Column(db.Text, nullable=False)
    suggestion_choosen = db.Column(db.Text)
    suggestions = db.relationship('Suggestions', back_populates='text_with_suggestion', uselist=False)


class Suggestions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_with_suggestion_id = db.Column(db.Integer, db.ForeignKey('text_with_suggestion.id'))
    text_with_suggestion = db.relationship('TextWithSuggestion', back_populates='suggestions')
    suggestion = db.Column(db.Text)


# class Annotation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     mapped_session_id = db.Column(db.Integer, db.ForeignKey('mapped_session.id'))
#     mapped_session = db.relationship('MappedSession', back_populates='annotations')
#     annotation = db.Column(db.Text)
#
