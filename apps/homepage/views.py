from django.shortcuts import render
from django.views.generic.base import View

class Home(View):
    """
    The homepage for personal.
    """
    def get(self, request):
        return render(request, 'homepage.html')
