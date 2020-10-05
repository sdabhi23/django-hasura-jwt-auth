from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth.models import User
import requests
import os


@receiver(signals.post_save, sender=User)
def auth_signal(sender, **kwargs):
    if User.objects.count() > 1:
        user = kwargs['instance']
        print(user.id)
        print(user.username)
        headers = {
            "content-type": "application/json",
            "x-hasura-admin-secret": os.environ['HASURA_GRAPHQL_ADMIN_SECRET']
        }
        mutation = """mutation CreateUser($userId: Int!, $userName: String!) {
            insert_user(objects: {id: $userId, username: $userName}) {
                affected_rows
            }
        }
        """
        variables = {
            'userId': user.id,
            'userName': user.username
        }
        r = requests.post(os.environ['GRAPHQL_URI'], json={
                          'query': mutation, 'variables': variables, 'operationName': 'CreateUser'}, headers=headers)
        print(user.username)
        print(user.id)
        print(r.json())
        print("User registered!")
