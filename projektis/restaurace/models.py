from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class DishType(models.Model):
    name= models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Dish(models.Model):
    type= models.ForeignKey(DishType, on_delete= models.CASCADE)
    name= models.CharField(max_length=100)
    basePrice= models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    dishes= models.ManyToManyField(Dish, through='DishInRestaurant', related_name="restaurants")
    contact= models.CharField(max_length=16)

    def __str__(self):
        return self.name + ' [' + self.city + ']'

class DishInRestaurant(models.Model):
    dish= models.ForeignKey(Dish, on_delete= models.CASCADE)
    restaurant= models.ForeignKey(Restaurant, on_delete= models.CASCADE)
    price= models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        if self.price <= 0:
            self.price= self.dish.basePrice
        super().save(*args, **kwargs)

    def __str__(self):
        return self.restaurant.__str__() + ' - ' + self.dish.name

class Review(models.Model):
    restaurant= models.ForeignKey(Restaurant, on_delete= models.CASCADE)
    stars= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])   
    comment= models.CharField(max_length=512)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant.name + ": " + self.ratingDescription()

    def ratingDescription(self):
        if self.stars <= 1:
            return "Poor"
        elif self.stars >= 4:
            return "Amazing"
        else:
            return "Average"
