from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        characters.extend('!@#$%&*')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    length = int(request.GET.get('length', 12))

    thepassword = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'password.html', {'password': thepassword})
