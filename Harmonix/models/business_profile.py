"""This module contains the business profile model
allowing businesses to create business profiles.
"""
from django.db import models
from django.utils import timezone
from .users import HarmonixUser


class BusinessProfile(models.Model):
    """Business profile model.
    This model is used to store business profiles.
    The business profile model is linked to the user model.
    This allows us to easily retrieve the business profile of a user.

    Attributes:
        id: The id of the business.
        representative: The user that represents the business.
        business_name: The name of the business.
        Address: The address of the business.
        City: The city of the business.
        State: The state of the business.
        Zip: The zip code of the business.
        Phone: The phone number of the business.
        Email: The email address of the business.
        Website: The website of the business.
        Description: The description of the business.
        history: The history of the business.
        verified: Whether or not the business is verified.
    """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    representative = models.ForeignKey(HarmonixUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=255, default='Other')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    description = models.TextField()
    history = models.TextField()
    verified = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=100,
                                           null=True, blank=True)
    business_certificate = models.FileField(upload_to='Business/certificates/',
                                            null=True, blank=True)
    logo = models.ImageField(upload_to='Business/logos/',
                             null=True, blank=True)
    cover_photo = models.ImageField(upload_to='Business/cover_photos/',
                                    null=True, blank=True)

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.business_name
