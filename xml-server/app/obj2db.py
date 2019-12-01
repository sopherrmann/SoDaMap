from typing import List

from app import db
import app.models as dbm
import app.xml_schema as schema
from app.utils import create_point, create_bbox_from_obj, wkb_to_xy


class ParserXMLDB:

    def __init__(self, xml_cls: schema.MappedSession = None, db_obj: dbm.MappedSession = None, db_id: int = None):
        self.xml = xml_cls
        self.db = db_obj
        self.db_id = db_id

    # Database query is needed here to use lazy loading
    def set_db_from_id(self):
        self.db = db.session.query(dbm.MappedSession).get(self.db_id)

    def set_db(self) -> None:
        if self.db:
            return
        if self.db_id:
            self.set_db_from_id()
        elif self.xml:
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

    def set_xml(self):
        if self.xml:
            return
        if not self.db and self.db_id:
            self.set_db_from_id()
        if self.db:
            self.xml = schema.MappedSession(
                startApplicationTimeStamp=self.db.start_application_time_stamp,
                endApplicationTimeStamp=self.db.end_application_time_stamp,
                userPositionElements=self.s_get_user_position(),
                mapInteractionsElements=self.s_get_map_interaction(),
                mapSearchsElements=self.s_get_map_search(),
                routingsElements=self.s_get_routings(),
                questionsElements=self.s_get_questions(),
                spatialBookmarksElements=self.s_get_spatial_bookmarks(),
            )

    # XML to DB
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
            where_clicked = mt.clickInteraction.whereClicked

            map_interaction.is_click_interaction = True
            map_interaction.new_bbox_time_stamp_lr = lr.timeStamp
            map_interaction.new_bbox_time_stamp_ul = ul.timeStamp
            map_interaction.new_bbox_geom = create_bbox_from_obj(ul=ul, lr=lr)

            map_interaction.where_clicked_geom = create_point(x=where_clicked.longitude, y=where_clicked.latitude)
            map_interaction.where_clicked_time_stamp = where_clicked.timeStamp

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
                db_ms.bbox_time_stamp_lr = lr.timeStamp
                db_ms.bbox_time_stamp_ul = ul.timeStamp
                db_ms.bbox_geom = create_bbox_from_obj(ul=ul, lr=lr)

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

    def get_orig_routing(self, tws: List[schema.textWithSuggestions]) -> dbm.RoutingOrigin:
        return dbm.RoutingOrigin(text_with_suggestion=self.get_text_with_suggestions(tws))

    def get_destination_routing(self, tws: List[schema.textWithSuggestions]) -> dbm.RoutingDestination:
        return dbm.RoutingDestination(text_with_suggestion=self.get_text_with_suggestions(tws))

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

    # DB to XML
    def s_get_user_position(self) -> schema.userPositions:
        return schema.userPositions(userPosition=[self.get_geo_coord_with_time_from_obj(u) for u in self.db.user_positions])

    def s_get_spatial_bookmarks(self) -> schema.spatialBookmarks:
        sb_all = []
        for sb in self.db.spatial_bookmarks:
            sb_xml = schema.spatialBookmark(
                userPositionWithTimeStamp=self.get_geo_coord_with_time_from_obj(sb)
            )
            if sb.notes:
                sb_xml.notes = sb.notes
            sb_all.append(sb_xml)

        if len(sb_all) == 0:
            sb_all = None
        return schema.spatialBookmarks(spatialBookmark=sb_all)

    def get_geo_coord_with_time_from_obj(self, db_elem):
        x, y = wkb_to_xy(db_elem.geom)
        return self.get_geo_coord_with_time(x, y, db_elem.time_stamp)

    @staticmethod
    def get_geo_coord_with_time(x, y, time_stamp):
        return schema.geocoordinateWithTimeStamp(
            timeStamp=time_stamp,
            latitude=y,
            longitude=x,
        )

    def get_bbox(self, geom_elem, time_lr, time_ul) -> schema.bbox:
        xmin, ymin, xmax, ymax = wkb_to_xy(geom_elem)
        return schema.bbox(
            lowerRightCorner=self.get_geo_coord_with_time(xmax, ymin, time_lr),
            upperLeftCorner=self.get_geo_coord_with_time(xmin, ymax, time_ul),
        )

    @staticmethod
    def s_get_text_with_sug(tws: dbm.TextWithSuggestion) -> schema.textWithSuggestions:
        # may not work if suggestions is None
        tws_xml = schema.textWithSuggestions(
            textTyped=tws.text_typed,
            suggestionChosen=tws.suggestion_chosen,
        )
        tws_xml.suggestions = None
        if tws.suggestions:
            tws_xml.suggestions = schema.suggestions(suggestion=[sug.suggestion for sug in tws.suggestions])
        return tws_xml

    def s_get_questions(self) -> schema.questions:
        return schema.questions(
            question=[
                schema.questionStruct(
                    question=q.question,
                    answer=q.answer,
                )
                for q in self.db.questions
            ]
        )

    def s_get_routings(self) -> schema.routings:
        r = None
        if self.db.routing:
            r = schema.routing(
                startRoutingInterfaceTimeStamp=self.db.routing.start_routing_interface_time_stamp,
                endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp=self.db.routing.end_routing_interface_send_request_or_interface_closed_time_sta,
                OriginTextBoxHistory=[self.s_get_text_with_sug(tws)
                                      for tws in self.db.routing.origin_text_box_history.text_with_suggestion],
                DestiantionTextBoxHistory=[self.s_get_text_with_sug(tws)
                                           for tws in self.db.routing.destination_text_box_history.text_with_suggestion],
            )
            r.startRoutingTimeStamp = None
            r.endRoutingTimeStamp = None
            if self.db.routing.start_routing_time_stamp:
                r.startRoutingTimeStamp = self.db.routing.start_routing_time_stamp
            if self.db.routing.end_routing_time_stamp:
                r.endRoutingTimeStamp = self.db.routing.end_routing_time_stamp

        return schema.routings(routingElement=r)

    def s_get_map_search(self) -> schema.mapSearchs:
        ms_all = []
        for ms in self.db.map_searches:
            msi = schema.mapSearch(
                StarttimeStamp=ms.starttime_stamp,
                EndtimeStamp=ms.endtime_stamp,
                textWithSuggestions=[self.s_get_text_with_sug(tws) for tws in ms.text_with_suggestion]
            )
            msi.BBox = None
            if ms.bbox_geom is not None:
                msi.BBox = self.get_bbox(ms.bbox_geom, ms.bbox_time_stamp_lr, ms.bbox_time_stamp_ul)
            ms_all.append(msi)

        if len(ms_all) == 0:
            ms_all = None
        return schema.mapSearchs(mapSearchElement=ms_all)

    def s_get_map_interaction(self) -> schema.mapInteractions:
        mi_xml_all = []
        for mi in self.db.map_interactions:
            mi_xml = schema.mapInteraction(
                userPositionWithTimeStamp=self.get_geo_coord_with_time_from_obj(mi)
            )
            if mi.is_click_interaction:
                mi_xml.mapInteractionTypeName = schema.mapInteractionType(
                    clickInteraction=self.s_get_click_interaction(mi)
                )
            elif mi.is_pan_interaction:
                mi_xml.mapInteractionTypeName = schema.mapInteractionType(
                    panInteraction=self.s_get_pan_interaction(mi)
                )
            elif mi.is_zoom_in_interaction:
                mi_xml.mapInteractionTypeName = schema.mapInteractionType(
                    zoomInInteraction=self.s_get_zoom_in_out_interaction(mi)
                )
            elif mi.is_zoom_out_interaction:
                mi_xml.mapInteractionTypeName = schema.mapInteractionType(
                    zoomOutInteraction=self.s_get_zoom_in_out_interaction(mi)
                )

            mi_xml_all.append(mi_xml)

        if len(mi_xml_all) == 0:
            mi_xml_all = None
        return schema.mapInteractions(singleMapInteraction=mi_xml_all)

    def s_get_click_interaction(self, mi) -> schema.click:
        return schema.click(
            whereClicked=self.get_geo_coord_with_time(*wkb_to_xy(mi.where_clicked_geom), mi.where_clicked_time_stamp),
            BBox=self.get_bbox(mi.new_bbox_geom, mi.new_bbox_time_stamp_lr, mi.new_bbox_time_stamp_ul),
        )

    def s_get_zoom_in_out_interaction(self, mi) -> schema.zoomInOut:
        return schema.zoomInOut(
            newBBox=self.get_bbox(mi.new_bbox_geom, mi.new_bbox_time_stamp_lr, mi.new_bbox_time_stamp_ul),
            newZoomLevel=mi.new_zoom_level,
            oldBBox=self.get_bbox(mi.old_bbox_geom, mi.old_bbox_time_stamp_lr, mi.old_bbox_time_stamp_ul),
            oldZoomLevel=mi.old_zoom_level,
        )

    def s_get_pan_interaction(self, mi) -> schema.pan:
        return schema.pan(
            newBBox=self.get_bbox(mi.new_bbox_geom, mi.new_bbox_time_stamp_lr, mi.new_bbox_time_stamp_ul),
            oldBBox=self.get_bbox(mi.old_bbox_geom, mi.old_bbox_time_stamp_lr, mi.old_bbox_time_stamp_ul),
        )


def get_db_from_xml(xml_data):
    xml_obj = schema.CreateFromDocument(xml_data)
    parser = ParserXMLDB(xml_obj)
    parser.set_db()
    db_obj = parser.db
    db.session.add(db_obj)
    db.session.commit()
    return db_obj.id


def get_xml_from_db_id(db_id):
    parser = ParserXMLDB(db_id=db_id)
    parser.set_xml()
    xml = parser.xml.toxml("utf-8", element_name='outputFile')
    return xml.decode('utf-8')
