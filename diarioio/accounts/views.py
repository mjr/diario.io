from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import login
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from .models import PasswordReset
from .forms import RegistrationForm, EditAccountForm, PasswordResetForm
from .decorators import not_logged


User = get_user_model()

def custom_login(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return login(request)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def password_reset(request):
    form = PasswordResetForm(request.POST or None)
    success = False
    if form.is_valid():
        form.save()
        success = True
    return render(request, 'accounts_password_reset.html', {'form': form, 'success': success})

def password_reset_confirm(request, key):
    success = False
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        success = True
    return render(request, 'accounts_password_reset_confirm.html', {'form': form, 'success': success})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def edit(request):
    success = False
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            success = True
    else:
        form = EditAccountForm(instance=request.user)
    return render(request, 'accounts.html', {'form': form, 'success': success})

@login_required
def edit_password(request):
    success = False
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            form = PasswordChangeForm(user=request.user)
            success = True
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts_password.html', {'form': form, 'success': success})
