from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'home.html')

def passgen(request):
    char = list(string.ascii_lowercase)  # Start with lowercase letters

    length = int(request.GET.get('length', 12))  # Default length is 12

    if request.GET.get('Uppercase'):
        char.extend(list(string.ascii_uppercase))

    if request.GET.get('Digits'):
        char.extend(list(string.digits))

    if request.GET.get('Symbols'):
        char.extend(list(string.punctuation))

    password = ""
    for x in range(length):
        password += random.choice(char)

    return render(request, 'password.html', {'password': password})
