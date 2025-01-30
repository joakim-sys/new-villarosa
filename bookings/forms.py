# File: bookings/forms.py
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'guest_name', 'guest_email', 'check_in_date', 'check_out_date', 'number_of_guests']

    # Custom date field validation
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('check_in_date') and cleaned_data.get('check_out_date'):
            if cleaned_data['check_in_date'] >= cleaned_data['check_out_date']:
                self.add_error('check_out_date', "Check-out must be after check-in.")
