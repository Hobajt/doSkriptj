from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Restaurant, Review, Dish, DishType
from .forms import SearchFormRestaurant, SearchFormDish, EditFormRestaurant

def indexRestaurant(request):
    restaurants = Restaurant.objects.all().order_by("name")
    return render(request, 'restaurace/indexRestaurant.html', {'restaurants': restaurants})

def indexDish(request):
    dishes= Dish.objects.all().order_by("name")
    return render(request, 'restaurace/indexDish.html', {'dishes': dishes})

def indexDishType(request):
    dt= DishType.objects.all().order_by("name")
    return render(request, 'restaurace/indexDishType.html', {'dTypes': dt})


def infoRestaurant(request, id_restaurant):
    restaurant= get_object_or_404(Restaurant, pk=id_restaurant)
    return render(request, 'restaurace/infoRestaurant.html', {'restaurant': restaurant})

def infoDish(request, id_dish):
    dish= get_object_or_404(Dish, pk=id_dish)
    return render(request, 'restaurace/infoDish.html', {'dish': dish})

def infoDishType(request, id_dishType):
    dishType= get_object_or_404(DishType, pk=id_dishType)
    return render(request, 'restaurace/infoDishType.html', {'dishType': dishType})

def infoReview(request, id_review):
    review= get_object_or_404(Review, pk=id_review)
    return render(request, 'restaurace/infoReview.html', {'review': review})


def searchRestaurant(request):
    if request.method == 'POST':
        form= SearchFormRestaurant(request.POST)
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
        form= SearchFormRestaurant()
    return render(request, 'restaurace/searchRestaurant.html', {'restaurants':res, 'form': form})

def searchDish(request):
    if request.method == 'POST':
        form= SearchFormDish(request.POST)
        if form.is_valid():
            searchString= form.cleaned_data['searchString']
            limitPrice= form.cleaned_data['limitPrice']
            priceFrom= form.cleaned_data['price_from']
            priceTo= form.cleaned_data['price_to']
            filters= {'name__icontains':searchString}
            if limitPrice == True:
                filters['basePrice__gte']= priceFrom
                filters['basePrice__lte']= priceTo

            dish= Dish.objects.filter(**filters)
        else:
            dish= None
    else:
        dish= None
        form= SearchFormDish()
    return render(request, 'restaurace/searchDish.html', {'dishes':dish, 'form': form})    


def editRestaurant(request, id_restaurant):
    res= get_object_or_404(Restaurant, pk=id_restaurant)
    if request.method == 'POST':
        form = EditFormRestaurant(request.POST, instance = res)
        if form.is_valid():
            res= form.save()
            return HttpResponseRedirect(reverse('restaurace:infoRestaurant', args=(res.id,)))
    else:
        form= EditFormRestaurant(instance= res)
    return render(request, 'restaurace/editRestaurant.html', {'form': form})



























    


