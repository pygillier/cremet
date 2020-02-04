from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class CremetAdminConfig(AdminConfig):
    default_site = 'venues.admin.CremetAdminSite'


class VenuesConfig(AppConfig):
    name = 'venues'
