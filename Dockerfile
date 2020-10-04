FROM python:3.7-alpine

COPY ./tripmgmt/ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]