FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    python3-dev

RUN apt-get install -y \
    libpq-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python3", "./server.py" ]
