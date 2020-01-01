from typing import List

from app.models import Routing, TextWithSuggestion, MapSearch, UserPosition, MapInteraction, Question, SpatialBookmark
from app.repository import get_entity_type
from app.utils import wkb_to_xy


class ParseDbJson:

    def get_func_from_entity_type(self, entity_type):
        mapper = {
            'user_position': self.get_user_position,
            'map_interaction': self.get_map_interaction,
            'map_search': self.get_map_search,
            'routing': self.get_routing,
            'question': self.get_question,
            'spatial_bookmark': self.get_spatial_bookmark,
        }
        return mapper[entity_type]

    def get_json_entity_from_db(self, mapped_session_id: int, entity_type: str):
        entities = get_entity_type(mapped_session_id, entity_type)
        entity_mapper_func = self.get_func_from_entity_type(entity_type)
        return entity_mapper_func(entities)

    def get_user_position(self, entities: List[UserPosition]) -> List[dict]:
        return [self._get_geo_coord_with_time_from_obj(entity) for entity in entities]

    def get_map_interaction(self, entities: List[MapInteraction]) -> List[dict]:
        map_interaction = []
        for entity in entities:
            d = {
                'UserPositionWithTimeStamp': self._get_geo_coord_with_time_from_obj(entity),
                'ClickInteraction': None,
                'PanInteraction': None,
                'ZoomInInteraction': None,
                'ZoomOutInteraction': None,
            }
            if entity.is_click_interaction:
                d['ClickInteraction'] = self._get_click_interaction(entity)
            elif entity.is_pan_interaction:
                d['PanInteraction'] = self._get_pan_interaction(entity)
            elif entity.is_zoom_in_interaction:
                d['ZoomInInteraction'] = self._get_zoom_interaction(entity)
            elif entity.is_zoom_out_interaction:
                d['ZoomOutInteraction'] = self._get_zoom_interaction(entity)

            map_interaction.append(d)
        return map_interaction

    def _get_click_interaction(self, entity: MapInteraction) -> dict:
        return {
            'WhereClicked': self._get_geo_coord_with_time(*wkb_to_xy(entity.where_clicked_geom), entity.where_clicked_time_stamp),
            'BBox': self._get_bbox(entity.new_bbox_geom, entity.new_bbox_time_stamp_lr, entity.new_bbox_time_stamp_ul),
        }

    def _get_pan_interaction(self, entity: MapInteraction) -> dict:
        return {
            'NewNBox': self._get_bbox(entity.new_bbox_geom, entity.new_bbox_time_stamp_lr,
                                      entity.new_bbox_time_stamp_ul),
            'OldBBox': self._get_bbox(entity.old_bbox_geom, entity.old_bbox_time_stamp_lr,
                                      entity.old_bbox_time_stamp_ul)
        }

    def _get_zoom_interaction(self, entity: MapInteraction) -> dict:
        return {
            'NewNBox': self._get_bbox(entity.new_bbox_geom, entity.new_bbox_time_stamp_lr,
                                      entity.new_bbox_time_stamp_ul),
            'OldBBox': self._get_bbox(entity.old_bbox_geom, entity.old_bbox_time_stamp_lr,
                                      entity.old_bbox_time_stamp_ul),
            'NowZoomLevel': entity.new_zoom_level,
            'OldZoomLevel': entity.old_zoom_level,
        }

    def get_question(self, entities: List[Question]) -> List[dict]:
        return [
            {
                'question': entity.question,
                'answer': entity.answer,
            }
            for entity in entities]

    def get_spatial_bookmark(self, entities: List[SpatialBookmark]) -> List[dict]:
        return [
            {
                'UserPositionWithTimeStamp': self._get_geo_coord_with_time_from_obj(entity),
                'Notes': entity.notes
            }
            for entity in entities
        ]

    def get_routing(self, entities: List[Routing]):
        entity = entities[0]
        return {
            'StartRoutingInterfaceTimeStamp': entity.start_routing_interface_time_stamp,
            'EndRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp': entity.end_routing_interface_send_request_or_interface_closed_time_sta,
            'OriginTextBoxHistory': [self._get_text_with_suggestions(tws)
                                     for tws in entity.origin_text_box_history.text_with_suggestion],
            'DestiantionTextBoxHistory': [self._get_text_with_suggestions(tws)
                                          for tws in entity.destination_text_box_history.text_with_suggestion],
            'StartRoutingTimeStamp': entity.start_routing_time_stamp,
            'EndRoutingTimeStamp': entity.end_routing_time_stamp
        }

    def get_map_search(self, entities: List[MapSearch]) -> List[dict]:
        map_search = []
        for entity in entities:
            d = {
                'StarttimeStamp': entity.starttime_stamp,
                'EndtimeStamp': entity.endtime_stamp,
                'textWithSuggestions': [self._get_text_with_suggestions(tws) for tws in entity.text_with_suggestion]
            }
            if entity.bbox_geom is not None:
                d['BBox'] = self._get_bbox(entity.bbox_geom, entity.bbox_time_stamp_lr, entity.bbox_time_stamp_ul)
            map_search.append(d)
        return map_search

    def _get_text_with_suggestions(self, tws: TextWithSuggestion) -> dict:
        return {
            'textTyped': tws.text_typed,
            'suggestionChosen': tws.suggestion_chosen,
            'suggestions': tws.suggestions
        }

    def _get_bbox(self, geom_elem, time_lr, time_ul) -> dict:
        xmin, ymin, xmax, ymax = wkb_to_xy(geom_elem)
        return {
            'LowerRightCorner': self._get_geo_coord_with_time(xmax, ymin, time_lr),
            'UpperLeftCorner': self._get_geo_coord_with_time(xmin, ymax, time_ul)
        }

    def _get_geo_coord_with_time(self, x, y, time) -> dict:
        return {
            'TimeStamp': time,
            'Latitude': y,
            'Longitude': x,
        }

    def _get_geo_coord_with_time_from_obj(self, obj):
        x, y = wkb_to_xy(obj.geom)
        return self._get_geo_coord_with_time(x, y, obj.time_stamp)