FROM python:3.7
WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000


RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
# update
RUN apt-get update -y
# install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/110.0.5481.77/chromedriver_linux64.zip &&\
	unzip chromedriver_linux64.zip chromedriver -d /usr/local/bin/

# install chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y

RUN python -m pip install --upgrade pip -i https://mirrors.bfsu.edu.cn/pypi/web/simple/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple/
COPY . .
CMD ["flask", "run"]