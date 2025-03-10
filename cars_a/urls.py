from collections import namedtuple

from django.urls import path

from .views import home, CarsList, CarDetail, CarCreate, CarUpdate, CarDelete, contact_form

urlpatterns = [
    path('', home, name='home' ),
    path('cars-list', CarsList.as_view(), name='cars-list'),
    path('car/<int:pk>', CarDetail.as_view(), name='car-detail'),
    path('car-create', CarCreate.as_view(), name='car-create'),
    path('car-update/<int:pk>/', CarUpdate.as_view(), name='car-update'),
    path('car-delete/<int:pk>/', CarDetail.as_view(), name='car-delete'),
    path('contact/', contact_form, name='contact')
]

