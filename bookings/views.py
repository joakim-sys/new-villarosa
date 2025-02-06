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
                form.add_error(None, e.message)  # Attach error to the form
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_success.html', {'form': form})


def book_now(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, "Booking successful!")
                return redirect('booking')
            except ValidationError as e:
                form.add_error(None, e.message)  # Attach error to the form
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()

    return render(request, 'bookings/book_now.html', {'form': form})
