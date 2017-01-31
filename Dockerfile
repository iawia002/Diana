FROM daocloud.io/library/python:2.7.13
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y gcc g++ python-software-properties libpq-dev git build-essential
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
