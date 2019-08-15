FROM ubuntu
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip
RUN python3.7 -m pip install pip
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-setuptools
RUN apt-get install -y wget
RUN apt-get install unzip
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip
RUN unzip ngrok-stable-linux-386.zip -d /usr/local/bin
RUN ngrok --version
RUN apt-get install -y python-dev python3.7-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip
RUN mkdir /housebot
ADD ./requirements.txt /housebot/requirements.txt
RUN python3.7 -m pip install -r /housebot/requirements.txt
RUN python3.7 -m spacy download en
ADD . /housebot
WORKDIR /housebot
RUN python3.7 train_nlu_core.py
