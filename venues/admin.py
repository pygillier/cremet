from django.contrib import admin
from .models import City, Venue


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue_type', 'active', 'visibility')

    def visibility(self, obj):
        if obj.is_visible():
            return "Visible"
        elif not obj.city.active:
            return "Not visible (city)"
        elif not obj.active:
            return "Not visible"
