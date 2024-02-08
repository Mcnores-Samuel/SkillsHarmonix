"""This module contains the urls for all urls in the Harmonix app.
These urls are used to navigate to the different pages in the Harmonix app.
"""
from django.urls import path
from .views.home_page import home_page
from Harmonix.views.registers import (sign_up, log_in, log_out,
                              create_business_profile,
                              create_professional_profile,
                              create_job_post, create_feedback,
                              job_application_point)
from Harmonix.views.general import job_listing
from .views import dashboard


urlpatterns = [
     path('', home_page, name='home_page'),
     path('dashboard/', dashboard.dashboard, name='dashboard'),
     # Paths for the registers in the Harmonix app.
     path('sign_up/', sign_up.sign_up, name='sign_up'),
     path('log_in/', log_in.log_in, name='log_in'),
     path('log_out/', log_out.log_out, name='log_out'),
     path('business_profile/',
          create_business_profile.business_profile,
          name='business_profile'),
     path('professional_profile/',
          create_professional_profile.professional_profile,
          name='professional_profile'),
     path('create_job_post/', create_job_post.create_job_post,
          name='create_job_post'),
     path('create_feedback/', create_feedback.create_feedback,
          name='create_feedback'),
     path('job_application/<int:job_id>/', job_application_point.job_application_point,
          name='job_application_point'),
     # Paths for the company sites in the Harmonix app.
     path('job_listings/', job_listing.job_listings, name='job_listings'),
]