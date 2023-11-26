from typing import Any
from ..models.business_profile import BusinessProfile
from ..models.users import HarmonixUser
from django import forms
from django.utils import timezone


class BusinessProfileForm(forms.Form):
    """Business profile form.
    This form is used to create a business profile.
    Attributes:
        business_name: The name of the business.
        business_type: The type of the business.
        business_description: The description of the business.
        business_website: The website of the business.
        business_phone_number: The phone number of the business.
        business_address: The address of the business.
    """
    business_name = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Business Name'}))
    category = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Business Type'}))
    address = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Address(Street)'}))
    city = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(max_length=100, required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'State'}))
    country = forms.CharField(max_length=100, required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    zipcode = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Zipcode'}))
    phone = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.CharField(max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    website = forms.CharField(max_length=100, required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Website url'}))
    description = forms.CharField(required=True,
                                    widget=forms.Textarea(attrs={'placeholder': 'Please describe your business'}))
    history = forms.CharField(required=True,
                                    widget=forms.Textarea(attrs={'placeholder': 'Please describe your business history'}))
    registration_number = forms.CharField(max_length=100, required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Registration Number'}))
    business_certificate = forms.FileField(required=False)
    logo = forms.ImageField(required=False,
                            widget=forms.FileInput(attrs={'placeholder': 'Business Logo'}))
    cover_photo = forms.ImageField(required=False,
                                   widget=forms.FileInput(attrs={'placeholder': 'Cover Photo'}))
    
    def __init__(self, *args, **kwargs):
        """This method initializes the form.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        """This method cleans the form.
        Returns:create_business_profile
            A cleaned form.
        """
        cleaned_data = super().clean()
        return cleaned_data
    
    def process_profile(self):
        """This method processes the profile.
        Returns:
            A business profile.
        """
        user = HarmonixUser.objects.get(id=self.user.id)
        user.user_type = 'Business owner'
        user.save()
        business_profile = BusinessProfile(
            created_at=timezone.now(),
            updated_at=timezone.now(),
            representative=self.user,
            business_name=self.cleaned_data['business_name'],
            category=self.cleaned_data['category'],
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            country=self.cleaned_data['country'],
            zipcode=self.cleaned_data['zipcode'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
            website=self.cleaned_data['website'],
            description=self.cleaned_data['description'],
            history=self.cleaned_data['history'],
            registration_number=self.cleaned_data['registration_number'],
            business_certificate=self.cleaned_data['business_certificate'],
            logo=self.cleaned_data['logo'],
            cover_photo=self.cleaned_data['cover_photo'],
        )
        business_profile.save()
        return business_profile
    