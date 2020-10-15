from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm

# Create your views here.
def homePage(request):
    asias = Asia.objects.all()
    americas = America.objects.all()
    africas = Africa.objects.all()
    europes = Europe.objects.all()

    context = {'asias' : asias, 'americas': americas, 'africas' : africas, 'europes' : europes}
    return render(request, 'django_app/home.html', context)

def registerPage(request):
    form = CreateUserForm()


    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('login')

    context = {'form' : form}

    return render(request, 'django_app/register.html', context)

def loginPage(request):
    context = {}

    return render(request, 'django_app/login.html', context)