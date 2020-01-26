import json

from graphene_django.utils.testing import GraphQLTestCase
from cremet.schema import schema
from venues.models import City, Venue


class VenueSchemaTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        a = City.objects.create(
            name="Agartha",
            active=False)
        y = City.objects.create(
            name="Ys Brittany",
            active=True)

        Venue.objects.create(
            city=a,
            name="hidden-by-city",
            active=True
        )

    def test_all_cities(self):
        response = self.query(
            """
            {
                allCities {
                    edges {
                        node {
                            id
                            slug
                        }
                    }
                }
            }
            """,
            op_name="allCities"
        )

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        self.assertIn('ys-brittany', content)
