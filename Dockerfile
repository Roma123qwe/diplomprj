FROM ubuntu:20.04

RUN apt-get update 
RUN apt-get -y upgrade
RUN apt-get -y install python3-pip
RUN mkdir /calender
WORKDIR /calender
COPY ./calender/requirements.txt /prj/
RUN pip3 install -r /prj/requirements.txt