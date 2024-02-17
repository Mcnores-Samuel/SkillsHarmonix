"""This module contains the job application model
allowing users to submit job applications.
"""
from django.db import models
from django.utils import timezone
from .job_listings import JobListing
from .professional_profile import ProfessionalProfile
from django.core.validators import (RegexValidator,
                                    FileExtensionValidator,
                                    validate_email)


class JobApplication(models.Model):
    """Job application model.
    This model is used to store job applications.
    The job application model is linked to the business profile model and the
    professional profile model.
    This allows us to easily retrieve the business profile and the professional
    profile of a job application.

    Attributes:
        date: The date the job application was submitted.
        applicant: The professional profile that submitted the job application.
        job: The business profile that posted the job listing.
        first_name: The first name of the applicant.
        last_name: The last name of the applicant.
        address: The address of the applicant.
        city: The city of the applicant.
        state: The state of the applicant.
        resume: The resume of the applicant.
        cover_letter: The cover letter of the applicant.
        phone: The phone number of the applicant.
        email: The email address of the applicant.
    """
    date_submitted = models.DateTimeField(default=timezone.now)
    applicant = models.ForeignKey(ProfessionalProfile,
                                  on_delete=models.CASCADE,
                                  null=True, blank=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True, blank=True)
    resume = models.FileField(upload_to='Professional/resumes/', 
                              validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])])
    cover_letter = models.TextField()
    phone = models.CharField(max_length=50, 
                             validators=[RegexValidator(
                                 regex=r'^\+?1?\d{9,15}$',
                                 message="Enter a valid phone number.")]
                                 )
    email = models.EmailField(
        max_length=100,
        validators=[validate_email])

    class Meta:
        app_label = 'Harmonix'
