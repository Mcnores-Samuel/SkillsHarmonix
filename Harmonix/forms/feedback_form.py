from django import forms
from ..models.feedback import Feedback
from ..models.users import HarmonixUser
from django.utils import timezone


class FeedBackForm(forms.Form):
    """This class is used to create a feedback form"""
    TYPE = (
        ("Bug report", "Bug report"),
        ("Feature request", "Feature request"),
        ("general feedback", "general feedback"),
        ("complaint", "complaint"),
        ("other", "other")
    )
    user_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Please enter your name"})
            )
    email = forms.EmailField(required=False)
    feedback_type = forms.CharField(widget=forms.Select(choices=TYPE))
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Please enter your feedback here"})
            )
    priority = forms.IntegerField(
        required=False,
        widget=forms.Select(
            choices=[(i, i) for i in range(1, 6)]),
            help_text="Please select a priority for your feedback from 1 to 5.\
            1 being the lowest priority and 5 being the highest priority."
            )
    
    def __init__(self, *args, **kwargs):
        """This method is used to initialize the form"""
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        """This method is used to clean the form"""
        cleaned_data = super().clean()
        return cleaned_data
    
    def process_feedback(self):
        """This method is used to process the feedback"""
        if self.user:
            user = HarmonixUser.objects.get(username=self.user.username)
            feedback = Feedback(
                user=user,
                date=timezone.now(),
                user_name=user.first_name + " " + user.last_name,
                email=user.email,
                feedback_type=self.cleaned_data['feedback_type'],
                message=self.cleaned_data['message'],
                priority=self.cleaned_data['priority']
                )
        else:
            feedback = Feedback(
                date=timezone.now(),
                user_name=self.cleaned_data['user_name'],
                email=self.cleaned_data['email'],
                feedback_type=self.cleaned_data['feedback_type'],
                message=self.cleaned_data['message'],
                priority=self.cleaned_data['priority']
                )
        feedback.save()
        return feedback