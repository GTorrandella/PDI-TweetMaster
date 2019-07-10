FROM python:3.5

WORKDIR usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY /Fetcher ./Fetcher
COPY /Scheduler ./Scheduler
COPY /Campaign ./Campaign
COPY /Logger ./Logger
COPY /DataBaseConnector ./DataBaseConnector
COPY /Tweet ./Tweet

ENTRYPOINT ["python3", "-m", "Scheduler.scheduler_rabbit"]