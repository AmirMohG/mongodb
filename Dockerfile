FROM hub.hamdocker.ir/library/python:3.12.3

WORKDIR /app

COPY . /app

RUN pip install pymongo

CMD [ "python", "connect_mongo.py" ]


