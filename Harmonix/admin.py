from django.contrib import admin
from .adminSites.user_admin_ops import HarmonixUserAdmin
from .adminSites.businessProfile import BusinessProfileAdmin
from .adminSites.ProfessionalProfile import ProfessionalProfileAdmin
from .models.users import HarmonixUser
from .models.business_profile import BusinessProfile
from .models.professional_profile import ProfessionalProfile

admin.site.site_header = "SkillsHarmonix Administration"
admin.site.site_title = "SkillsHarmonix Administration"
admin.site.index_title = "SkillsHarmonix Administration"

admin.site.register(HarmonixUser, HarmonixUserAdmin)
admin.site.register(BusinessProfile, BusinessProfileAdmin)
admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)
