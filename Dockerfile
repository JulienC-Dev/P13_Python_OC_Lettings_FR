FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app/oc_lettings_site
#CMD gunicorn wsgi:application --bind 0.0.0.0:8000