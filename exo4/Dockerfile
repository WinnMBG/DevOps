FROM ubuntu:latest

RUN echo "I am run during image building"
RUN apt-get update 
RUN apt-get install python3 python3-pip -y
RUN pip install --upgrade flask
RUN apt-get install mysql-client -y

WORKDIR /home/user
COPY . .

ENTRYPOINT ["ls", "-la"]

