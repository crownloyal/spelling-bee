# syntax=docker/dockerfile:1

FROM python:3.9-bullseye

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
EXPOSE 50002
CMD [ "python", "./sb/sb_stats.py"]
