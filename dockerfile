FROM python:3.7

RUN apt-get update &&\
    apt-get install zip &&\
    apt-get install unzip