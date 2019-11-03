from flask import request
from app import app, db
from app.xml_schema import CreateFromDocument
from app.obj2db import Pyxb2DB


@app.route('/import', methods=['POST'])
def import_xml():
    xml_input = request.data
    xml_cls = CreateFromDocument(xml_text=xml_input)
    db_obj = Pyxb2DB(xml_cls).map()
    db.session.add(db_obj)
    db.session.commit()


@app.route('/annotation', methods=['POST'])
def annotation():
    # needs to include mapped session, annotation, user (?)
    pass


@app.route('/logs', methods=['GET', 'POST'])
def get_all_logs():
    # get all logs
    # for POST add new log comment
    pass


@app.route('/logs/<id>')
def get_log(id: int):
    pass

