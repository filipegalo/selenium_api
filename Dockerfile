FROM selenium/standalone-chrome:4.0.0-beta-1-prerelease-20201202

USER root

RUN apt-get update && apt-get -y upgrade
RUN apt install -y python3
RUN apt install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip install uwsgi

WORKDIR /srv/
RUN mkdir /srv/selenium
COPY ./selenium /srv/selenium
COPY selenium.conf /etc/supervisor/conf.d/
RUN pip install -r /srv/selenium/requirements.txt

WORKDIR /srv/selenium

EXPOSE 4444 4000