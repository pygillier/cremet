from django.test import TestCase
from venues.models import City, Venue


class CityTestCase(TestCase):

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

        Venue.objects.create(
            city=y,
            name="hidden-by-venue",
            active=False
        )

        Venue.objects.create(
            city=y,
            name="shown-by-venue",
            active=True
        )

    def test_city_slug(self):

        agartha = City.objects.get(name="Agartha")
        ys = City.objects.get(name="Ys Brittany")

        self.assertEquals(agartha.slug, "agartha")
        self.assertEquals(ys.slug, "ys-brittany")

    def test_venue_visibility(self):
        v1 = Venue.objects.get(name="hidden-by-city")
        v2 = Venue.objects.get(name="hidden-by-venue")
        v3 = Venue.objects.get(name="shown-by-venue")

        self.assertFalse(v1.is_visible)
        self.assertFalse(v2.is_visibl)
        self.assertTrue(v3.is_visible)
