"""This is the admin site for the feedback model.
This class is used to display the feedback model
in the admin site.
"""
from django.contrib import admin


class FeedbackAdmin(admin.ModelAdmin):
    """Feedback admin.
    This class is used to display the feedback model
    in the admin site.
    """
    list_display = ('user', 'email', 'feedback_type', 'message')
    search_fields = ('user', 'email', 'feedback_type', 'message')