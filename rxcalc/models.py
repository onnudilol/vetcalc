from django.db import models


class Medication(models.Model):
    name = models.CharField(max_length=140, unique=True, default='')
    factor = models.FloatField(default=0.0)
    concentration = models.CharField(max_length=140, blank=True, default='')
    category = models.CharField(max_length=140, blank=True, default='')
    admin = models.CharField(max_length=140, blank=True, default='')
    desc = models.TextField(blank=True, default='')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['category']
