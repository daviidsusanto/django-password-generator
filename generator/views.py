from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLUMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length'))
    password = ''

    for i in range(length):
        password += random.choice(character)

    return render(request,'generator/password.html',{'password': password})

def about(request):
    return render(request,'generator/about.html')