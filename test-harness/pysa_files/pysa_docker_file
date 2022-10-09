FROM python:3.8-buster

WORKDIR /config

RUN apt-get update && \
    apt-get upgrade && \
    apt-get -y install time && \
    pip install pyre-check

COPY ./pysa_entrypoint.sh /usr/local/startup_scripts/

ENTRYPOINT ["sh", "/usr/local/startup_scripts/pysa_entrypoint.sh"]