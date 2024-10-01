from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return HttpResponse('Log in here')

def forget_password(request):
    return HttpResponse('Restore password page')

def register(request):
    return HttpResponse('Register page')