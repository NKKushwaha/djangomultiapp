from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return HttpResponse ('<h1>Rohit sharma is caption of MI</h1>')