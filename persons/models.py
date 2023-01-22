from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class StudentMap(models.Model):
    """Модель с данными студента, связана с аккаунтом  User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

