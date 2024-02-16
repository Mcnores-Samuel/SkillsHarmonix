"""This file contains the views for the dashboard page."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.job_listings import JobListing
from ..models.business_profile import BusinessProfile


@login_required
def dashboard(request):
    """Render the dashboard page."""
    if request.user.is_authenticated and request.user.user_type == 'Business owner':
        user = request.user
        business = BusinessProfile.objects.get(representative=user)
        data = JobListing.objects.filter(
            company=business
        )
        context = {
            'data': data,
        }
        return render(request, 'company_sites/dashboard.html', context)
    elif request.user.is_authenticated and request.user.user_type == 'Job seeker':
        return render(request, 'jobseeker_sites/dashboard.html')
    return render(request, 'dashboard.html')