"""This file contains the views for the dashboard page."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.job_listings import JobListing
from ..models.business_profile import BusinessProfile
from ..models.professional_profile import ProfessionalProfile
from ..models.Job_application import JobApplication
from django.shortcuts import redirect
from django.contrib import messages
from .search_engine import search_engine
from django.db.models import Q


@login_required
def dashboard(request):
    """Render the dashboard page."""
    if request.user.is_authenticated and request.user.user_type == 'Business owner':
        user = request.user
        try:
            business = BusinessProfile.objects.get(representative=user)
            apps = JobApplication.objects.filter(
                job__company=business
            )
            data = JobListing.objects.filter(
                company=business
            )
            print(apps)
        except BusinessProfile.DoesNotExist:
            return redirect('business_profile')
        context = {
                'data': data,
                'apps': apps
            }
        return render(request, 'company_sites/dashboard.html', context)
    elif request.user.is_authenticated and request.user.user_type == 'Job seeker':
        data = JobListing.objects.all().order_by('-date_posted')
        pos = set(JobListing.objects.values_list('position', flat=True).distinct())
        categories = set(JobListing.objects.values_list('category', flat=True).distinct())
        locations = set(JobListing.objects.values_list('location', flat=True).distinct())
        recommended = []
        try:
            user = request.user
            professional = ProfessionalProfile.objects.get(jobseeker=user)
            skills = professional.skills.split(',')
            locations = professional.city
            recommended.append(JobListing.objects.filter(
                Q(position__icontains=skills) |
                Q(location__icontains=locations)
            ))
        except AttributeError:
            messages.info(request, 'Please create a professional profile to view recommended jobs')
            return redirect('professional_profile')
        if request.method == 'POST':
            data = search_engine(request)
        context = {
            'data': data,
            'recommended': recommended,
            'pos': pos,
            'categories': categories,
            'locations': locations
        }
        return render(request, 'jobseeker_sites/dashboard.html', context)
    return render(request, 'dashboard.html')