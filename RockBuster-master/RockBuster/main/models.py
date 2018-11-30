from django.db import models


# Django creates a primary key (pk) starting with #1
class Movie(models.Model):
    director = models.CharField(max_length=250)   #Column in table
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    

class Scenes(models.Model):
    scene = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actors = models.CharField(max_length=250)

