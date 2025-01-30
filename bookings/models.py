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
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.IntegerField()

    def clean(self):
        # Validate that check-in is before check-out
        if self.check_in_date >= self.check_out_date:
            raise ValidationError("Check-out date must be after check-in date.")

        # Check room availability
        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            check_in_date__lt=self.check_out_date,
            check_out_date__gt=self.check_in_date
        ).exists()

        if overlapping_bookings:
            raise ValidationError("The room is already booked for these dates.")

    def __str__(self):
        return f"{self.guest_name} - {self.room.name} ({self.check_in_date} to {self.check_out_date})"
