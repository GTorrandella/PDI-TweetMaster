FROM python:3.5

WORKDIR usr/src/app

COPY requirements.txt ./requirements.txt
COPY campaign_api_flask.py ./campaign_api_flask.py
COPY /Tweet ./Tweet
COPY /Campaign ./Campaign
COPY /Reporter ./Reporter
COPY /Manager ./Manager
COPY /DataBaseConnector ./DataBaseConnector
COPY /Logger ./Loggers

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-m", "campaign_api_flask"]