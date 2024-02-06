"""This module contains the sign up form class
allowing users to create accounts.
"""
from ..models.users import HarmonixUser
from django import forms

class SignUpForm(forms.Form):
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
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm password',
                   'class': 'form-control'}))
    register_interest = forms.ChoiceField(
        choices=[
                 ('Business owner', 'Business owner'),
                 ('Job seeker', 'Job seeker')],
        help_text='How would you describe your role or interests?',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control'}))
    
    def clean(self):
        """Clean method.
        This method is used to validate the form.
        Returns:
            The cleaned data.
        """
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords don't match. Please try again.")
        return cleaned_data
    
    def process_data(self):
        """Process data method.
        This method is used to process the form data.
        Returns:
            The user object.
        """
        user = HarmonixUser(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            user_type=self.cleaned_data['register_interest']
            )
        return user
    

