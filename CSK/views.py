from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse ('<h1> Dhonit is caption of csk</h1>')
