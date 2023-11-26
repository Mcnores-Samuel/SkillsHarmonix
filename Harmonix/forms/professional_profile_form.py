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
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    address = forms.CharField(max_length=255,
                                 widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(max_length=50,
                                    widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'state'}))
    country = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    zipcode = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Zipcode'}))
    phone = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    skills = forms.CharField(required=True,
                             widget=forms.Textarea(attrs={'placeholder': 'Skills e.g. programming, design, etc'}))
    bio = forms.CharField(required=True,
                          widget=forms.Textarea(attrs={'placeholder': 'Describe yourself'}))
    experience = forms.CharField(required=True,
                                 widget=forms.Textarea(attrs={'placeholder': 'Describe your experience'}))
    education = forms.CharField(required=True,
                                widget=forms.Textarea(attrs={'placeholder': 'Describe your education'}))
    resume = forms.FileField(required=False)
    portfolio = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Portfolio url'}))
    preferences = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Preferences e.g. full-time, part-time, etc'}))
    avatar = forms.ImageField(required=False,
                                 widget=forms.FileInput(attrs={'placeholder': 'Avatar'}))
    
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