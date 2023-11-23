"""This module contains the feedback model
allowing users to submit feedback.
"""
from django.db import models
from django.utils import timezone
from .users import HarmonixUser


TYPE = (
    ("Bug report", "Bug report"),
    ("Feature request", "Feature request"),
    ("general feedback", "general feedback"),
    ("complaint", "complaint"),
    ("other", "other")
)

class Feedback(models.Model):
    """Feedback model.
    This model is used to store feedback.
    The feedback model is linked to the user model.
    This allows us to easily retrieve the user that submitted the feedback.
    Attributes:
        user: The user that submitted the feedback.
        date: The date the feedback was submitted.
        first_name: The first name of the user.
        email: The email address of the user.
        type: The type of the feedback.
        message: The message of the feedback.
        priority: The priority of the feedback.
    """
    user = models.ForeignKey(HarmonixUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    feedback_type = models.CharField(max_length=20, choices=TYPE)
    message = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)

    class Meta:
        app_label = 'Harmonix'