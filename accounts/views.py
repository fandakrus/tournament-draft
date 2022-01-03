from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    content = {'form': form}
    return render(request, 'accounts/register.html', content)


def index(request):
    return render(request, 'accounts/index.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

