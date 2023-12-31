from ...models.job_listings import JobListing
from ...models.business_profile import BusinessProfile
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def job_listings(request):
    """This function is used to display all job listings.

    Args:
        request (HttpRequest): The request object used to pass state through the system.

    Returns:
        HttpResponse: The response object containing the job listings page.
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            business = BusinessProfile.objects.filter(representative=user).first()
            if business:
                job_listings = JobListing.objects.filter(company=business)

                paginator = Paginator(job_listings, 12)
                page_number = request.GET.get('page')
                try:
                    job_listings = paginator.page(page_number)
                except PageNotAnInteger:
                    job_listings = paginator.page(1)
                except EmptyPage:
                    job_listings = paginator.page(paginator.num_pages)

                return render(request, 'company_sites/job_listings.html',
                          {'job_listings': job_listings})
            else:
                return redirect(reverse('home_page'))