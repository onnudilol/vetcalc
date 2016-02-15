from django.db import models
from django.utils.text import slugify


class Medication(models.Model):
    name = models.CharField(max_length=140, unique=True, default='')
    slug = models.SlugField(max_length=40, unique=True, default='')
    category = models.CharField(max_length=140, blank=True, default='')
    desc = models.TextField(blank=True, default='')

    class Meta:
        abstract = True
        ordering = ['category', 'name']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Injection(Medication):
    factor = models.FloatField(default=0.0)
    concentration = models.CharField(max_length=140, blank=True, default='')
    admin = models.CharField(max_length=140, blank=True, default='')
