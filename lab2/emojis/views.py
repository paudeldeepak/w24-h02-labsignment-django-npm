from django.shortcuts import render

from django.http import HttpResponse # Make sure to include this import

def index(request):
    return render(request, "index.html")

# Create your views here.
