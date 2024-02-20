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
    working_time = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Working Time e.g. Full Time, Part Time, etc'}))
    working_location = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Working Location e.g. Onsite, Remote, etc'}))
    position = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Job position e.g. senior developer, etc'}))
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
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Skills you are looking for (optional)',
                   'rows': 3, 'cols': 40}))
    experience = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Experience you need (optional)',
                   'rows': 3, 'cols': 40}))
    education = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Education level you are looking for (optional)',
                   'rows': 3, 'cols': 40}))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Job Description',
                   'rows': 3, 'cols': 40}))
    roles = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Responsibilities' +\
                   ' or Roles (must be comma separated)',
                   'rows': 3, 'cols': 40}))
    benefits = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Benefits' +\
                   ' (must be comma separated)',
                   'rows': 3, 'cols': 40}))
    qualifications = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Qualifications or Requirements e.g.' +\
                ' 2 years experience, Bachelors' +\
                'Degree in Computer Science, etc.' +\
                ' (must be comma separated)',
                'rows': 3, 'cols': 40}))

    how_to_apply = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'How to apply'\
                + ' (must be comma separated)',
                   'rows': 3, 'cols': 40}))
    cautions = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'any cautions or'\
                + ' warnings (must be comma separated)',
                   'rows': 3, 'cols': 40}))

    def __init__(self, *args, **kwargs):
        """This method initializes the form.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.user = kwargs.pop('user', None)
        super(JobPostForm, self).__init__(*args, **kwargs)

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
            working_time=self.cleaned_data['working_time'],
            working_location=self.cleaned_data['working_location'],
            skills=self.cleaned_data['skills'],
            experience=self.cleaned_data['experience'],
            education=self.cleaned_data['education'],
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
            how_to_apply=self.cleaned_data['how_to_apply'],
            cautions=self.cleaned_data['cautions'],
        )
        job_post.save()
        return job_post
