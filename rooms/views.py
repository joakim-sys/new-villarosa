from django.shortcuts import render

from django.views import  generic

class BookingView(generic.TemplateView):
    template_name = 'rooms/booking_page.html'
    