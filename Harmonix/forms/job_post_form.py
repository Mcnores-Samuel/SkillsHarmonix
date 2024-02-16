"""This module contains the job post form.
This form is used to create a job post.
"""
from django import forms
from ..models.job_listings import JobListing
from ..models.business_profile import BusinessProfile
from ..models.users import HarmonixUser
from django.utils import timezone


class JobPostForm(forms.Form):
    """Job post form.
    This form is used to create a job post.
    Attributes:
        title: The title of the job post.
        position: The position of the job post.
        description: The description of the job post.
        roles: The roles of the job post.
        benefits: The benefits of the job post.
        qualifications: The qualifications of the job post.
        salary: The salary of the job post.
        location: The location of the job post.
        category: The category of the job post.
        contacts: The contacts of the job post.
        How_to_apply: How to apply to the job post.
    """
    title = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Job Title'}))
    deadline = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={'type': 'date'}))
    position = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Job position'}))
    salary = forms.CharField(
        max_length=50, required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Salary (optional)'}))
    location = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Location'}))
    category = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Category'}))
    contacts = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Contacts'}))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Job Description'}))
    roles = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Responsibilities' +\
                   ' or Roles (must be comma separated)'}))
    benefits = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Benefits' +\
                   ' (must be comma separated)'}))
    qualifications = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Qualifications or Requirements e.g.' +\
                ' 2 years experience, Bachelors' +\
                'Degree in Computer Science, etc.' +\
                ' (must be comma separated)'}))

    How_to_apply = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'How to apply'\
                + ' (must be comma separated)'}))
    cautions = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'any cautions or'\
                + ' warnings (must be comma separated)'}))

    def __init__(self, *args, **kwargs):
        """This method initializes the form.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.user = kwargs.pop('user', None)
        self.instance = kwargs.pop('instance', None)
        super(JobPostForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['title'].initial = self.instance.title
            self.fields['deadline'].initial = self.instance.deadline
            self.fields['position'].initial = self.instance.position
            self.fields['description'].initial = self.instance.description
            self.fields['roles'].initial = self.instance.roles
            self.fields['benefits'].initial = self.instance.benefits
            self.fields['qualifications'].initial = self.instance.qualifications
            self.fields['salary'].initial = self.instance.salary
            self.fields['location'].initial = self.instance.location
            self.fields['category'].initial = self.instance.category
            self.fields['contacts'].initial = self.instance.contacts
            self.fields['How_to_apply'].initial = self.instance.How_to_apply
            self.fields['cautions'].initial = self.instance.cautions

    def clean(self):
        """This method cleans the form.
        Returns:create_business_profile
            A cleaned form.
        """
        cleaned_data = super(JobPostForm, self).clean()
        return cleaned_data

    def process_job_post(self):
        """This method processes the job post.
        Returns:
            A job post.
        """
        company = BusinessProfile.objects.get(
            representative=HarmonixUser.objects.get(username=self.user.username))
        job_post = JobListing(
            company=company,
            date_posted=timezone.now(),
            deadline=self.cleaned_data['deadline'],
            title=self.cleaned_data['title'],
            position=self.cleaned_data['position'],
            description=self.cleaned_data['description'],
            roles=self.cleaned_data['roles'],
            benefits=self.cleaned_data['benefits'],
            qualifications=self.cleaned_data['qualifications'],
            salary=self.cleaned_data['salary'],
            location=self.cleaned_data['location'],
            category=self.cleaned_data['category'],
            contacts=self.cleaned_data['contacts'],
            How_to_apply=self.cleaned_data['How_to_apply'],
            cautions=self.cleaned_data['cautions'],
        )
        job_post.save()
        return job_post
