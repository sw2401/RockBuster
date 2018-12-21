from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist  # form try exections

from main.models import Movie, Renter
from main.forms import SearchForm

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello, Welcome to RockBuster</h1>"+
     #                   "<h2>Taste the Dwayne</h2>")

     #This seperated the html files from the views
     #All the html pages should be created in main/templates/main
     #return render(request, 'main/index.html')
     mv = Movie.objects.get(title='The Hangover')
     ti = mv.title
     av = mv.availability
     #context = {
     #     'title': mv.title
     #}
     return render (request, 'main/index.html')
     #return render (request, 'main/test.html', {'context':[ti, av]})

def nextPage(request):
     mv = Movie.objects.filter(title = 'The Hangover')
     context = {
          'title': mv.title
     }
     return render (request, 'main/test.html', {'context'})

def search(request):
     submitted = False
     if request.method == 'POST':
          form = SearchForm(request.POST)
          if form.is_valid():
               #Get all data from the web form
               #-------------------------------------------------------------------------------------------
               #cd = form.cleaned_data
               title = form.cleaned_data['title']
               direct = form.cleaned_data['director']
               year = form.cleaned_data['year']
               genre = form.cleaned_data['genre']
               rating = form.cleaned_data['rating']
               price = form.cleaned_data['price']
               #-------------------------------------------------------------------------------------------
              
               if(title=='' and direct=='' and year=='' and genre=='' and rating=='' and price==''):
                    ti = 'Nothing was entered'
                    return render (request, 'main/test.html', {'context':[ti]})


               # Single value Searched
               #-------------------------------------------------------------------------------------------
               #Search by TItle
               if(title!='' and direct=='' and year=='' and genre=='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title)
                    count = Movie.objects.filter(title__iexact=title).count()
                    if(count == 3):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              ti3 = mv[2].title
                              av3 = mv[2].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2, ti3, av3]})
                    elif(count == 2):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2]})
                    elif(count == 1):
                         if(mv):
                              #mv = Movie.objects.get(title=title)
                              #mv = Movie.objects.filter(title=title)
                              ti = mv[0].title
                              av = mv[0].availability
                              return render (request, 'main/test.html', {'context':[ti, av]})
                    else:
                         ti = title + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Director
               if(title=='' and direct!='' and year=='' and genre=='' and rating=='' and price==''):
                    mv = Movie.objects.filter(director__iexact=direct)
                    count = Movie.objects.filter(director__iexact=direct).count()
                    if(count == 3):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              ti3 = mv[2].title
                              av3 = mv[2].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2, ti3, av3]})
                    elif(count == 2):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2]})
                    elif(count == 1):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              return render (request, 'main/test.html', {'context':[ti, av]})
                    else:
                         ti = direct + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Year
               if(title=='' and direct=='' and year!='' and genre=='' and rating=='' and price==''):
                    mv = Movie.objects.filter(year=year)
                    count = Movie.objects.filter(year=year).count()
                    if(count == 3):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              ti3 = mv[2].title
                              av3 = mv[2].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2, ti3, av3]})
                    elif(count == 2):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2]})
                    elif(count == 1):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              return render (request, 'main/test.html', {'context':[ti, av]})
                    else:
                         ti = year + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Genre
               if(title=='' and direct=='' and year=='' and genre!='' and rating=='' and price==''):
                    mv = Movie.objects.filter(genre__iexact=genre)
                    count = Movie.objects.filter(genre__iexact=genre).count()
                    if(count == 3):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              ti3 = mv[2].title
                              av3 = mv[2].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2, ti3, av3]})
                    elif(count == 2):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2]})
                    elif(count == 1):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              return render (request, 'main/test.html', {'context':[ti, av]})
                    else:
                         ti = genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Ratings
               if(title=='' and direct=='' and year=='' and genre=='' and rating!='' and price==''):
                    mv = Movie.objects.filter(rating__iexact=rating)
                    count = Movie.objects.filter(rating__iexact=rating).count()
                    if(count == 3):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              ti3 = mv[2].title
                              av3 = mv[2].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2, ti3, av3]})
                    elif(count == 2):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2]})
                    elif(count == 1):     
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              return render (request, 'main/test.html', {'context':[ti, av]})
                    else:
                         ti = rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               
               #Search by Price
               if(title=='' and direct=='' and year=='' and genre=='' and rating=='' and price!=''):
                    mv = Movie.objects.filter(price=price)
                    count = Movie.objects.filter(price=price).count()
                    if(count == 3):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              ti3 = mv[2].title
                              av3 = mv[2].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2, ti3, av3]})
                    elif(count == 2):
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              ti2 = mv[1].title
                              av2 = mv[1].availability
                              return render (request, 'main/test.html', {'context':[ti, av, ti2, av2]})
                    elif(count == 1):     
                         if(mv):
                              ti = mv[0].title
                              av = mv[0].availability
                              return render (request, 'main/test.html', {'context':[ti, av]})
                    else:
                         ti = price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               #-------------------------------------------------------------------------------------------
                 
               #assert False
               return render (request, 'main/test.html', {'context':[ti, av]})
     else:
          form = SearchForm()
          if 'submitted' in request.GET:
               submitted = True
     return render(request, 'main/search.html', {'form': form, 'page_list': Movie.objects.all(), 'submitted': submitted})
