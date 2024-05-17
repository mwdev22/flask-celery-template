FROM python:3.10-slim-buster

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN -d -p 6379:6379 redis

RUN flask db init
RUN flask db migrate
RUN flask db update

RUN chmod +x run.sh

CMD ["/bin/bash", "run.sh"]