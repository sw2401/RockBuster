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

    def getTitle(self):
        return self.title
    def getDirect(self):
        return self.director
    def getYear(self):
        return self.year
    def getGenre(self):
        return self.genre
    def getRate(self):
        return self.rating
    def getPrice(self):
        return self.price

class Renter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)


class Scenes(models.Model):
    scene = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actors = models.CharField(max_length=250)

