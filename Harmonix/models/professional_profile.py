"""This module contains the professional profile model
allowing job seekers to create professional profiles.
"""
from django.db import models
from django.utils import timezone
from .users import HarmonixUser


class ProfessionalProfile(models.Model):
    """Professional profile model.
    This model is used to store professional profiles.
    The professional profile model is linked to the user model.
    This allows us to easily retrieve the professional profile of a user.

    Attributes:
        id: The id of the jobseeker.
        jobseeker: The user that represents the jobseeker.
        first_name: The first name of the jobseeker.
        last_name: The last name of the jobseeker.
        address: The address of the jobseeker.
        city: The city of the jobseeker.
        state: The state of the jobseeker.
        zip: The zip code of the jobseeker.
        phone: The phone number of the jobseeker.
        email: The email address of the jobseeker.
        skills: The skills of the jobseeker.
        bio: The bio of the jobseeker.
        experience: The experience of the jobseeker.
        education: The education of the jobseeker.
        resume: The resume of the jobseeker.
        portfolio: The portfolio of the jobseeker.
        preferences: The preferences of the jobseeker.
        verified: Whether or not the jobseeker is verified.
    """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    jobseeker = models.OneToOneField(HarmonixUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    skills = models.TextField()
    bio = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    resume = models.FileField(upload_to='Professional/resumes/',
                              null=True, blank=True)
    portfolio = models.CharField(max_length=255)
    preferences = models.TextField()
    verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='Professional/avatars/',
                               null=True, blank=True)

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.first_name + " " + self.last_name