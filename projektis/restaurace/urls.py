from django.urls import path

from . import views

app_name='restaurace'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_restaurant>/', views.resInfo, name='resInfo'),
    path('dishes/', views.dishIndex, name='dishIndex'),
    path('dishes/<int:id_dish>/', views.dishInfo, name='dishInfo'),
    path('dishes/byType/<int:id_dishType>/', views.dishByType, name='dishByType'),
]
