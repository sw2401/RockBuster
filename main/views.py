from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello, Welcome to RockBuster</h1>"+
     #                   "<h2>Taste the Dwayne</h2>")

     #This seperated the html files from the views
     #All the html pages should be created in main/templates/main
     return render(request, 'main/rb_index.html')