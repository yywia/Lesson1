from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def recent_news(request):
    return HttpResponse('Recent news')

def search_news(request):
    return HttpResponse('Search news')

def hot_news(request):
    return HttpResponse('Hot News!!!')