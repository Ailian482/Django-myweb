from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponse


# create your views here
def index(request):
    return HttpResponse("Hello world. You're at the myapp index.")


def add(request):
    return HttpResponse("add ......")