"""This file contains the log in view,
which is used to log in a user to the site.
"""
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from Harmonix.forms.log_in_form import LogInForm
from django.contrib import messages


def log_in(request):
    """This function is used to log in a user to the site.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the log in page.
    """
    user = None
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user and user.is_active:
                login(request, user)
                messages.success(request, 'Welcome back, ' + user.username + '!, ' + 'Logged in successfully')
                if user.user_type == 'Business owner':
                    return redirect('dashboard')
                elif user.user_type == 'Job seeker':
                    return redirect('dashboard')
                elif user.is_superuser:
                    return redirect('/admin/')
                else:
                    return redirect('home_page')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LogInForm()
    return render(request, 'registers/log_in.html', {'form': form, "user": request.user})