from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def who(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")