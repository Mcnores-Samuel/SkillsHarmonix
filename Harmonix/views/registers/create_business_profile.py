from Harmonix.forms.business_profile_form import BusinessProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Harmonix.models import BusinessProfile


@login_required
def business_profile(request):
    """This function is used to create a business profile.
    or updates user business profile.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the create business profile page.
    """
    if request.method == 'POST':
        user = request.user
        business = BusinessProfile.objects.filter(representative=user).first()
        if business:
            form = BusinessProfileForm(request.POST, request.FILES,
                                       instance=business, user=user)
        else:
            form = BusinessProfileForm(request.POST, request.FILES, user=user)
        if form.is_valid():
            bus_profile = form.process_profile()
            if bus_profile:
                messages.success(request, 'Business profile created successfully.')
                form = BusinessProfileForm(instance=business, user=user)
                return redirect('business_profile')
        else:
            messages.error(request, form.errors)
    else:
        user = request.user
        business = BusinessProfile.objects.filter(representative=user).first()
        if business:
            form = BusinessProfileForm(instance=business, user=user)
        else:
            form = BusinessProfileForm(user=request.user)
    return render(request, 'registers/business_profile.html',
                  {'form': form, 'business': business})
