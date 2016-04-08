from django.db import models
from django.utils.text import slugify

from jsonfield import JSONField


class Medication(models.Model):
    """
    Abstract base class for medication
    """

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
    """
    Inherits from :model:`common.Medication`.  admin field for injection admin route.
    """

    admin = models.CharField(max_length=140, blank=True, default='')


class CRI(Medication):
    """
    Inherits from :model:`common.Medication`.  Additional fields for complexity of calculation, rates, units.
    """

    SIMPLE = 'ez'
    ADVANCED = 'adv'
    CALC_TYPE_CHOICES = ((SIMPLE, 'Simple'), (ADVANCED, 'Advanced'))

    calc_type = models.CharField(max_length=3, choices=CALC_TYPE_CHOICES, default='')
    rates = JSONField()
    recommended_rates = models.CharField(max_length=10, default='')
    units = models.CharField(max_length=3, default='')
    time = models.CharField(max_length=3, default='')


class Prescription(Medication):
    """
    Inherits from :model:`common.Medication`.  client description for laymen.
    """

    client_desc = models.TextField(blank=True, default='')
