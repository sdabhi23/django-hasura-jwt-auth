# Django JWT Auth Server

A simple containerized JWT based auth server written using Django, Djoser and Django Rest Framework

## Required environment variables

* **HASURA_GRAPHQL_ADMIN_SECRET**: The admin secret for your Hasura instance
* **GRAPHQL_URI**: The graphql endpoint of your Hasura instance
* **DJANGO_SUPERUSER_EMAIL**: Email addredd for the superuser account
* **DJANGO_SUPERUSER_USERNAME**: Username for the superuser account
* **DJANGO_SUPERUSER_PASSWORD**: Password for the superuser account

## Deployment instructions

Run container by pulling image from Docker Hub

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
