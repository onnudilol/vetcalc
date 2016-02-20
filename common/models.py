from django.db import models
from django.utils.text import slugify

from jsonfield import JSONField


class Medication(models.Model):
    name = models.CharField(max_length=140, unique=True, default='')
    slug = models.SlugField(max_length=40, unique=True, default='')
    category = models.CharField(max_length=140, blank=True, default='')
    concentration = models.CharField(max_length=140, blank=True, default='')
    desc = models.TextField(blank=True, default='')
    factor = models.FloatField(default=0.0)

    class Meta:
        abstract = True
        ordering = ['category', 'name']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Injection(Medication):
    admin = models.CharField(max_length=140, blank=True, default='')


class CRI(Medication):
    SIMPLE = 'ez'
    ADVANCED = 'adv'
    CALC_TYPE_CHOICES = ((SIMPLE, 'Simple'), (ADVANCED, 'Advanced'))

    calc_type = models.CharField(max_length=3, choices=CALC_TYPE_CHOICES, default='')
    rates = JSONField()
    units = models.CharField(max_length=3, default='')
    time = models.CharField(max_length=3, default='')
