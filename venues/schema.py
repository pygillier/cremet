from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import City, Venue


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        exclude = ('active', 'created_at', 'updated_at')
        filter_fields = []
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(active=True)


class VenueNode(DjangoObjectType):
    class Meta:
        model = Venue
        exclude = ('active', 'created_at', 'updated_at')
        filter_fields = []
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(active=True, city__active=True)


class Query(ObjectType):
    all_cities = DjangoFilterConnectionField(CityNode)
    all_venues = DjangoFilterConnectionField(VenueNode)
