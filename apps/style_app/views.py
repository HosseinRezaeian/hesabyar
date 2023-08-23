from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from . import models


def header(request):
    nav_bar = models.NavigationBar.objects.all()
    return render(request, 'header.html', {'navBar': nav_bar})
# Create your views here.
