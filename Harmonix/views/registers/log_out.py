from django.contrib.auth import logout
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required
def log_out(request):
    """The `sign_out` view function is responsible for handling user sign-out.
    """
    logout(request)
    return redirect(reverse('home_page'))
