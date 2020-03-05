from django.shortcuts import redirect, render
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("home:home_page")
            else:
                return HttpResponse("Error Username or password.")
        else:
            return HttpResponse("Invalid username or password.")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse('GET or POST')


def user_logout(request):
    logout(request)
    return redirect('home:home_page')
