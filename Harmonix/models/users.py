from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ("Business owner", "Business owner"),
    ("Job seeker", "Job seeker"),
)

class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True, null=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    user_type = models.ChoiceField(choices=USER_TYPE)
