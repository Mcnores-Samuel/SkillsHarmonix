from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.job_listings import JobListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    data = JobListing.objects.all().order_by('-date_posted')
    paginator = Paginator(data, 12)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        'data': data,
    }
    return render(request, 'index.html', context)
