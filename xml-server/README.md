# SoDa Map XML-Server

This is a simple flask server managing the connection between the user interface and the database. In more detail it is
handling xml uploads, annotation functionality and logs.

## Setup

### Using virtualenv

1. Navigate into this folder and create a virtual environment (currently only tested with Python3.6)
```bash
virtualenv SoDaXMLenv -p python3.6
```
1. Activate the environment and install all needed requirements into it
```bash
source SoDaXMLenv/bin/activate
pip install -r requirements.txt
```
1. Run the flask server
```
flask run
```
After this the flask server should be running on http://127.0.0.1:5000/.

### Using docker

There is a Dockerfile available in this folder which performs the whole setup.

1. Navigate into this folder and build the docker image
```bash
docker build -t xmlserver-img .
```
1. Run docker image
```bash
docker run --name xmlserver xmlserver-img
```
To explicitly set the location of the database add the following to the run statement
``--env DATABASE_URL=postgresql://username:password@host:port/db_name``

### Using docker-compose

In the SoDaMap repository a docker-compose file is provided. This also includes the XMLServer. Therefore by running the
docker-compose also this component will be running. (See SoDaMap README for more detailed explanation.)

## Available endpoints

**already available**:

1. ``/mapped_sessions`` [GET]:  
returns a list of already inserted mapped_sessions
1. ``/mapped_sessions/import`` [POST]:  
is used to upload mapped session xml files following the schema into the database.
1. ``/annotation/<entity_types>`` [GET]:  
returns a list of annotatable entities
1. ``/annotation/<entity_type>/<entity_id>`` [POST]:  
adds a given annotation to the specified entity

**to be implemented**
1. ``/logs`` [POST]:   
is used to store a log message in the database
1. ``/logs`` [GET]:   
returns all available lob messages in xml format
