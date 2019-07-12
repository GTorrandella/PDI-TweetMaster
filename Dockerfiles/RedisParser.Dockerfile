FROM python:3.5

WORKDIR usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY /Tweet ./Tweet
COPY /Campaign ./Campaign
COPY /DataBaseConnector ./DataBaseConnector
COPY /Logger ./Logger
COPY /RedisParser ./RedisParser