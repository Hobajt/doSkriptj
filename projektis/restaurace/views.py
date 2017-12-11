from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Restaurant, Review, Dish, DishType

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



