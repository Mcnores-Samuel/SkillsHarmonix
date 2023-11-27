"""This is the admin site for the job listing model.
This class is used to display the job listing model
in the admin site.
"""
from django.contrib import admin


class JobListingAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'location', 'date_posted', 'deadline')
    search_fields = ('company', 'title', 'location', 'category')
