from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def index(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'intro.html')

def industry(request):
    return render(request, 'industry.html')

def grow(request):
    return render(request, 'grow.html')

def train(request):
    return render(request, 'train.html')

def marketing(request):
    return render(request, 'marketing.html')

def shop(request):
    return render(request, 'shop.html')

def member(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # 導向到首頁

    context = {
        'form': form
    }

    return render(request, 'member.html', context)

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # 電子郵件內容樣板
            email_template = render_to_string(
                'accounts/signup_success_email.html',
                {'username': request.user.username}
            )


            return redirect('/register')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def base(request):
    return render(request, 'base.html')

def new(request):
    return render(request, 'new.html')