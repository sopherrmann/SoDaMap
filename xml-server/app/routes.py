from flask import request, jsonify

from app import app
from app.obj2db import Pyxb2DB
from app.repository import *
from app.utils import time_to_timestamp, apply_to_entity
from app.xml_schema import CreateFromDocument


@app.route('/mapped_sessions', methods=['GET'])
def route_get_mapped_sessions():
    mapped_sessions = get_mapped_sessions()
    ms = [{'id': m.id} for m in mapped_sessions]
    return jsonify({
        'status': 200,
        'mapped_sessions': ms
    })


@app.route('/mapped_sessions/import', methods=['POST'])
def route_import_xml():
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


@app.route('/annotation/entity_types', methods=['GET'])
def route_get_annotatable_entities():
    entities = get_annotable_entities()
    return jsonify({
        "status": 200,
        "entity_types": ', '.join(entities)
    })


@app.route('/annotation/<string:entity_type>/<int:entity_id>', methods=['POST'])
def route_annotation(entity_type: str, entity_id: int):
    cur_annotation = request.json['annotation']

    if entity_type not in get_annotable_entities():
        return forge_error(400, f'Entity of type {entity_type} can not be annotated.')

    insert_annotation(entity_type, entity_id, cur_annotation)
    return jsonify({
        "status": 200,
        "entity": entity_type,
        "entity_identifier": entity_id,
    })

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

