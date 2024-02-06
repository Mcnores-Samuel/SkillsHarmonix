"""This module contains the job listing model
allowing businesses to post job listings.
"""
from .business_profile import BusinessProfile
from django.db import models
from django.utils import timezone


class JobListing(models.Model):
    """Job listing model.
    This model is used to store job listings.
    The job listing model is linked to the business profile model.
    This allows us to easily retrieve the business profile of a job listing.

    Attributes:
        business: The business that posted the job listing.
        date_posted: The date the job listing was posted.
        deadline: The deadline of the job listing.
        title: The title of the job listing.
        description: The description of the job listing.
        requirements: The requirements of the job listing.
        benefits: The benefits of the job listing.
        salary: The salary of the job listing.
        location: The location of the job listing.
        category: The category of the job listing.
        contacts: The contacts of the job listing.
        How_to_apply: How to apply to the job listing.
    """
    company = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE,
                                null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    roles = models.TextField()
    benefits = models.TextField()
    qualifications = models.TextField()
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    contacts = models.CharField(max_length=255)
    How_to_apply = models.TextField()
    cautions = models.TextField()

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.title
