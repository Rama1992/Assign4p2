from django.contrib import admin
from ehbapp.models import EventHall


class EventHallAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(EventHall, EventHallAdmin)
