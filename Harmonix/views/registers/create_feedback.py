from ...forms.feedback_form import FeedBackForm
from django.shortcuts import render, redirect
from django.contrib import messages


def create_feedback(request):
    """This method creates a feedback.
    Args:
        request: The full HTTP request object.
    Returns:
        A redirect to the feedback page.
    """
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.process_feedback()
            if feedback:
                messages.success(request, 'Feedback Created successfully.')
                return redirect('create_feedback')
            else:
                messages.error(request, 'Feedback Creation failed.')
                messages.error(request, form.errors)
                return redirect('create_feedback')
    else:
        form = FeedBackForm()
    return render(request, 'registers/create_feedback.html', {'form': form, 'user': request.user})