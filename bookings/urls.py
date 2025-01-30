# File: bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking_view, name='booking'),
]
