#!/usr/bin/env python3
from django.test import TestCase
from Harmonix.models.users import HarmonixUser

class TestUser(TestCase):
    """Test user model.
    This class contains all the unit tests for the user model.
    """
    def setUp(self):
        """Set up.
        This method is called before each test.
        """
        HarmonixUser.objects.create_user(email="mcnoressamuel@gmail.com",
                                 username="Samuel",
                                 password="password",
                                 user_type="Business owner")
        HarmonixUser.objects.create_user(email="fitsuminform@gmail.com",
                                 username="Fitsum",
                                 password="password",
                                 user_type="Job seeker")

    def test_user_creation(self):
        """Test user creation.
        This method tests the creation of a user.
        """
        user = HarmonixUser.objects.get(email="mcnoressamuel@gmail.com")
        self.assertEqual(user.username, "Samuel")
        self.assertEqual(user.user_type, "Business owner")
        user = HarmonixUser.objects.get(email="fitsuminform@gmail.com")
        self.assertEqual(user.username, "Fitsum")
        self.assertEqual(user.user_type, "Job seeker")

    def test_user_update(self):
        """Test user update.
        This method tests the update of a user.
        """
        user = HarmonixUser.objects.get(username="Samuel")
        user.username = "James"
        user.save()
        user = HarmonixUser.objects.get(username="James")
        self.assertEqual(user.username, "James")
        user = HarmonixUser.objects.get(username="Fitsum")
        user.username = "Mary"
        user.save()
        user = HarmonixUser.objects.get(username="Mary")
        self.assertEqual(user.username, "Mary")

    def test_user_deletion(self):
        """Test user deletion.
        This method tests the deletion of a user.
        """
        user = HarmonixUser.objects.get(username="Samuel")
        user.delete()
        user = HarmonixUser.objects.filter(username="Samuel")
        self.assertEqual(len(user), 0)
        user = HarmonixUser.objects.get(username="Fitsum")
        user.delete()
        user = HarmonixUser.objects.filter(username="Fitsum")
        self.assertEqual(len(user), 0)
    
    def test_user_id(self):
        """Test user id.
        This method tests the id of a user.
        """
        user = HarmonixUser.objects.get(username="Samuel")
        self.assertIsInstance(user.id, int)
        user = HarmonixUser.objects.get(username="Fitsum")
        self.assertIsInstance(user.id, int)