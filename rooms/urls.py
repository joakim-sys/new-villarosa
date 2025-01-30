from django.urls import path

from rooms.views import BookingView

urlpatterns = [

    path('',BookingView.as_view(),name='booking'),
]