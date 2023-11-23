"""This module contains the sign up form class
allowing users to create accounts.
"""
from ..models.users import User
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
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    

