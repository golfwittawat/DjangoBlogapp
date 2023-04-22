from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    return HttpResponse('<h1>Hello World</h1>')
