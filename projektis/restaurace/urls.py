from django.urls import path

from . import views

app_name='restaurace'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_restaurant>/', views.resInfo, name='resInfo'),
]
