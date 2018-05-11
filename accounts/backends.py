from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseModelBackend

# User = get_user_model()
from .models import User


class ModelBackend(BaseModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                print(user)
                if user.check_password(password):
                    return user
            except User.DoesNotExist as e:
                print(e)
