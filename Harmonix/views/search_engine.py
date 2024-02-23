"""This file contains the views for the search engine page."""
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.job_listings import JobListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def search_engine(request):
    """Render the search engine page."""
    data = JobListing.objects.all().order_by('-date_posted')
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
    return data