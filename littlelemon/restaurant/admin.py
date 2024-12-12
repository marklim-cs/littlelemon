from django.contrib import admin
from .models import Booking, Menu

class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_guests", "booking_date")

class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "inventory")

admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)