from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ("Business owner", "Business owner"),
    ("Job seeker", "Job seeker"),
)

class User(AbstractUser):
    """Custom user model.
    The default Django user model is not flexible enough for our needs.
    We need to add a user_type field to the model, so we can distinguish
    between business owners and job seekers.

    Attributes:
        email: The user's email address.
        username: The user's username.
        first_name: The user's first name.
        last_name: The user's last name.
        user_type: The user's type. Either "Business owner" or "Job seeker".
    """
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.username
    

class BusinessProfile(models.Model):
    """Business profile model.
    This model is used to store business profiles.
    The business profile model is linked to the user model.
    This allows us to easily retrieve the business profile of a user.

    Attributes:
        representative: The user that represents the business.
        business_name: The name of the business.
        Name: The name of the representative.
        Address: The address of the business.
        City: The city of the business.
        State: The state of the business.
        Zip: The zip code of the business.
        Phone: The phone number of the business.
        Email: The email address of the business.
        Website: The website of the business.
        Description: The description of the business.
        history: The history of the business.
        verified: Whether or not the business is verified.
    """
    representative = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Website = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    history = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.business_name


class ProfessionalProfile(models.Model):
    """Professional profile model.
    This model is used to store professional profiles.
    The professional profile model is linked to the user model.
    This allows us to easily retrieve the professional profile of a user.

    Attributes:
        jobseeker: The user that represents the jobseeker.
        first_name: The first name of the jobseeker.
        last_name: The last name of the jobseeker.
        address: The address of the jobseeker.
        city: The city of the jobseeker.
        state: The state of the jobseeker.
        zip: The zip code of the jobseeker.
        phone: The phone number of the jobseeker.
        email: The email address of the jobseeker.
        skills: The skills of the jobseeker.
        bio: The bio of the jobseeker.
        experience: The experience of the jobseeker.
        education: The education of the jobseeker.
        resume: The resume of the jobseeker.
        portfolio: The portfolio of the jobseeker.
        preferences: The preferences of the jobseeker.
        verified: Whether or not the jobseeker is verified.
    """
    jobseeker = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    resume = models.FileField(upload_to='Professional/resumes/')
    portfolio = models.CharField(max_length=255)
    preferences = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='Professional/avatars/')

    class Meta:
        app_label = 'Harmonix'

    def __str__(self):
        return self.first_name + " " + self.last_name