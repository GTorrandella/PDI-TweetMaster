FROM python:3.5

WORKDIR usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY /Fetcher ./Fetcher
COPY /Tweet ./Tweet
COPY /Campaign ./Campaign
COPY /Logger ./Logger

ENTRYPOINT ["python3", "-m", "Fetcher.fetcher_consumer"]

