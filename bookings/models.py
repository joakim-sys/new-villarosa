# File: bookings/models.py
from django.db import models
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50)  # Example: Single, Double, Suite
    total_rooms = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField()
    date_in = models.DateField('Check In', null=True)
    date_out = models.DateField('Check Out', null=True)
    number_of_guests = models.IntegerField()

    # def clean(self):
    #     # Validate check-in before check-out
    #     if self.date_in and self.date_out:
    #         if self.date_in >= self.date_out:
    #             raise ValidationError("Check-out date must be after check-in date.")
    #
    #     # Check for overlapping bookings
    #     overlapping_bookings = Booking.objects.filter(
    #         date_in__lt=self.date_out,
    #         date_out__gt=self.date_in
    #     ).exclude(id=self.id).exists()
    #
    #     if overlapping_bookings:
    #         raise ValidationError("The room is already booked for these dates.")

    def __str__(self):
        return f"{self.guest_name} - {self.guest_email} ({self.date_in} to {self.date_out})"
