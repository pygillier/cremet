from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import City


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        exclude = ('active', 'created_at', 'updated_at')
        filter_fields = []
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(active=True)


class Query(ObjectType):
    all_cities = DjangoFilterConnectionField(CityNode)
