from django.contrib.auth.backends import ModelBackend
from .models import KitchenUser

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = KitchenUser.objects.get(email=username)
        except KitchenUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
