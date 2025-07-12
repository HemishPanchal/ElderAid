from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"homepage.html")

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def special_view(request):
    return render(request, 'special.html')


