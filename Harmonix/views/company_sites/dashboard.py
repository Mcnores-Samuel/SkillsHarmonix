from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def business_dashboard(request):
    return render(request, 'company_sites/dashboard.html', {})