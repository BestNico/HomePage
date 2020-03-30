from django.shortcuts import render


def home_page(request):
    return render(request, 'homepage.html')

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
