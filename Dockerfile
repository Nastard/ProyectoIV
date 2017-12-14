FROM python:3

MAINTAINER David Sánchez Montés <anixo.a.tope@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 80
CMD [ "hug", "-p 80", "-f", "./botQueToca/hugweb.py" ]
