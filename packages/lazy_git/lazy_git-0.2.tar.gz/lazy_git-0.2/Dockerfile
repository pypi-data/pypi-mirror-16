FROM python:3

MAINTAINER Tim Jones <tjones@mintel.com>

COPY . /docker
WORKDIR /docker

RUN apt-get install git
RUN python setup.py install

ENV LAZY_GIT_MODE Production
CMD python manage.py runserver --host 0.0.0.0 --port 65004

EXPOSE 65004
