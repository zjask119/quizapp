from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import Quiz
from users.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def get_user_profile(request):
    user = request.user
    quizes = Quiz.objects.filter(author=user)
    return render(request, 'users/profile.html', {"user": user, 'quizes': quizes})
