from django.apps import AppConfig


class IsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'is_app'
    
    def ready(self) -> None:
        import is_app.signals
