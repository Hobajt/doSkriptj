from django.urls import path

from . import views

app_name='restaurace'
urlpatterns = [
    path('', views.indexRestaurant, name='indexRestaurant'),
    path('dishes/', views.indexDish, name='indexDish'),
    path('dishes/types/', views.indexDishType, name='indexDishType'),

    path('<int:id_restaurant>/', views.infoRestaurant, name='infoRestaurant'),
    path('dishes/<int:id_dish>/', views.infoDish, name='infoDish'),
    path('review/<int:id_review>/', views.infoReview, name='infoReview'),
    path('dishes/types/<int:id_dishType>/', views.infoDishType, name='infoDishType'),

    path('search/', views.searchRestaurant, name='searchRestaurant'),
    path('dishes/search/', views.searchDish, name='searchDish'),

    path('edit/<int:id_restaurant>/', views.editRestaurant, name='editRestaurant'),
]
