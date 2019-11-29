from flask import request, jsonify

from app import app
from app.obj2db import Pyxb2DB
from app.repository import *
from app.utils import time_to_timestamp, apply_to_entity
from app.xml_schema import CreateFromDocument
from app.models import SessionType


@app.route('/mapped_sessions', methods=['GET'])
def route_get_mapped_sessions():
    ms = get_mapped_session_description(get_mapped_sessions())
    return jsonify({
        'status': 200,
        'mapped_sessions': ms
    })


@app.route('/mapped_sessions/mapped')
def route_get_mapped_sessions_mapped():
    ms = get_mapped_session_description(get_mapped_sessions(SessionType.mapped))
    return jsonify({
        'status': 200,
        'mapped_sessions': ms
    })


@app.route('/mapped_sessions/web')
def route_get_mapped_sessions_web():
    ms = get_mapped_session_description(get_mapped_sessions(SessionType.web))
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

    annotation_entity = create_annotation_entity(cur_annotation)
    insert_annotation(entity_type, entity_id, annotation_entity)
    return jsonify({
        "status": 200,
        "entity": entity_type,
        "entity_identifier": entity_id,
    })


# need to get one web_session_id per web session (equivalent to mapped_session but when using the webGIS)
@app.route('/mapped_sessions/new', methods=['POST'])
def route_create_new_mapped_session():
    web_session_id = get_new_web_session_id()
    return jsonify({
        "status": 200,
        "web_session_id": web_session_id
    })


@app.route('/mapped_sessions/<int:mapped_session_id>', methods=['PATCH'])
def route_update_mapped_session(mapped_session_id: int):
    # Currently end time is only value which can be updated
    end_time = time_to_timestamp(request.json['end_time'])
    to_update = get_mapped_session_by_id(mapped_session_id)

    if not to_update:
        return forge_error_404()

    to_update.end_application_time_stamp = end_time
    update_mapped_session(mapped_session_id, to_update)

    return jsonify({
        "status": 200,
        "web_session_id": mapped_session_id,
    })


@app.route('/mapped_sessions/entity_types', methods=['GET'])
def route_get_entity_types_to_update():
    entities = get_updateable_entities()
    return jsonify({
        "status": 200,
        "entity_types": ', '.join(entities)
    })


@app.route('/mapped_sessions/<int:mapped_session_id>/<string:entity_type>', methods=['POST'])
def route_write_log(mapped_session_id: int, entity_type: str):
    if entity_type not in get_updateable_entities():
        return forge_error(400, f'Unknown type {entity_type}')
    entity_mapper = TABLE_MAPPING[entity_type]

    mapped_session = get_mapped_session_by_id_eager(mapped_session_id, entity_mapper.attr)
    if not mapped_session:
        return forge_error_404()

    # create database entity
    data = request.json
    try:
        entity = apply_to_entity(data, entity_mapper.table())
    except ValueError as e:
        return forge_error(400, str(e))

    complete_entity = getattr(mapped_session, entity_mapper.attr_name)
    # assumed that all entities will be a list in the future > TODO check
    if isinstance(complete_entity, list):
        complete_entity.append(entity)
    else:
        complete_entity = entity
    setattr(mapped_session, entity_type, complete_entity)

    update_mapped_session(mapped_session_id, mapped_session)

    return jsonify({
        "status": 200,
        "updated_entity": entity_type,
    })


def forge_error_404():
    return forge_error(404, "Not found")


def forge_error(status_code: int, message: str):
    return jsonify({
        "status": status_code,
        "message": message
    }), status_code
