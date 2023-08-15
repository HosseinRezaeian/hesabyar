from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def header(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated==False:
        redirect('login')
    return render(request, 'header.html')
# Create your views here.
