"""This file contains a module for job applications previews for business owners."""
from ...models.Job_application import JobApplication
from ...models.business_profile import BusinessProfile
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def job_applications(request):
    """Render the job applications page."""
    user = request.user
    time = timezone.now()
    business = BusinessProfile.objects.get(representative=user)
    apps = JobApplication.objects.filter(
        job__company=business,
        job__date_posted__lte=time,
        job__deadline__gte=time).order_by('-date_submitted')
    group_by_job = {}
    for app in apps:
        if app.job.title in group_by_job:
            group_by_job[app.job.title].append(app)
        else:
            group_by_job[app.job.title] = [app]
    context = {
        'apps': group_by_job
    }
    return render(request, 'company_sites/job_applications.html', context)