FROM python:3.6-alpine
MAINTAINER M.Sadeq Azarkaman
ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tempneed gcc libc-dev linux-headers \
        postgresql-dev
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN apk del .tempneed
RUN mkdir /app
WORKDIR /app

COPY . /app

RUN adduser -D apiuser
USER apiuser
