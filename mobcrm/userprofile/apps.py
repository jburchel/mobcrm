from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofile'
    
    def ready(self):
        import userprofile.signals  # This line ensures that the signals are connected
