FROM python:3.11-buster

RUN mkdir /app
WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src .