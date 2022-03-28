FROM python:3.8-slim-buster

ADD ./ ./mercury-orchestrator

RUN pip install schedule
RUN pip install requests
RUN pip install pika --upgrade

WORKDIR /mercury-orchestrator

CMD [ "python", "/mercury-orchestrator/main.py" ]