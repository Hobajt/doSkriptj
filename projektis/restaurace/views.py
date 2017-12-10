from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Restaurant, Review

def index(request):
    return render(request, 'restaurace/index.html')

def resInfo(request, id_restaurant):
    restaurant= get_object_or_404(Restaurant, pk=id_restaurant)
    return render(request, 'restaurace/resInfo.html', {'restaurant': restaurant})


