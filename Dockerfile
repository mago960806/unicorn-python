FROM ubuntu:latest

RUN apt-get update -y && apt-get install python python-pip -y

RUN cd /open-unicorn && pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "/open-unicorn/app.py"]
