from django.apps import AppConfig
#signals
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #users.py ichidagi malumotni yuklab olamiz
    def ready(self):
        import users.signals
