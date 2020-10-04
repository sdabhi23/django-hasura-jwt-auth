# Django JWT Auth Server

A simple containerized JWT based auth server for integration with Hasura GrphQL Engine written in Python using Django and Django Rest Framework

## Required environment variables

* **SECRET_KEY:** The signing key for all types of tokens
* **HASURA_GRAPHQL_ADMIN_SECRET:** The admin secret for your Hasura instance
* **GRAPHQL_URI:** The graphql endpoint of your Hasura instance
* **DJANGO_SUPERUSER_EMAIL:** Email addredd for the superuser account
* **DJANGO_SUPERUSER_USERNAME:** Username for the superuser account
* **DJANGO_SUPERUSER_PASSWORD:** Password for the superuser account

## Configuration for HGE

* HASURA_GRAPHQL_JWT_SECRET

    ```json
    {
        "type": "HS256",
        <!-- should be same as the SECRET_KEY set above -->
        "key": "3EK6FD+o0+c7tzBNVfjpMkNDi2yARAAKzQlk8O2IKoxQu4nF7EdAh8s3TwpHwrdWT6R",
        "claims_namespace_path": "$.hasura"
    }
    ```

## Important routes

### Register new user

* Method: POST
* Route: `/user/`
* Headers: NA
* Sample request body:

    ```json
    {
        "email": "test_user@example.com",
        "password": "test_user-psswd",
        "username": "testUser"
    }
    ```

* Sample response body:

    ```json
    {
        "email": "test_user@example.com",
        "password": "wjertu98vut985utp54uvuc0ufcpx9u90fug98cvy9g8yj89uxcuf0u",
        "username": "testUser"
    }
    ```

### Get JWT token

* Method: POST
* Route: `/token/`
* Headers: NA
* Sample request body:

    ```json
    {
        "password": "test_user-psswd",
        "username": "testUser"
    }
    ```

* Sample response body:

    ```json
    {
        "refresh": "eyJ0edfgtrhrhy1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMTg5NzAwNywianRpIjoiY2YwYzRiNzFkMmFiNDk0OWFlODJhMTRmZDQyMzA1YmMiLCJ1c2VyX2lkIjoxfQ.ucmW5dOCrHbDPxqQR2xgnNTSpQL6kAdVI00cAdM8G8Y",
        "access": "eyJ0edfgtrhrhy1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxODEwOTA3LCJqdGkiOiI0MzE1ODg5OTMzOTA0NjVmYjNiYWNlYmY2MzI2NWJiYyIsInVzZXJfaWQiOjF9.Dcb9yKTAnc7LFJAf35B3nZc46OZjokh7S0XfQ86s_50"
    }
    ```

### Refresh access token

* Method: POST
* Route: `/token/refresh/`
* Headers: NA
* Sample request body:

    ```json
    {
        "refresh": "eyJ0edfgtrhrhy1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMTg5NzAwNywianRpIjoiY2YwYzRiNzFkMmFiNDk0OWFlODJhMTRmZDQyMzA1YmMiLCJ1c2VyX2lkIjoxfQ.ucmW5dOCrHbDPxqQR2xgnNTSpQL6kAdVI00cAdM8G8Y"
    }
    ```

* Sample response body:

    ```json
    {
        "access": "eyJ0edfgtrhrhy1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxODEwOTA3LCJqdGkiOiI0MzE1ODg5OTMzOTA0NjVmYjNiYWNlYmY2MzI2NWJiYyIsInVzZXJfaWQiOjF9.Dcb9yKTAnc7LFJAf35B3nZc46OZjokh7S0XfQ86s_50"
    }
    ```

### Get user details

* Method: POST
* Route: `/token/refresh/`
* Headers:

    ```http
    Authorization: Bearer eyJ0edfgtrhrhy1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxODEwOTA3LCJqdGkiOiI0MzE1ODg5OTMzOTA0NjVmYjNiYWNlYmY2MzI2NWJiYyIsInVzZXJfaWQiOjF9.Dcb9yKTAnc7LFJAf35B3nZc46OZjokh7S0XfQ86s_50
    ```

* Sample request body: NA
* Sample response body:

    ```json
    {
        "id": 14086,
        "username": "testUser",
        "email": "test_user@example.com"
    }
    ```

## Deployment instructions

* Run container by pulling image from Docker Hub:

    ```bash
    ➜ docker run -p 8000:8000 --env-file dev.env django-hasura-jwt-auth
    ```

## Dev environment setup

* Install pipenv tool

    ```bash
    ➜ pip install pipenv
    ```

* Install dependencies using pipenv

    ```bash
    ➜ pipenv install
    ```

* Apply migrations

    ```bash
    ➜ pipenv run python manage.py migrate
    ```

* Create super user to acess the admin panel

    ```bash
    ➜ pipenv run python manage.py createsuperuser
    Username (leave blank to use 'shrey'): admin
    Email address: admin@example.com
    Password:
    Password (again):
    Superuser created successfully.
    ```

* Run the development server

    ```bash
    ➜ pipenv run python manage.py runserver
    ```
