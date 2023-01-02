FROM ubuntu:focal


RUN apt-get update && apt-get install -y python3.9 python3.9

#Create a directory inside my container and put myself in
RUN mkdir -p  /home/app

WORKDIR /home/app

COPY script/weather_classification_tp.py  ./

RUN mkdir  $(pwd)/data_inputs
RUN mkdir  $(pwd)/data_outputs

RUN echo $(pwd)


# Copy current folder files to /home/app
COPY requirements.txt .
COPY /data/ResNet152V2-Weather-Classification-03.h5 .

#For install all the requirements
RUN apt-get -y install python3-pip
RUN pip install -r requirements.txt
RUN pwd && ls

CMD ["python3","weather_classification_tp.py"]
