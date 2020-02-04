from django.contrib import admin
from .models import City, Venue


# AdminSite
class CremetAdminSite(admin.AdminSite):
    site_header = "Cremet"
    site_title = "Cremet administration"


admin_site = CremetAdminSite(name='cremet')


# Publishing actions
def make_city_active(modeladmin, request, queryset):
    queryset.update(active=True)


def make_city_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


make_city_active.short_description = "Mark selected cities as active"
make_city_inactive.short_description = "Mark selected cities as inactive"


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'venues', 'active')
    list_filter = ('active',)

    actions = [make_city_active, make_city_inactive]

    def venues(self, obj):
        return obj.venues.count()


class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'venue_type', 'active', 'status')
    list_filter = ('city', 'venue_type', 'active')

    def status(self, obj):
        print(obj)
        if obj.is_visible:
            return "Visible"
        elif not obj.city.active:
            return "Not visible (city)"
        elif not obj.active:
            return "Not visible"


# Register ModelAdmins
admin_site.register(City, CityAdmin)
admin_site.register(Venue, VenueAdmin)
