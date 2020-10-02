# Django JWT Auth Server

A simple containerized JWT based auth server written using Django, Djoser and Django Rest Framework

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
