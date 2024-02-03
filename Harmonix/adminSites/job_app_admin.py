"""This is the admin site for the business profile model.
This class is used to display the business profile model
"""
from django.contrib import admin


class JobApplicationAdmin(admin.ModelAdmin):
    """Job application admin.
    This class is used to display the job application model
    in the admin site.
    """
    list_display = ('date_submitted', 'applicant', 'job', 'phone', 'email')
    search_fields = ('applicant', 'job', 'phone', 'email')