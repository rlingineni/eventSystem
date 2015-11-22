from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'ems'

    def ready(self):
        import ems.signals