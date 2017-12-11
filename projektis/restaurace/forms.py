from django import forms
from .models import Restaurant, Dish

class SearchFormRestaurant(forms.Form):
    searchString= forms.CharField(max_length=50, label='Search string')
    searchByName= forms.BooleanField(required=False, label='Search by name', initial=True)

class SearchFormDish(forms.Form):
    searchString= forms.CharField(max_length=50, label='Search string')
    limitPrice= forms.BooleanField(required=False, label='Limit Price')
    price_from= forms.IntegerField(label='from', required=False, initial=0)
    price_to= forms.IntegerField(label='to', required=False, initial=0)

class EditFormRestaurant(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ['dishes']
