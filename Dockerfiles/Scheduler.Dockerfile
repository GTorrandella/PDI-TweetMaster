FROM python:3.5

WORKDIR usr/src/app

COPY requirements.txt ./requirements.txt
COPY /Fetcher ./Fetcher
COPY /Campaign ./Campaign
COPY /Logger ./Logger

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-m", "Scheduler.scheduler_rabbit"]