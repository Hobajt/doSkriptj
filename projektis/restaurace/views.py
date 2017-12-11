from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Restaurant, Review, Dish, DishType
from .forms import RestaurantSearchForm

def index(request):
    restaurants = Restaurant.objects.all().order_by("name")
    return render(request, 'restaurace/index.html', {'restaurants': restaurants})

def resInfo(request, id_restaurant):
    restaurant= get_object_or_404(Restaurant, pk=id_restaurant)
    return render(request, 'restaurace/resInfo.html', {'restaurant': restaurant})

def dishIndex(request):
    dishes= Dish.objects.all().order_by("name")
    return render(request, 'restaurace/dishIndex.html', {'dishes': dishes})

def dishInfo(request, id_dish):
    dish= get_object_or_404(Dish, pk=id_dish)
    return render(request, 'restaurace/dishInfo.html', {'dish': dish})

def dishByType(request, id_dishType):
    dishType= get_object_or_404(DishType, pk=id_dishType)
    return render(request, 'restaurace/dishByType.html', {'dishType': dishType})

def reviewInfo(request, id_review):
    review= get_object_or_404(Review, pk=id_review)
    return render(request, 'restaurace/reviewInfo.html', {'review': review})

def restaurantSearch(request):
    if request.method == 'POST':
        form= RestaurantSearchForm(request.POST)
        if form.is_valid():
            searchString= form.cleaned_data['searchString']
            byName= form.cleaned_data['searchByName']
            if byName == True:
                res= Restaurant.objects.filter(name__icontains=searchString)
            else:
                res= Restaurant.objects.filter(city__icontains=searchString)
        else:
            res= None
    else:
        res= None
        form= RestaurantSearchForm()
    return render(request, 'restaurace/restaurantSearch.html', {'restaurants':res, 'form': form})

def dishSearch(request):
    



