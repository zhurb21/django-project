from django.shortcuts import render

from django.http import HttpResponse
from .models import *

# Create your views here.
def homePage(request):
    asias = Asia.objects.all()
    americas = America.objects.all()
    africas = Africa.objects.all()
    europes = Europe.objects.all()

    context = {'asias' : asias, 'americas': americas, 'africas' : africas, 'europes' : europes}
    return render(request, 'django_app/home.html', context)