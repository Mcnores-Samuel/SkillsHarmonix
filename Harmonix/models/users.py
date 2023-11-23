"""This file contains the user model, business profile model,
and professional profile model allowing users to
create accounts and profiles.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ("Business owner", "Business owner"),
    ("Job seeker", "Job seeker"),
)

class HarmonixUser(AbstractUser):
    """Custom user model.
    The default Django user model is not flexible enough for our needs.
    We need to add a user_type field to the model, so we can distinguish
    between business owners and job seekers.

    Attributes:
        id: The id of the user.
        email: The user's email address.
        username: The user's username.
        first_name: The user's first name.
        last_name: The user's last name.
        user_type: The user's type. Either "Business owner" or "Job seeker".
    """
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    user_type = models.CharField(max_length=25, choices=USER_TYPE, default='Job seeker')
    image = models.ImageField(upload_to='User/images/', null=True, blank=True)

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.username