FROM python:3.10.4

ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

RUN mkdir /app
WORKDIR /app

COPY ./ /app

RUN ls .

RUN pip install -r requirements.txt
