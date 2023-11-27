"""This module contains the urls for all urls in the Harmonix app.
These urls are used to navigate to the different pages in the Harmonix app.
"""
from django.urls import path
from .views.registers import (sign_up, log_in, log_out,
                              create_business_profile,
                              create_professional_profile,
                              create_job_post)


urlpatterns = [
    # Paths for the registers in the Harmonix app.
    path('sign_up/', sign_up.sign_up, name='sign_up'),
    path('log_in/', log_in.log_in, name='log_in'),
    path('log_out/', log_out.log_out, name='log_out'),
    path('register_business/',
         create_business_profile.create_business_profile,
         name='create_business_profile'),
    path('register_professional/',
         create_professional_profile.create_professional_profile,
         name='create_professional_profile'),
     path('create_job_post/', create_job_post.create_job_post,
          name='create_job_post'),
]