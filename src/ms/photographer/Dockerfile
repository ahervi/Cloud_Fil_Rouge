FROM python:2.7
RUN pip install flask_cors pytest mongoengine flask connexion thrift
ADD . /app
WORKDIR /app
CMD ./photographer_service_main.py