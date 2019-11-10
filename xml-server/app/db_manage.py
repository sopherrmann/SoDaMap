from datetime import datetime

from app import db
from app.models import MappedSession, Annotation


def insert_annotation(mapped_session_id: int, annotation: str):
    mapped_session = db.session.query(MappedSession).filter(MappedSession.id == mapped_session_id).one()
    mapped_session.annotations.append(Annotation(annotation=annotation))
    mapped_session.modified = datetime.now()
    db.session.add(mapped_session)
    db.session.commit()

    return mapped_session.inserted, mapped_session.modified
