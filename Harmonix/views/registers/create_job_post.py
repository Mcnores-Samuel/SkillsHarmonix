from Harmonix.forms.job_post_form import JobPostForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_job_post(request):
    """This method creates a job post.
    Args:
        request: The full HTTP request object.
    Returns:
        A redirect to the job post page.
    """
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.process_job_post()
            if job_post:
                messages.success(request, 'Job Post Created successfully.')
                return redirect('self_job_posts')
            else:
                messages.error(request, 'Job Post Creation failed.')
                messages.error(request, form.errors)
                return redirect('create_job_post')
    else:
        form = JobPostForm()
    return render(request, 'registers/create_job_post.html', {'form': form})