from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')   #pulls from html file

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):    #check if uppercase box is selected
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()?/.,'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length', 12)) #'length' references the select tag in html with name=length, 12 as default

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
