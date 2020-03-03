from django.shortcuts import render


def home_page(request):
    return render(request, 'index_test.html')
