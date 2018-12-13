from django.shortcuts import render
from django.http import HttpResponse
from main.models import Movie, Renter

# Create your views here.
def index(request):
     return render(request, 'main/index.html', {'content':['The Hangover', 'Todd Phillips', 2009, 'comedy', 'R', 3.99,]})
     #return render(request, 'main/index.html')