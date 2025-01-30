# File: bookings/views.py
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Booking successful!")
                return redirect('booking')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})
