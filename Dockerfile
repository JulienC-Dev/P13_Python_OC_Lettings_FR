FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /app/oc_lettings_site
RUN python3 manage.py collectstatic --noinput --clear
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate


WORKDIR /app/oc_lettings_site
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT