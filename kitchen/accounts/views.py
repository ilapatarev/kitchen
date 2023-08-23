from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

from .forms import UserRegistrationForm, UserLoginForm





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Use email as username
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or desired URL
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})

class HomeView(TemplateView):
    template_name = 'home.html'

def user_logout(request):
    logout(request)
    return redirect('home')