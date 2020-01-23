from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"
        ordering = ["name"]
