FROM ubuntu:latest

RUN echo "I am run during image building"
RUN apt-get update 
RUN apt-get install python3 python3-pip -y

WORKDIR /home/user
COPY ./app.py .

ENTRYPOINT ["ls","-la",";","python3", "./app.py"]
