from flask import request, jsonify
from app import app, db
from app.xml_schema import CreateFromDocument
from app.models import MappedSession
from app.obj2db import Pyxb2DB
from app.db_manage import insert_annotation


@app.route('/mapped_sessions', methods=['GET'])
def get_mapped_sessions():
    mapped_sessions = db.session.query(MappedSession).all()
    ms = [{'id': m.id} for m in mapped_sessions]
    return jsonify({
        'status': 200,
        'mapped_sessions': ms
    })


@app.route('/mapped_sessions/import', methods=['POST'])
def import_xml():
    xml_input = request.data
    xml_cls = CreateFromDocument(xml_text=xml_input)
    db_obj = Pyxb2DB(xml_cls).map()
    db.session.add(db_obj)
    db.session.commit()

    return jsonify({
        "status": 200,
        "identifier": db_obj.id,
        "inserted": db_obj.inserted,
    })


@app.route('/mapped_sessions/<mapped_session_id>/annotation', methods=['POST'])
def annotation(mapped_session_id):
    cur_annotation = request.json['annotation']
    inserted, modified = insert_annotation(mapped_session_id, cur_annotation)
    return jsonify({
        "status": 200,
        "identifier": mapped_session_id,
        "inserted": inserted,
        "modified": modified,
    })


@app.route('/logs', methods=['GET', 'POST'])
def get_all_logs():
    # get all logs
    # for POST add new log comment
    pass

