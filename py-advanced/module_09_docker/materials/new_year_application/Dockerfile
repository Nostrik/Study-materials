FROM python:3.7.9-slim-stretch

ENV TERM xterm

RUN mkdir /app

RUN mkdir /app/static

RUN mkdir /app/templates

COPY static /app/static

COPY templates /app/templates

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY app.py /app/

WORKDIR /app

ENTRYPOINT ["python", "app.py"]