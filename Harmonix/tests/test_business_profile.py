"""This file contains the test cases for the sign up view."""
from django.test import TestCase
from Harmonix.models.users import HarmonixUser
from Harmonix.models.business_profile import BusinessProfile


class TestBusinessProfile(TestCase):
    """This class contains the test cases for the sign up view."""
    def setUp(self):
        """This method sets up the test cases."""
        HarmonixUser.objects.create_user(email="mcnoressamuel@gmail.com",
                                 username="Samuel",
                                 password="password",
                                 user_type="Business owner")
        HarmonixUser.objects.create_user(email="fitsuminform@gmail.com",
                                 username="Fitsum",
                                 password="password",
                                 user_type="Job seeker")
        
    def test_business_profile_creation(self):
        """This method tests the creation of a business profile."""
        user = HarmonixUser.objects.get(email="mcnoressamuel@gmail.com")
        