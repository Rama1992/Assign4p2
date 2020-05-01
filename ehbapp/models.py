from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Profile
from EventHallBookingProject import settings


# Create your models here.
class EventHall(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.TextField()
    description = models.TextField(default="this is a event hall")
    phone_number = models.CharField(max_length=10)
    #is_reserved = models.NullBooleanField()


class Bookings(models.Model):
    booked_hall_id = models.ForeignKey(EventHall, on_delete=models.CASCADE)
    booked_on = models.DateTimeField()
