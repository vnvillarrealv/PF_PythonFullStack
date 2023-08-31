from django.apps import AppConfig


class DonacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donacion'

    def ready(self):
        from.tasks import start_task
        start_task()
        