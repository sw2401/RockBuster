from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('', views.index, name='index'),
    path('', views.nextPage, name='nextPage'),
    
]