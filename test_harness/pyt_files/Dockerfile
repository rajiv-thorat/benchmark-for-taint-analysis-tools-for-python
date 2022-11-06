FROM python:3.8-buster

WORKDIR /pyt

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install time

ENTRYPOINT ["time", "-o", "/op/non_exec_metrics.txt", "python3", "-m", "pyt", "-j", "-o", "/op/vuls.json", "/app"]