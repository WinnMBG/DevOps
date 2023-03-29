FROM ubuntu:latest

RUN echo "I am run during image building"
RUN apt-get update 
RUN apt-get install python3 python3-pip -y
RUN pip install --upgrade flask
RUN pip install --upgrade redis

WORKDIR /home/user
COPY ./app.py .

ENTRYPOINT ["python3","app.py"]
