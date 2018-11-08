from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, Welcome to RockBuster</h1>"+
                        "<h2>Taste the Dwayne</h2>")