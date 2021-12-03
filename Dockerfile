# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY bot.py bot.py
COPY .env .env
RUN pip3 install -r requirements.txt

CMD [ "python3", "bot.py" ]