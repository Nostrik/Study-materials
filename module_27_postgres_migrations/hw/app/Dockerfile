FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

ADD flask_app.py /var/server/flask_app.py

WORKDIR /var/server

#CMD gunicorn --workers=2 flask_app:app

ENTRYPOINT ["gunicorn", "-b", ":5000", "flask_app:app"]