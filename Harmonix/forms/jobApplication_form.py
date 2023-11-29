from typing import Any
from ..models.Job_application import JobApplication
from ..models.job_listings import JobListing
from django import forms
from django.utils import timezone


class JobApplicationForm(forms.Form):
    """Job application form.
    This class is used to display the job application model
    in the admin site.
    """
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    address = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Address e.g. 123 Main St.'})
            )
    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Current City or Town'})
            )
    state = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'State'})
            )
    country = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Country'})
            )
    resume = forms.FileField(
        widget=forms.FileInput(
            attrs={'class': 'form-control'})
            )
    cover_letter = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   "placeholder": "Write your cover letter here."})
            )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
        )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'})
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(JobApplicationForm, self).__init__(*args, **kwargs)

    def clean(self):
        """Clean form data.
        This method is used to clean the form data.
        """
        cleaned_data = super().clean()
        return cleaned_data
    
    def process_application(self, job_id):
        """Process application.
        This method is used to process the job application form.
        """
        job_to_apply = JobListing.objects.get(id=job_id)
        if JobApplication.objects.get(job=job_to_apply,
                                      first_name=self.cleaned_data['first_name'],
                                      last_name=self.cleaned_data['last_name']):
            return "Already applied"
        
        if self.user:
            user = JobApplication.objects.get(applicant=self.user)
            job_application = JobApplication(
                date_submitted=timezone.now(),
                applicant=user,
                job=job_to_apply,
                first_name=user.first_name,
                last_name=user.last_name,
                address=user.address,
                city=user.city,
                state=user.state,
                country=user.country,
                resume=user.resume,
                cover_letter=self.cleaned_data['cover_letter'],
                phone=user.phone,
                email=user.email,
                )
            job_application.save()
            return job_application
        elif not self.user:
            job_application = JobApplication(
                date_submitted=timezone.now(),
                job=job_to_apply,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                address=self.cleaned_data['address'],
                city=self.cleaned_data['city'],
                state=self.cleaned_data['state'],
                country=self.cleaned_data['country'],
                resume=self.cleaned_data['resume'],
                cover_letter=self.cleaned_data['cover_letter'],
                phone=self.cleaned_data['phone'],
                email=self.cleaned_data['email'],
                )
            job_application.save()
            return job_application
        return "Error"
