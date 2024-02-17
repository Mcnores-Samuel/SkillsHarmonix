"""This module contains the sign up form class
allowing users to create accounts.
"""
from ..models.users import HarmonixUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    """Sign up form.
    This form is used to sign up users.
    Attributes:
        username: The username of the user.
        email: The email address of the user.
        password1: The password of the user.
        password2: The password confirmation of the
                     user.
    """
    email = forms.EmailField(
        max_length=100, required=True,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter your email address',
                   'class': 'form-control'}))
    username = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'form-control'}))
    register_interest = forms.ChoiceField(
        choices=[
                 ('Business owner', 'Business owner'),
                 ('Job seeker', 'Job seeker')],
        help_text='How would you describe your role or interests?',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control'}))
    
    class Meta:
        model = HarmonixUser
        fields = ('username', 'email', 'password1', 'password2', 'register_interest')