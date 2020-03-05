from django.shortcuts import redirect, render
from .forms import UserLoginForm, UserRegisterForm
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


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data.get('password'))
            new_user.save()
            login(request, new_user)
            return redirect("home:home_page")
        else:
            return HttpResponse("Error, please re-input")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("GET or POST")
