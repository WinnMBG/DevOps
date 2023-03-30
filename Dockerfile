FROM ubuntu:latest

RUN echo "I am run during image building"
RUN apt-get update 
RUN apt-get install python3 python3-pip -y
RUN pip install --upgrade flask

WORKDIR /home/user
COPY ./ ./

ENTRYPOINT ["python3","-m","flask","--app", "wm.py", "run", "--host=0.0.0.0"]
