from django.apps import AppConfig


class EduServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_service'

    # читай signals.py
    '''
    def ready(self):
        import edu_service.signals
    '''