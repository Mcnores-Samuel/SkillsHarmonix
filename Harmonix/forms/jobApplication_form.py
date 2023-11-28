from ..models.Job_application import JobApplication
from django import forms


class JobApplicationForm(forms.Form):
    """Job application form.
    This class is used to display the job application model
    in the admin site.
    """
    # date_submitted = models.DateTimeField(default=timezone.now)
    # applicant = models.ForeignKey(ProfessionalProfile,
    #                               on_delete=models.CASCADE)
    # job = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # address = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    # country = models.CharField(max_length=50, null=True, blank=True)
    # resume = models.FileField(upload_to='Professional/resumes/')
    # cover_letter = models.TextField()
    # phone = models.CharField(max_length=50)
    # email = models.CharField(max_length=100)
    pass