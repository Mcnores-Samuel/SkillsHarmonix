from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.job_listings import JobListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .search_engine import search_engine


def home_page(request):
    """This function is used to render the home page.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the home page.
        The home page contains a list of all job listings.

    Functionality:
        This function is used to render the home page.
        It also contains the search functionality.
    
    Note:
        The search functionality is implemented in the search_engine.py file.
        This function can be accessed by any user, whether they are authenticated or not.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    current_date = timezone.now()
    data = JobListing.objects.filter(deadline__gte=current_date).order_by('-date_posted')
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
