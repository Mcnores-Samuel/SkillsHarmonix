from ...forms.jobApplication_form import JobApplicationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages


def job_application_point(request, job_id):
    """This function is used to apply for a job.

    Args:
        request (HttpRequest): The request object used to pass state through the system.
        job_id (int): The id of the job to apply for.

    Returns:
        HttpResponse: The response object containing the job application page.
    """
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.process_application(job_id=int(job_id), user=request.user)
            if application == "Already applied":
                messages.error(request, "You have already applied for this job.")
                return redirect('home_page')
            elif application:
                messages.success(request, "You have successfully applied for this job.")
                return redirect('home_page')
            else:
                messages.error(request, "There was an error processing your application.")
        else:
            messages.error(request, form.errors)
    else:
        form = JobApplicationForm()
    return render(request, 'registers/job_application.html',
                  {'form': form, "user": request.user})