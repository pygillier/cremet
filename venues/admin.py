from django.contrib import admin
from .models import City, Venue


# Publishing actions
def make_city_active(modeladmin, request, queryset):
    queryset.update(active=True)


def make_city_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


make_city_active.short_description = "Mark selected cities as active"
make_city_inactive.short_description = "Mark selected cities as inactive"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'venues', 'active')
    list_filter = ('active',)

    actions = [make_city_active, make_city_inactive]

    def venues(self, obj):
        return obj.venues.count()


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'venue_type', 'active')
    list_filter = ('city', 'venue_type', 'active')

    def visibility(self, obj):
        if obj.is_visible():
            return "Visible"
        elif not obj.city.active:
            return "Not visible (city)"
        elif not obj.active:
            return "Not visible"
