from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm
from .models import KitchenUser, Profile



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create a profile for the new user
            Profile.objects.create(user=user)

            # Log in the user
            login(request, user)

            # Redirect to the user's profile page
            return redirect('home')
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


@login_required
def update_profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'account/update_profile.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'profile': profile})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        user = profile.user

        # Delete the profile
        profile.delete()
        user.delete()
        # Optionally, log out the user to prevent any authentication issues
        logout(request)

        # Redirect to the home page or any other page
        return redirect('home')

    return render(request, 'account/delete_profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        if new_password == confirm_new_password:
            if request.user.check_password(current_password):
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Your password has been changed.')
                return redirect('login')
            else:
                messages.error(request, 'Current password is incorrect.')
        else:
            messages.error(request, 'New passwords do not match.')

    return render(request, 'account/change_password.html')