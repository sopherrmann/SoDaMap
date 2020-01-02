from collections import namedtuple
from typing import List

from sqlalchemy.orm import joinedload

from app.models import *
from app.utils import timestamp_to_time

Mapper = namedtuple('Mapper', 'table attr attr_name annotatable updateable')

# Map entity type to table
TABLE_MAPPING = {
    'mapped_session': Mapper(MappedSession, MappedSession, 'mapped_session', True, False),
    'user_position': Mapper(UserPosition, MappedSession.user_positions, 'user_positions', True, True),
    'map_interaction': Mapper(MapInteraction, MappedSession.map_interactions, 'map_interactions', True, True),
    'map_search': Mapper(MapSearch, MappedSession.map_searches, 'map_searches', True, True),
    'routing': Mapper(Routing, MappedSession.routing, 'routing', True, True),
    'spatial_bookmark': Mapper(SpatialBookmark, MappedSession.spatial_bookmarks, 'spatial_bookmarks', True, True),
    'question': Mapper(Question, MappedSession.questions, 'questions', False, True),
}


def get_annotable_entities():
    return [k for k in TABLE_MAPPING.keys() if TABLE_MAPPING[k].annotatable]


def get_updateable_entities():
    return [k for k in TABLE_MAPPING if TABLE_MAPPING[k].updateable]


def get_mapped_sessions(session_type: SessionType = None):
    if session_type:
        return db.session.query(MappedSession) \
            .filter(MappedSession.session_type == session_type) \
            .all()
    return db.session.query(MappedSession).all()


def get_mapped_session_description(mapped_sessions: List[MappedSession]):
    return [
    {
        'id': m.id,
        'application_start': timestamp_to_time(m.start_application_time_stamp),
        'application_end': timestamp_to_time(m.end_application_time_stamp),
     }
            for m in mapped_sessions]


def create_annotation_entity(annotation_txt: str) -> Annotation:
    return Annotation(annotation=annotation_txt)


def insert_annotation(entity: str, entity_id: int, annotation: Annotation):
    entity_table = TABLE_MAPPING[entity].table
    entity_session = db.session.query(entity_table).filter(entity_table.id == entity_id).one()
    entity_session.annotation.append(annotation)
    db.session.commit()


def get_new_web_session_id():
    web_session = MappedSession(
        session_type=SessionType.web,
        start_application_time_stamp=datetime.now(),
        end_application_time_stamp=datetime.now(),  # TODO init special value and update when session is closed!
    )
    db.session.add(web_session)
    db.session.commit()
    return web_session.id


# TODO eager fetch as list > iterate
def get_mapped_session_by_id_eager(mapped_session_id: int, eager_fetch: db.Model) -> MappedSession:
    fetched = db.session.query(MappedSession) \
        .options(joinedload(eager_fetch)) \
        .get(mapped_session_id)
    db.session.close()
    return fetched


def get_mapped_session_by_id(mapped_session_id: int) -> MappedSession:
    fetched = db.session.query(MappedSession).get(mapped_session_id)
    db.session.close()
    return fetched


def update_mapped_session(mapped_session_id: int, mapped_session: MappedSession) -> MappedSession:
    assert mapped_session_id == mapped_session.id

    db.session.add(mapped_session)
    db.session.commit()
    return mapped_session


def get_entity_type(mapped_session_id: int, entity_type: str):
    assert entity_type in TABLE_MAPPING

    entity_mapper = TABLE_MAPPING[entity_type]
    return db.session.query(entity_mapper.table).filter_by(mapped_session_id=mapped_session_id).all()
