from Harmonix.forms.professional_profile_form import ProfessionalProfileForm
from ...models.professional_profile import ProfessionalProfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def professional_profile(request):
    """This function is used to create a professional profile.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the create professional profile page.
    """
    user = request.user
    professional = ProfessionalProfile.objects.filter(jobseeker=user).first()
    if request.method == 'POST':
        form = ProfessionalProfileForm(request.POST, request.FILES,
                                       instance=professional, user=user)
        if form.is_valid():
            prof_profile = form.process_profile()
            if prof_profile:
                messages.success(request, 'Profile created successfully')
                return redirect('dashboard')
        else:
            messages.error(request, form.errors)
    else:
        form = ProfessionalProfileForm(user=request.user, instance=professional)
    return render(request, 'registers/professional_profile.html',
                  {'form': form})