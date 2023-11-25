"""This file contains the sign up view,
which is used to registe-r a new user to the site.
"""
from ...forms.sign_up_form import SignUpForm
from django.shortcuts import render
from django_email_verification import send_email


def sign_up(request):
    """This function is used to register a new user to the site.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the sign up page.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            send_email(user)
            user.save()
            return render(request, 'registers/confirm_email.html', {'user': user})
        else:
            err = form.errors.as_data()
            return render(request, 'registers/sign_up.html', {'form': form, 'err': err})
    else:
        form = SignUpForm()
        return render(request, 'registers/sign_up.html', {'form': form})