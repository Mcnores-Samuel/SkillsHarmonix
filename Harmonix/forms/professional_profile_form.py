from ..models.professional_profile import ProfessionalProfile
from ..models.users import HarmonixUser
from django import forms
from django.utils import timezone


class ProfessionalProfileForm(forms.Form):
    """Professional profile form.
    This form is used to create a professional profile.
    Attributes:
        first_name: The first name of the user.
        last_name: The last name of the user.
        address: The address of the user.
        city: The city of the user.
        state: The state of the user.
        country: The country of the user.
        resume: The resume of the user.
        phone: The phone number of the user.
        email: The email address of the user.
    """
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'placeholder': 'Avatar',
                   'class': 'form-control animated-section'}))
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'First Name', 
            'class': 'form-control animated-section'}))
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name', 
            'class': 'form-control animated-section'}))
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Address', 
            'class': 'form-control animated-section'}))
    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'City', 
            'class': 'form-control animated-section'}))
    state = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'state', 
            'class': 'form-control animated-section'}))
    country = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Country', 
            'class': 'form-control animated-section'}))
    zipcode = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Zipcode', 
            'class': 'form-control animated-section'}))
    phone = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone Number', 
            'class': 'form-control animated-section'}))
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Email',
                   'class': 'form-control animated-section'}))
    resume = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={'placeholder': 'Resume',
            'class': 'form-control animated-section'}))
    portfolio = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Portfolio url',
            'class': 'form-control animated-section'}))
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Skills e.g. programming, design, etc',
            'class': 'form-control animated-section',
            'rows': 3, 'cols': 20, 'style': 'resize:none;'}))
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Describe yourself',
            'class': 'form-control animated-section',
            'rows': 5, 'cols': 20, 'style': 'resize:none;'}))
    experience = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Describe your experience',
            'class': 'form-control animated-section',
            'rows': 5, 'cols': 20, 'style': 'resize:none;'}))
    education = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Describe your education',
            'class': 'form-control animated-section',
            'rows': 5, 'cols': 20, 'style': 'resize:none;'}))
    preferences = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Preferences e.g. full-time, part-time, etc',
            'class': 'form-control animated-section',
            'rows': 3, 'cols': 20, 'style': 'resize:none;'}))
    
    def __init__(self, *args, **kwargs):
        """This method initializes the form.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.user = kwargs.pop('user', None)
        self.professional = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if self.professional:
            self.fields['first_name'].initial = self.professional.first_name
            self.fields['last_name'].initial = self.professional.last_name
            self.fields['address'].initial = self.professional.address
            self.fields['city'].initial = self.professional.city
            self.fields['state'].initial = self.professional.state
            self.fields['country'].initial = self.professional.country
            self.fields['zipcode'].initial = self.professional.zipcode
            self.fields['phone'].initial = self.professional.phone
            self.fields['email'].initial = self.professional.email
            self.fields['skills'].initial = self.professional.skills
            self.fields['bio'].initial = self.professional.bio
            self.fields['experience'].initial = self.professional.experience
            self.fields['education'].initial = self.professional.education
            self.fields['resume'].initial = self.professional.resume
            self.fields['portfolio'].initial = self.professional.portfolio
            self.fields['preferences'].initial = self.professional.preferences
            self.fields['avatar'].initial = self.professional.avatar

    def clean(self):
        """This method cleans the form.
        Returns:
            A cleaned form.
        """
        cleaned_data = super().clean()
        return cleaned_data
    
    def process_profile(self):
        """This method processes the profile.
        Returns:
            A professional profile.
        """
        user = HarmonixUser.objects.get(id=self.user.id)
        user.user_type = 'Job seeker'
        user.save()
        pro_profile = ProfessionalProfile(
            created_at=timezone.now(),
            updated_at=timezone.now(),
            jobseeker=self.user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            country=self.cleaned_data['country'],
            zipcode=self.cleaned_data['zipcode'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
            skills=self.cleaned_data['skills'],
            bio=self.cleaned_data['bio'],
            experience=self.cleaned_data['experience'],
            education=self.cleaned_data['education'],
            resume=self.cleaned_data['resume'],
            portfolio=self.cleaned_data['portfolio'],
            preferences=self.cleaned_data['preferences'],
            avatar=self.cleaned_data['avatar'],
        )
        pro_profile.save()
        return pro_profile