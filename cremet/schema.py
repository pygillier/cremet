import graphene

from venues.schema import Query as venuesQuery


class Query(venuesQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
