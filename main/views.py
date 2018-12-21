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


               # Title  double combo's
               #-------------------------------------------------------------------------------------------  
               #Search by TItle and Director
               if(title!='' and direct!='' and year=='' and genre=='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).count()
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
                         ti = title + ' and ' + direct + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle and Year
               if(title!='' and direct=='' and year!='' and genre=='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(year=year)
                    count = Movie.objects.filter(title__iexact=title).filter(year=year).count()
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
                         ti = title + ' and ' + year + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle and Genre
               if(title!='' and direct=='' and year=='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(genre__iexact=genre)
                    count = Movie.objects.filter(title__iexact=title).filter(genre__iexact=genre).count()
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
                         ti = title + ' and ' + genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle and Rating
               if(title!='' and direct=='' and year=='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(rating__iexact=rating)
                    count = Movie.objects.filter(title__iexact=title).filter(rating__iexact=rating).count()
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
                         ti = title + ' and ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle and Price
               if(title!='' and direct=='' and year=='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(price=price).count()
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
                         ti = title + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # Director combo:
               #---------------
               #Search by Director and year
               if(title=='' and direct!='' and year!='' and genre=='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).count()
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
                         ti = direct + ' and ' + year + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Director and Genre
               if(title=='' and direct!='' and year=='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(genre__iexact=genre)
                    count = Movie.objects.filter(director__iexact=direct).filter(genre__iexact=genre).count()
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
                         ti = direct + ' and ' + genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Director and Rating
               if(title=='' and direct!='' and year=='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(rating__iexact=rating)
                    count = Movie.objects.filter(director__iexact=direct).filter(rating__iexact=rating).count()
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
                         ti = direct + ' and ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

                #Search by Director and Price
               if(title=='' and direct!='' and year=='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(price=price)
                    count = Movie.objects.filter(director__iexact=direct).filter(price=price).count()
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
                         ti = direct + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # Year combo:
               #---------------
               #Search by year and Genre
               if(title=='' and direct=='' and year!='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(year=year).filter(genre__iexact=genre)
                    count = Movie.objects.filter(year=year).filter(genre__iexact=genre).count()
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
                         ti = year + ' and ' + genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by year and Rating
               if(title=='' and direct=='' and year!='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(year=year).filter(rating__iexact=rating)
                    count = Movie.objects.filter(year=year).filter(rating__iexact=rating).count()
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
                         ti = year + ' and ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by year and Price
               if(title=='' and direct=='' and year!='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(year=year).filter(price=price)
                    count = Movie.objects.filter(year=year).filter(price=price).count()
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
                         ti = year + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               #-------------------------------------------------------------------------------------------
               

               # Title  Triple combo's
               #-------------------------------------------------------------------------------------------  
               #Search by TItle, Director, year
               if(title!='' and direct!='' and year!='' and genre=='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).count()
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
                         ti = title + ' , ' + direct + ' ' + year + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

                #Search by TItle, Director, Genre
               if(title!='' and direct!='' and year=='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(genre__iexact=genre)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(genre__iexact=genre).count()
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
                         ti = title + ' , ' + direct + ' ' + genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle, Director, rating
               if(title!='' and direct!='' and year=='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(rating__iexact=rating)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(rating__iexact=rating).count()
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
                         ti = title + ' , ' + direct + ' ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               
               #Search by TItle, Director, price
               if(title!='' and direct!='' and year=='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(price=price).count()
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
                         ti = title + ' , ' + direct + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title, year, genre
               if(title!='' and direct=='' and year!='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(year=year).filter(genre__iexact=genre)
                    count = Movie.objects.filter(title__iexact=title).filter(year=year).filter(genre__iexact=genre).count()
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
                         ti = title + ' , ' + year + ' ' + genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title, year, rating
               if(title!='' and direct=='' and year!='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(year=year).filter(rating__iexact=rating)
                    count = Movie.objects.filter(title__iexact=title).filter(year=year).filter(rating__iexact=rating).count()
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
                         ti = title + ' , ' + year + ' ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title, year, price
               if(title!='' and direct=='' and year!='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(year=year).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(year=year).filter(price=price).count()
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
                         ti = title + ' , ' + year + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title, genre, rating
               if(title!='' and direct=='' and year=='' and genre!='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(genre__iexact=genre).filter(rating__iexact=rating)
                    count = Movie.objects.filter(title__iexact=title).filter(genre__iexact=genre).filter(rating__iexact=rating).count()
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
                         ti = title + ' , ' + genre + ' ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title, genre, price
               if(title!='' and direct=='' and year=='' and genre!='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(genre__iexact=genre).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(genre__iexact=genre).filter(price=price).count()
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
                         ti = title + ' , ' + genre + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

                #Search by Title, rating, price
               if(title!='' and direct=='' and year=='' and genre=='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(rating__iexact=rating) .filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(rating__iexact=rating) .filter(price=price).count()
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
                         ti = title + ' , ' + rating + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # Director
               #----------
                #Search by direct, year, genre
               if(title=='' and direct!='' and year!='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).count()
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
                         ti = direct + ' , ' + year + ' ' + genre + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by direct, year, rating
               if(title=='' and direct!='' and year!='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(rating__iexact=rating)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(rating__iexact=rating).count()
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
                         ti = direct + ' , ' + year + ' ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

                #Search by direct, year, price
               if(title=='' and direct!='' and year!='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(price=price)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(price=price).count()
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
                         ti = direct + ' , ' + year + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # year
               #-----
                #Search by year, genre, rating
               if(title=='' and direct=='' and year!='' and genre!='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating)
                    count = Movie.objects.filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).count()
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
                         ti = year + ' , ' + genre + ' ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by year, genre, price
               if(title=='' and direct=='' and year!='' and genre!='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(year=year).filter(genre__iexact=genre).filter(price=price)
                    count = Movie.objects.filter(year=year).filter(genre__iexact=genre).filter(price=price).count()
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
                         ti = year + ' , ' + genre + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # Genre
               #------
                #Search by genre, rating, price
               if(title=='' and direct=='' and year=='' and genre!='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = genre + ' , ' + rating + ' ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
                #------------------------------------------------------------------------------------------- 
               
               # Title  Quad combo's
               #-------------------------------------------------------------------------------------------  
               #Search by TItle, Director, year, and genre
               if(title!='' and direct!='' and year!='' and genre!='' and rating=='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' and ' + genre +' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               
               #Search by TItle, Director, year, and rating
               if(title!='' and direct!='' and year!='' and genre=='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(rating__iexact=rating)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(rating__iexact=rating).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' and ' + rating +' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle, Director, year, and price
               if(title!='' and direct!='' and year!='' and genre=='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(price=price).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' and ' + price +' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # Director
               #---------
               #Search by Director, year, genre and rating
               if(title=='' and direct!='' and year!='' and genre!='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).count()
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
                         ti = direct + ' , ' + year + ' , ' + genre + ' and ' + rating +' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Director, year, genre and price
               if(title=='' and direct!='' and year!='' and genre!='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(price=price)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(price=price).count()
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
                         ti = direct + ' , ' + year + ' , ' + genre + ' and ' + price +' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               # Director
               #---------
               #Search by year, genre, rating and price
               if(title=='' and direct=='' and year!='' and genre!='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = year + ' , ' + genre + ' , ' + rating + ' and ' + price +' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

                #-------------------------------------------------------------------------------------------  
               

               # Title  Five combo's
               #-------------------------------------------------------------------------------------------  
               #Search by TItle, Director, year, genre, and rating
               if(title!='' and direct!='' and year!='' and genre!='' and rating!='' and price==''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' , ' + genre + ' and ' + rating + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               
               #Search by Title , year, genre, rating and price
               if(title!='' and direct=='' and year!='' and genre!='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = title + ' , ' + year + ' , ' + genre + ' , ' + rating + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title , direct, genre, rating and price
               if(title!='' and direct!='' and year=='' and genre!='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = title + ' , ' + direct + ' , ' + genre + ' , ' + rating + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by Title , direct, year, rating and price
               if(title!='' and direct!='' and year!='' and genre=='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' , ' + rating + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Search by TItle, Director, year, genre, and price
               if(title!='' and direct!='' and year!='' and genre!='' and rating=='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(price=price).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' , ' + genre + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})

               #Director
               #--------
               #Search by Director, year, genre, rating and price
               if(title=='' and direct!='' and year!='' and genre!='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = direct + ' , ' + year + ' , ' + genre + ' , ' + rating + ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               #-------------------------------------------------------------------------------------------  

               # All six
               #-------------------------------------------------------------------------------------------  
               #Search by TItle, Director, year, genre, and rating
               if(title!='' and direct!='' and year!='' and genre!='' and rating!='' and price!=''):
               
                    mv = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price)
                    count = Movie.objects.filter(title__iexact=title).filter(director__iexact=direct).filter(year=year).filter(genre__iexact=genre).filter(rating__iexact=rating).filter(price=price).count()
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
                         ti = title + ' , ' + direct + ' , ' + year + ' , ' + genre + ' , ' + rating +  ' and ' + price + ' is not a valid selection'
                         return render (request, 'main/test.html', {'context':[ti]})
               #------------------------------------------------------------------------------------------- 

               '''
               .filter(title__iexact=title)  .filter(director__iexact=direct)   .filter(year=year)  
               .filter(genre__iexact=genre)  .filter(rating__iexact=rating)     .filter(price=price)
               '''

               #assert False
               return render (request, 'main/test.html', {'context':[ti, av]})
     else:
          form = SearchForm()
          if 'submitted' in request.GET:
               submitted = True
     return render(request, 'main/search.html', {'form': form, 'page_list': Movie.objects.all(), 'submitted': submitted})
