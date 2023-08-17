FROM python:3.10-slim
ADD ./requirements.txt .
ADD ./manage.py .
RUN pip3  install -r requirements.txt

RUN mkdir ./djangoProjectNEW
ADD ./djangoProjectNEW /djangoProjectNEW

RUN mkdir ./login
ADD ./login /login

RUN mkdir ./manager
ADD ./manager /manager

USER user