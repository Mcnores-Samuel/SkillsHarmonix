from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.job_listings import JobListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    data = JobListing.objects.all().order_by('-date_posted')
    pos = set(JobListing.objects.values_list('position', flat=True).distinct())
    categories = set(JobListing.objects.values_list('category', flat=True).distinct())
    locations = set(JobListing.objects.values_list('location', flat=True).distinct())

    if request.method == 'POST':
        query = request.POST.get('search_query')
        location = request.POST.get('location')
        category = request.POST.get('category')
        position = request.POST.get('position')
        if query:
            data = data.filter(
                Q(title__icontains=query) |
                Q(position__icontains=query) |
                Q(roles__icontains=query) |
                Q(location__icontains=query) |
                Q(category__icontains=query)
            ).distinct()
        if location:
            data = data.filter(location=location)
        if category:
            data = data.filter(category=category)
        if position:
            data = data.filter(position=position)
    
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
