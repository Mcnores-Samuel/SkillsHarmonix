from Harmonix.forms.job_post_form import JobPostForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ...models.job_listings import JobListing


@login_required
def create_job_post(request):
    """This method creates a job post.
    Args:
        request: The full HTTP request object.
    Returns:
        A redirect to the job post page.
    """
    if request.method == 'POST':
        job_listing = request.POST.get('job_listing_id', None)
        if job_listing:
            job_instance = JobListing.objects.filter(id=job_listing).first()
            form = JobPostForm(request.POST, user=request.user, instance=job_instance)
        else:
            form = JobPostForm(request.POST, user=request.user)
        if form.is_valid():
            job_post = form.process_job_post()
            if job_post:
                messages.success(request, 'Job Post Created successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Job Post Creation failed.')
                messages.error(request, form.errors)
                return redirect('create_job_post')
    else:
        job_instance = request.GET.get('job_listing_id', None)
        if job_instance:
            job = JobListing.objects.filter(id=job_instance).first()
            form = JobPostForm(instance=job, user=request.user)
        else:
            form = JobPostForm(user=request.user)
    return render(request, 'registers/create_job_post.html',
                  {'form': form, 'job_instance': job_instance})