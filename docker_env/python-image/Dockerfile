# Download base image ubuntu 20.04
FROM ubuntu:20.04

# LABEL about the custom image
LABEL maintainer="ashrafulalam135@gmail.com"
LABEL version="1.0"
LABEL description="This is custom Docker Image for the Python server."

ENV DEBIAN_FRONTEND=noninteractive

# Update Ubuntu Software repository and install python and supporting software
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  
# mkdir ./english_thesaurus

ENTRYPOINT ["python3"]