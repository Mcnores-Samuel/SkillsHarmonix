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
        job_id = request.POST.get('job_id', None)
        job_instance = None
        job_post = None
        if job_id:
            job_instance = JobListing.objects.filter(id=job_id).first()
            if job_instance:
                job_instance.title = request.POST.get('title', None)
                job_instance.position = request.POST.get('position', None)
                job_instance.description = request.POST.get('description', None)
                if request.POST.get('deadline', None):
                    job_instance.deadline = request.POST.get('deadline', None)
                job_instance.working_time = request.POST.get('working_time', None)
                job_instance.working_location = request.POST.get('working_location', None)
                job_instance.skills = request.POST.get('skills', None)
                job_instance.experience = request.POST.get('experience', None)
                job_instance.education = request.POST.get('education', None)
                job_instance.roles = request.POST.get('roles', None)
                job_instance.benefits = request.POST.get('benefits', None)
                job_instance.qualifications = request.POST.get('qualifications', None)
                job_instance.salary = request.POST.get('salary', None)
                job_instance.location = request.POST.get('location', None)
                job_instance.category = request.POST.get('category', None)
                job_instance.contacts = request.POST.get('contacts', None)
                job_instance.how_to_apply = request.POST.get('how_to_apply', None)
                job_instance.cautions = request.POST.get('cautions', None)
                job_instance.save()
                messages.success(request, 'Job Post Updated successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Job Post not found.')
                return redirect('dashboard')
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
        form = JobPostForm(user=request.user)
    return render(request, 'registers/create_job_post.html',
                  {'form': form})