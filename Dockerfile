FROM python:alpine

ARG flask_env=local
ENV FLASK_ENV=${flask_env}
ENV PYTHONPATH /deploy
ENV FLASK_APP /deploy/mastermindgameapi/app.py

RUN adduser -s /bin/bash -D mastermind

COPY --chown=mastermind:mastermind . /deploy

RUN pip3  install -r /deploy/requirements.txt

WORKDIR /deploy/mastermindgameapi

USER mastermind

CMD flask run --host=0.0.0.0
