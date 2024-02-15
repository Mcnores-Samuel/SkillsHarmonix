from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


def home_page(request):
    return render(request, 'index.html')
