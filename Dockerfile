FROM ubuntu:latest

RUN apt-get update -y && apt-get install python python-pip -y


RUN mkdir /open-unicorn \
    && cd /open-unicorn \
    && python -m pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8888

CMD ["python", "/open-unicorn/app.py"]
