from django.apps import AppConfig
from django.db.models.signals import pre_save


class AuthConfig(AppConfig):
    name = 'django-hasura-auth'

    def ready(self):
        from . import signals
