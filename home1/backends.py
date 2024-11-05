from django.contrib.auth.backends import ModelBackend
from home1.models import User_wedsite

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User_wedsite.objects.get(email=email)
            if user.check_password(password):
                return user
        except User_wedsite.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User_wedsite.objects.get(pk=user_id)
        except User_wedsite.DoesNotExist:
            return None
