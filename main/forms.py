from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(required=False, max_length=100, label = 'Title')
    director = forms.CharField(required=False, max_length=100, label='Director')
    year = forms.CharField(required=False, max_length=4, label = 'Year')
    genre = forms.CharField(required=False, max_length=50, label = 'Genre')
    rating = forms.CharField(required=False, max_length=10, label = 'Rating')
    price = forms.CharField(required=False, max_length=10, label = 'Price')
