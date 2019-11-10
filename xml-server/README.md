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

## Available endpoints

Currently three endpoints available:

1. ``/mapped_sessions`` [GET]:  
returns a list of already inserted mapped_sessions
1. ``/mapped_sessions/import`` [POST]:  
is used to upload mapped session xml files following the schema.
1. ``/mapped_sessions/<mapped_session_id>/annotation`` [POST]:  
adds an annotation to the given mapped_session. A JSON body of the following schema needs to be passed:
{"annotation": "your annotation text"}

**to be implemented**
1. ``/logs`` [POST]:   
is used to store a log message in the database
1. ``/logs`` [GET]:   
returns all available lob messages in xml format
