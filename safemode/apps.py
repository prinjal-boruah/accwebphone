from django.apps import AppConfig


class SafemodeConfig(AppConfig):
    name = 'safemode'

    def ready(selfself):
        from . import signals