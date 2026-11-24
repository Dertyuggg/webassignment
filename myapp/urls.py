from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fashion/', views.fashion, name='fashion'),
    path('food/', views.food, name='food'),
    path('cinema/', views.cinema, name='cinema'),
    path('contact/', views.contact, name='contact'),
]
