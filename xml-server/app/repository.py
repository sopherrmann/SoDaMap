from collections import namedtuple

from sqlalchemy.orm import joinedload

from app.models import *

Mapper = namedtuple('Mapper', 'table attr annotatable')

# Map entity type to table
TABLE_MAPPING = {
    'mapped_session': Mapper(MappedSession, MappedSession, True),
    'user_position': Mapper(UserPosition, MappedSession.user_positions, True),
    'map_interaction': Mapper(MapInteraction, MappedSession.map_interactions, True),
    'map_search': Mapper(MapSearch, MappedSession.map_searches, True),
    'routing': Mapper(Routing, MappedSession.routing, True),
    'spatial_bookmark': Mapper(SpatialBookmark, MappedSession.spatial_bookmarks, True),
    'question': Mapper(Question, MappedSession.questions, False),
}


def get_annotable_entities():
    return [k for k in TABLE_MAPPING.keys() if TABLE_MAPPING[k].annotatable]


def get_mapped_sessions():
    return db.session.query(MappedSession)\
        .filter(MappedSession.session_type == SessionType.mapped)\
        .all()


def insert_annotation(entity: str, entity_id: int, annotation: Annotation):
    entity_table = TABLE_MAPPING[entity].table
    entity_session = db.session.query(entity_table).filter(entity_table.id == entity_id).one()
    entity_session.annotations.append(annotation)
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
