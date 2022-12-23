FROM python:3.7

RUN apt-get update && apt-get install -y python3-dev supervisor nginx && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
RUN apt-get -y update
RUN apt-get -y install nano

COPY src/ /app/
COPY nginx.conf /etc/nginx/nginx.conf
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY supervisord.ini /etc/supervisor/conf.d/supervisord.ini
COPY static/ /static/
COPY ./static /usr/share/nginx/html/static

WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.ini"]