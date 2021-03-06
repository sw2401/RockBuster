import datetime
from django.db import models
from django.utils import timezone


# Django creates a primary key (pk) starting with #1
class Movie(models.Model):
    director = models.CharField(max_length=250)   #Column in table
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    availability = models.CharField(max_length=4, null=True)
    year = models.IntegerField(null=True)
    rating = models.CharField(max_length=6, null=True)
    date_purchased = models.CharField(max_length=10)   # current date when added to db

    def __str__(self):
        return self.title

class TvShow(models.Model):
    season = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    director = models.CharField(max_length=250)   #Column in table
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.CharField(max_length=4)
    year = models.IntegerField()
    rating = models.CharField(max_length=6)
    date_purchased = models.CharField(max_length=10)   # current date when added to db

class Game(models.Model):
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.CharField(max_length=4)
    year = models.IntegerField()
    rating = models.CharField(max_length=6)
    date_purchased = models.CharField(max_length=10)   # current date when added to db
    platform = models.CharField(max_length=100)

class RockBuster(models.Model):
    ceo = models.CharField(max_length=250)
    location = models.CharField(max_length=500)
    totalMovies = models.IntegerField()
    totalGames = models.IntegerField()
    totalShows = models.IntegerField()
    hours = models.CharField(max_length=500)

class Renter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)

class Rentals(models.Model):
    renterId = models.ForeignKey(Renter, on_delete=models.CASCADE)
    startDate = models.DateField()
    dueDate = models.DateField()
    returnDate = models.DateField()
    prodId = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Scenes(models.Model):
    scene = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actors = models.CharField(max_length=250)

