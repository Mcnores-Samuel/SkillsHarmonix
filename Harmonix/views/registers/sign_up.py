"""This file contains the sign up view,
which is used to registe-r a new user to the site.
"""
from Harmonix.forms.sign_up_form import SignUpForm
from django.shortcuts import render
from django_email_verification import send_email
from django.contrib import messages


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
            interest = form.cleaned_data['register_interest']
            user = form.save(commit=False)
            user.user_type = interest
            user.is_active = False
            send_email(user)
            user.save()
            messages.success(request, 'Account created successfully')
            return render(request, 'authentication/confirm_email.html', {'user': user})
        else:
            messages.error(request, 'Account creation failed')
            return render(request, 'registers/sign_up.html', {'form': form})
    form = SignUpForm()
    return render(request, 'registers/sign_up.html', {'form': form})