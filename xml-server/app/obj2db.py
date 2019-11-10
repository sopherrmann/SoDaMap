from typing import List

import app.xml_schema as schema
import app.models as dbm
from app.utils import create_point, create_bbox_from_obj


class Pyxb2DB:

    def __init__(self, xml_cls: schema.MappedSession):
        self.xml = xml_cls
        self.db = None

    def map(self) -> dbm.MappedSession:
        self.db = dbm.MappedSession(
            start_application_time_stamp=self.xml.startApplicationTimeStamp,
            end_application_time_stamp=self.xml.endApplicationTimeStamp,
            user_positions=self.get_user_positions(),
            map_interactions=self.get_map_interaction(),
            map_searches=self.get_map_searches(),
            routing=self.get_routing(),
            questions=self.get_questions(),
            spatial_bookmarks=self.get_spatial_bookmarks(),
        )
        return self.db

    def get_user_positions(self) -> List[dbm.UserPosition]:
        db_user_positions = []
        for u in self.xml.userPositionElements.userPosition:
            db_user_positions.append(
                dbm.UserPosition(
                    time_stamp=u.timeStamp,
                    geom=create_point(x=u.longitude, y=u.latitude),
                )
            )
        return db_user_positions

    def get_map_interaction(self) -> List[dbm.MapInteraction]:
        db_map_interactions = []
        for m in self.xml.mapInteractionsElements.singleMapInteraction:
            # Add content from userPosition part
            mu = m.userPositionWithTimeStamp
            map_interaction = dbm.MapInteraction(
                time_stamp=mu.timeStamp,
                geom=create_point(x=mu.longitude, y=mu.latitude),
                )
            # Add content from MapInteractionType part
            map_interaction = self.get_map_interaction_type(m.mapInteractionTypeName, map_interaction)
            db_map_interactions.append(map_interaction)
        return db_map_interactions

    def get_map_interaction_type(self, mt: schema.mapInteractionType, map_interaction: dbm.MapInteraction) -> dbm.MapInteraction:

        if mt.clickInteraction:
            ul = mt.clickInteraction.BBox.upperLeftCorner
            lr = mt.clickInteraction.BBox.lowerRightCorner

            map_interaction.is_click_interaction = True
            map_interaction.new_bbox_time_stamp_lr = lr.timeStamp,
            map_interaction.new_bbox_time_stamp_ul = ul.timeStamp,
            map_interaction.new_bbox_geom = create_bbox_from_obj(ul=ul, lr=lr)

        elif mt.panInteraction:
            map_interaction.is_pan_interaction = True
            map_interaction = self.fill_old_new_bbox(mt, 'panInteraction', map_interaction)

        elif mt.zoomInInteraction:
            map_interaction.is_zoom_in_interaction = True
            map_interaction = self.fill_old_new_bbox(mt, 'zoomInInteraction', map_interaction)
            map_interaction.old_zoom_level = mt.zoomInInteraction.oldZoomLevel
            map_interaction.new_zoom_level = mt.zoomInInteraction.newZoomLevel

        elif mt.zoomOutInteraction:
            map_interaction.is_zoom_out_interaction = True
            map_interaction = self.fill_old_new_bbox(mt, 'zoomOutInteraction', map_interaction)
            map_interaction.old_zoom_level = mt.zoomOutInteraction.oldZoomLevel
            map_interaction.new_zoom_level = mt.zoomOutInteraction.newZoomLevel

        return map_interaction

    @staticmethod
    def fill_old_new_bbox(mt: schema.mapInteractionType, map_interaction_name: str, map_interaction: dbm.MapInteraction):
        attr = getattr(mt, map_interaction_name)
        new_ul = attr.newBBox.upperLeftCorner
        new_lr = attr.newBBox.lowerRightCorner
        old_ul = attr.oldBBox.upperLeftCorner
        old_lr = attr.oldBBox.lowerRightCorner

        map_interaction.new_bbox_time_stamp_lr = new_lr.timeStamp
        map_interaction.new_bbox_time_stamp_ul = new_ul.timeStamp
        map_interaction.new_bbox_geom = create_bbox_from_obj(ul=new_ul, lr=new_lr)
        map_interaction.old_bbox_time_stamp_lr = old_lr.timeStamp
        map_interaction.old_bbox_time_stamp_ul = old_ul.timeStamp
        map_interaction.old_bbox_geom = create_bbox_from_obj(ul=old_ul, lr=old_lr)
        return map_interaction

    def get_map_searches(self) -> List[dbm.MapSearch]:
        def set_bbox():
            if ms.BBox:
                lr = ms.BBox.lowerRightCorner
                ul = ms.BBox.upperLeftCorner
                db_ms.bbox_time_stamp_lr = lr.timeStamp,
                db_ms.bbox_time_stamp_ul = ul.timeStamp,
                db_ms.bbox_geom = create_bbox_from_obj(ul=ul, lr=lr),

        db_map_searches = []
        for ms in self.xml.mapSearchsElements.mapSearchElement:
            db_ms = dbm.MapSearch(
                starttime_stamp=ms.StarttimeStamp,
                endtime_stamp=ms.EndtimeStamp,
                text_with_suggestion=self.get_text_with_suggestions(ms.textWithSuggestions),
            )
            set_bbox()
            db_map_searches.append(db_ms)
        return db_map_searches

    def get_routing(self) -> dbm.Routing:
        r = self.xml.routingsElements.routingElement
        return dbm.Routing(
            start_routing_time_stamp=r.startRoutingTimeStamp,
            end_routing_time_stamp=r.endRoutingTimeStamp,
            start_routing_interface_time_stamp=r.startRoutingInterfaceTimeStamp,
            end_routing_interface_send_request_or_interface_closed_time_sta=r.endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp,
            origin_text_box_history=self.get_orig_routing(r.OriginTextBoxHistory),
            destination_text_box_history=self.get_destination_routing(r.DestiantionTextBoxHistory)
        )

    def get_orig_routing(self, tws: List[schema.textWithSuggestions]) -> List[dbm.RoutingOrigin]:
        return [dbm.RoutingOrigin(text_with_suggestion=self.create_text_with_suggestion(t)) for t in tws]

    def get_destination_routing(self, tws: List[schema.textWithSuggestions]) -> List[dbm.RoutingDestination]:
        return [dbm.RoutingDestination(text_with_suggestion=self.create_text_with_suggestion(t)) for t in tws]

    def get_questions(self) -> List[dbm.Question]:
        db_questions = []
        for q in self.xml.questionsElements.question:
            db_questions.append(
                dbm.Question(
                    question=q.question,
                    answer=q.answer,
                )
            )
        return db_questions

    def get_spatial_bookmarks(self) -> List[dbm.SpatialBookmark]:
        db_spatial_bookmarks = []
        for s in self.xml.spatialBookmarksElements.spatialBookmark:
            su = s.userPositionWithTimeStamp
            db_spatial_bookmarks.append(
                dbm.SpatialBookmark(
                    time_stamp=su.timeStamp,
                    geom=create_point(x=su.longitude, y=su.latitude),
                    notes=s.notes,
                )
            )
        return db_spatial_bookmarks

    def get_text_with_suggestions(self, tws: List[schema.textWithSuggestions]) -> List[dbm.TextWithSuggestion]:
        return [self.create_text_with_suggestion(t) for t in tws]

    @staticmethod
    def create_text_with_suggestion(t: schema.textWithSuggestions) -> dbm.TextWithSuggestion:
        return dbm.TextWithSuggestion(
            text_typed=t.textTyped,
            suggestion_chosen=t.suggestionChosen,
            suggestions=[dbm.Suggestion(suggestion=sug) for sug in t.suggestions] if t.suggestions else [],
        )
