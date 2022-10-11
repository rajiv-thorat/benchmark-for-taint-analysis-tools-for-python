FROM snyk/snyk:python-3.8

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade && \
    apt-get -y install time

ENTRYPOINT ["time", "-o", "/op/non_exec_metrics.txt", "snyk", "code", "test", "--json-file-output=/op/issues.json"]