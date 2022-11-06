FROM python:3.8-buster

WORKDIR /app

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install time && \
    pip install python-taint

ENTRYPOINT ["time", "-o", "/op/non_exec_metrics.txt", "pyt", "-j", "-o", "/op/vuls.json", "/app"]