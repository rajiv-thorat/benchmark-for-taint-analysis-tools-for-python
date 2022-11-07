FROM python:3.8-buster

WORKDIR /app

RUN pip install Flask

COPY ./entrypoint.sh /usr/local/startup_scripts/

ENTRYPOINT ["sh", "/usr/local/startup_scripts/entrypoint.sh"]