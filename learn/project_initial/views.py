from django.http import HttpResponse
from django.shortcuts import render

def user(request):
    return HttpResponse("teste django")