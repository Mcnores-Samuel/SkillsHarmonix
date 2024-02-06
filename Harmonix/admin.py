from django.contrib import admin
from .adminSites.user_admin_ops import HarmonixUserAdmin
from .adminSites.businessProfile import BusinessProfileAdmin
from .adminSites.ProfessionalProfile import ProfessionalProfileAdmin
from .adminSites.job_app_admin import JobApplicationAdmin
from .adminSites.job_listing_admin import JobListingAdmin
from .adminSites.feedback_admin import FeedbackAdmin
from .models.users import HarmonixUser
from .models.business_profile import BusinessProfile
from .models.professional_profile import ProfessionalProfile
from .models.Job_application import JobApplication
from .models.job_listings import JobListing
from .models.feedback import Feedback

admin.site.site_header = "SkillsHarmonix Administration"
admin.site.site_title = "SkillsHarmonix Administration"
admin.site.index_title = "SkillsHarmonix Administration"

admin.site.register(HarmonixUser, HarmonixUserAdmin)
admin.site.register(BusinessProfile, BusinessProfileAdmin)
admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(JobListing, JobListingAdmin)
admin.site.register(Feedback, FeedbackAdmin)
