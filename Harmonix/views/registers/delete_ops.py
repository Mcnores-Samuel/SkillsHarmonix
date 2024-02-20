"""This module contains the method to delete a data from the database."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from ...models.job_listings import JobListing


@login_required
def delete_job_list(request):
    """This method deletes a job list.
    Args:
        request: The full HTTP request object.
        job_id: The id of the job list to delete.
    Returns:
        A redirect to the dashboard page.
    """
    if request.method == 'POST' and request.user.user_type == 'Business owner':
        job_id = request.POST.get('job_id', None)
        job_instance = JobListing.objects.filter(id=job_id).first()
        if job_instance:
            job_instance.delete()
            messages.success(request, 'Job Post Deleted successfully.')
            return redirect('dashboard')
        messages.error(request, 'Job Post not found.')
        return redirect('dashboard')
    messages.error(request, 'You are not authorized to delete this job post.')
    return redirect('dashboard')