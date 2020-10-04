FROM python:3.7-alpine

COPY ./django-hasura-auth/ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["sh", "./run.sh"]