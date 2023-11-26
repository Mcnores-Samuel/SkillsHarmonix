from ...forms.business_profile_form import BusinessProfileForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_business_profile(request):
    """This function is used to create a business profile.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the create business profile page.
    """
    if request.method == 'POST':
        user = request.user
        form = BusinessProfileForm(request.POST, request.FILES, user=user)
        if form.is_valid():
            bus_profile = form.process_profile()
            if bus_profile:
                return redirect(reverse('log_in'))
        else:
            messages.error(request, form.errors)
    else:
        form = BusinessProfileForm(user=request.user)
    return render(request, 'registers/create_business_profile.html',
                  {'form': form})
