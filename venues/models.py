from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ["name"]


class Venue(models.Model):

    class VenueType(models.TextChoices):
        FAST_FOOD = 'FF', _('Fast food')
        BISTRO = 'BI', _('Bistro')
        GASTRO = 'GA', _('Gastronomic')

    name = models.CharField(max_length=200)

    venue_type = models.CharField(
        max_length=2,
        choices=VenueType.choices,
        default=VenueType.BISTRO
    )
    delivery = models.BooleanField(default=False)
    take_away = models.BooleanField(default=False)

    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        related_name='venues'
    )

    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_visible(self):
        return (self.active and self.city.active)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
