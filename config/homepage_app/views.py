from user_app.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from user_app.models import Tweet, TwitterUser
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home_view(request):
    tweets = Tweet.objects.all()
    return render(request, 'index.html', {'tweets': tweets})

# ----------------------------------------------------------------
# Account views --------------------------------------------------


def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            request,
            username=data['username'],
            password=data['password']
        )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = TwitterUser.objects.create_user(
            username=data['username'],
            password=data['password'],
        )
        login(request, user)
        return HttpResponseRedirect(
            request.GET.get('next', reverse('home')))
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# ----------------------------------------------------------------
