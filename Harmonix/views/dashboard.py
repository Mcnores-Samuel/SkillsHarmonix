"""This file contains the views for the dashboard page."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.job_listings import JobListing
from ..models.business_profile import BusinessProfile
from ..models.Job_application import JobApplication
from django.shortcuts import redirect


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
        return render(request, 'jobseeker_sites/dashboard.html')
    return render(request, 'dashboard.html')