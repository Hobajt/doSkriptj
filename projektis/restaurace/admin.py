from django.contrib import admin
from .models import Restaurant, Review, Dish, DishType, DishInRestaurant

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(DishInRestaurant)

