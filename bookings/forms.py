from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'date_in', 'date_out', 'number_of_guests']

    def clean(self):
        cleaned_data = super().clean()
        date_in = cleaned_data.get('date_in')
        date_out = cleaned_data.get('date_out')

        if date_in and date_out:
            if date_in >= date_out:
                self.add_error('date_out', "Check-out must be after check-in.")

        return cleaned_data
