from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def jobseeker_dashboard(request):
    user = request.user
    return render(request, 'jobseeker_sites/dashboard.html', {'user': user})