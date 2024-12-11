from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("we work out!")


def febuary(request):
    return HttpResponse("we eat out!")


def march(request):
    return HttpResponse("we run!")


def april(request):
    return HttpResponse("we meditate!")
