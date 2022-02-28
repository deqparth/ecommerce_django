from django.apps import AppConfig


class UseraccConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useracc'

    def ready(self):
        import useracc.signals
