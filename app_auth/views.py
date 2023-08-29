from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('profile')
    template_name = 'templates/app_auth/register.html'

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    return render(request, 'app_auth/register.html')

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})

