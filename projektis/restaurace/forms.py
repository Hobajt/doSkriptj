from django import forms
from .models import Restaurant, Dish

class RestaurantSearchForm(forms.Form):
    searchString= forms.CharField(max_length=50, label='Search string')
    searchByName= forms.BooleanField(required=False, label='Search by name')
