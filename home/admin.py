from venues.admin import admin_site
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group
from .models import User


class CremetUserAdmin(UserAdmin):
    pass


class CremetGroupAdmin(GroupAdmin):
    pass


admin_site.register(User, CremetUserAdmin)
admin_site.register(Group, CremetGroupAdmin)
