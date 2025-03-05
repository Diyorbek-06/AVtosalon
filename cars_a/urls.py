from django.urls import path

from .views import home, cars_list, car_detail, car_create

urlpatterns = [
    path('', home, name='home' ),
    path('cars-list', cars_list, name='cars-list'),
    path('car/<int:pk>', car_detail, name='car-detail'),
    path('car-create', car_create, name='car-create')
]