from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('index', views.index, name="index"),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
