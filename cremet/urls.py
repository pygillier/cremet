"""cremet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .settings import DEBUG

from cremet.schema import schema
from venues.admin import admin_site

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin_site.urls),
    path('dj_admin/', admin.site.urls),
    path('graphql/', csrf_exempt(
        GraphQLView.as_view(graphiql=DEBUG, schema=schema))),
]
