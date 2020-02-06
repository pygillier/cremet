from graphene import relay, ObjectType, Int as GrapheneInt, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import City, Venue


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        exclude = ('active', 'created_at', 'updated_at')
        filter_fields = ['slug']
        interfaces = (relay.Node, )

    venues_count = GrapheneInt()

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(active=True)

    def resolve_venues_count(instance, info, **kwargs):
        return instance.venues.count()


class VenueNode(DjangoObjectType):

    venue_label = String()

    class Meta:
        model = Venue
        exclude = ('active', 'created_at', 'updated_at')
        filter_fields = []
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(active=True, city__active=True)

    def resolve_venue_label(instance, info, **kwargs):
        return Venue.VenueType(instance.venue_type).label


class Query(ObjectType):
    city = relay.Node.Field(CityNode, slug=String())
    venue = relay.Node.Field(VenueNode)
    all_cities = DjangoFilterConnectionField(CityNode)
    all_venues = DjangoFilterConnectionField(VenueNode)
