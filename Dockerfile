FROM python:3.6.1-alpine

# MAINTAINER "amon5cb@gmail.com"

# RUN apt-get update -y && \ 
# apt-get install -y python-pip python-dev

# COPY ./requirements.txt /app/requirements.txt

WORKDIR /chatbot

# RUN pip install -r requirements.txt

ADD . /chatbot


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt  

CMD ["python3", "server.py"]