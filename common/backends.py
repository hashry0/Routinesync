from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
              user = User.objects.get(email = username)
        except ObjectDoesNotExist:
              return None
        else:
              if user.check_password(password):
                    return user
        return None