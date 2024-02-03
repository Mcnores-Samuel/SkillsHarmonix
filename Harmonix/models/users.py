"""This file contains the user model, business profile model,
and professional profile model allowing users to
create accounts and profiles.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import (FileExtensionValidator, validate_email)


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, password=None, **extra_fields):
        """Create a new user profile

        Args:
            email (str): User email
            password (str, optional): User password. Defaults to None.
            **extra_fields: Extra fields to be added to the user profile

        Raises:
            ValueError: If email is not provided

        Returns:
            UserProfile: New user profile
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create a superuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


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
    USER_TYPE = (
        ("default", "default"),
        ("Business owner", "Business owner"),
        ("Job seeker", "Job seeker"),
        ("Admin", "Admin"),
    )
    email = models.EmailField(max_length=50, unique=True, validators=[validate_email])
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    user_type = models.CharField(max_length=25,
                                 choices=USER_TYPE, default='default')
    image = models.ImageField(upload_to='User/images/', null=True, blank=True,
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.email
