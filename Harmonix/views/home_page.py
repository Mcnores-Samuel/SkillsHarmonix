from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.job_listings import JobListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .search_engine import search_engine


def home_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    data = JobListing.objects.all().order_by('-date_posted')
    pos = set(JobListing.objects.values_list('position', flat=True).distinct())
    categories = set(JobListing.objects.values_list('category', flat=True).distinct())
    locations = set(JobListing.objects.values_list('location', flat=True).distinct())

    if request.method == 'POST':
        data = search_engine(request)
    
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
        'pos': pos,
        'categories': categories,
        'locations': locations
    }
    return render(request, 'index.html', context)
