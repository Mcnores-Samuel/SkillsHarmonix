from django.urls import path
from .views.registers import (sign_up, log_in, create_business_profile,
                              create_professional_profile)

urlpatterns = [
    path('sign_up/', sign_up.sign_up, name='sign_up'),
    path('log_in/', log_in.log_in, name='log_in'),
    path('register_business/',
         create_business_profile.create_business_profile,
         name='create_business_profile'),
    path('register_professional/',
         create_professional_profile.create_professional_profile,
         name='create_professional_profile'),
]