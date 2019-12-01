import app.xml_schema as schema
from app import db
from app.obj2db import ParserXMLDB, get_db_from_xml, get_xml_from_db_id


def test_import_serialization():
    with open('data/sample1.xml') as f:
        input = f.read()
    db_id = get_db_from_xml(input)
    output = get_xml_from_db_id(db_id)
    assert input == output


if __name__ == '__main__':
    test_import_serialization()
