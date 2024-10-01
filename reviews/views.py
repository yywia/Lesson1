from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def text_reviews(request):
    return HttpResponse('cool review')

def celebrity_review(request):
    return HttpResponse('some cool guy review')

def tripadvisor_score(request):
    return HttpResponse('we are cool')