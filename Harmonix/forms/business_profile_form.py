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
    logo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
            ))
    cover_photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    business_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Business Name',
            'class': 'form-control'})
            )
    category = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. Restaurant, Hotel, etc',
            'class': 'form-control'})
            )
    address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Address(Street)',
            'class': 'form-control'})
            )
    city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'City you are located in',
            'class': 'form-control'})
            )
    state = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'State you are located in',
            'class': 'form-control'})
            )
    country = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Country you are located in',
            'class': 'form-control'})
            )
    zipcode = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Zipcode',
            'class': 'form-control'})
            )
    phone = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone Number',
            'class': 'form-control'})
            )
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Email Address',
            'class': 'form-control'})
            )
    website = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Website url',
            'class': 'form-control'})
            )
    registration_number = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Registration Number',
            'class': 'form-control'})
            )
    business_certificate = forms.FileField(required=False)
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Please describe your business',
                   'class': 'form-control'}))
    history = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Please describe your business history',
                   'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        """This method initializes the form.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.user = kwargs.pop('user', None)
        self.business = kwargs.pop('instance', None)
        super(BusinessProfileForm, self).__init__(*args, **kwargs)
        if self.business:
            self.fields['business_name'].initial = self.business.business_name
            self.fields['category'].initial = self.business.category
            self.fields['address'].initial = self.business.address
            self.fields['city'].initial = self.business.city
            self.fields['state'].initial = self.business.state
            self.fields['country'].initial = self.business.country
            self.fields['zipcode'].initial = self.business.zipcode
            self.fields['phone'].initial = self.business.phone
            self.fields['email'].initial = self.business.email
            self.fields['website'].initial = self.business.website
            self.fields['description'].initial = self.business.description
            self.fields['history'].initial = self.business.history
            self.fields['registration_number'].initial = self.business.registration_number
            self.fields['business_certificate'].initial = self.business.business_certificate
            self.fields['logo'].initial = self.business.logo
            self.fields['cover_photo'].initial = self.business.cover_photo
    
    def clean(self):
        """This method cleans the form.
        Returns:create_business_profile
            A cleaned form.
        """
        cleaned_data = super(BusinessProfileForm, self).clean()
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
        if not self.business:
            business_profile.save()
        else:
            business_profile.id = self.business.id
            business_profile.save()
        return business_profile