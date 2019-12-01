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

*general information*
1. ``/mapped_sessions`` [GET]:  
returns a list of all mapped_sessions
1. ``/mapped_sessions/mapped`` [GET]:  
returns a list of all mapped_sessions created from a xml insertion
1. ``/mapped_sessions/web`` [GET]:  
returns a list of all mapped_sessions which were manually created

*import*
1. ``/mapped_sessions/import`` [POST]:  
is used to upload mapped session xml files following the schema into the database.

*annotation*
1. ``/annotation/<entity_types>`` [GET]:  
returns a list of annotatable entities
1. ``/annotation/<entity_type>/<entity_id>`` [POST]:  
adds a given annotation to the specified entity

*Web session management*
1. ``/mapped_sessions/new`` [POST]:  
creates a new *mapped session* in the database. This is used for logging. A log session is also stored as mapped session.
1. ``/mapped_sessions/<mapped_session_id>`` [GET]:   
return the given mapped_session as XML file. Should be used to retrieve log sessions as XML.
1. ``/mapped_sessions/<mapped_session_id>`` [PATCH]:  
Updates a given attribute of a mapped session. Currently only the end_application_time_stamp can be updated.
1. ``/mapped_sessions/entity_types`` [GET]:  
Returns a list of all entities which can be added to a mapped_session
1. ``/mapped_sessions/<mapped_session_id>/<entitiy_type>`` [POST]:  
Adds an additional entity of the specified entity_type to the given mapped_session. Have a look into the
example-requests folder to find possible request  bodies for different entities.
