from django.contrib import admin

# Register your models here.

from .models import Room, Profile, Department #Booking

admin.site.register(Room)
admin.site.register(Profile)
admin.site.register(Department)
#admin.site.register(Booking)