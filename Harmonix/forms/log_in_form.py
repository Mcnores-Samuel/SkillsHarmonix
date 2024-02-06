"""This module contains the log in form class 
allowing users to log into their accounts.
"""
from django import forms

class LogInForm(forms.Form):
    """Log in form.
    This form is used to log in users.
    Attributes:
        email: The email address of the user.
        password: The password of the user.
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)