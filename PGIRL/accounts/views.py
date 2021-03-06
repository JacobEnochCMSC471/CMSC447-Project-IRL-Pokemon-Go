from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import resolve


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('register_success')

        elif len(form.errors) != 0:
            errors = form.errors
            return render(request, 'register_fail.html', {
        'errors': errors,
    })

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'register.html', args)


def edit_profile(request):
    if request.method == 'POST':
        print("Request :")
        print(request.POST)
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)


def register_success(request):
    return render(request, 'register_success.html')


def register_fail(request):
    return render(request, 'register_fail.html')
