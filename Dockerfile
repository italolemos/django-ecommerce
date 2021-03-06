FROM python:3.6

RUN apt-get update
RUN apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
RUN mkdir -p /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/
