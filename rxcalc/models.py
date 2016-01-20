from django.db import models


class Medication(models.Model):
    name = models.CharField(max_length=140, unique=True, default='')
    concentration = models.CharField(max_length=140, blank=True, default='')
    desc = models.TextField(blank=True, default='')

    def __str__(self):
        return str(self.name)

# TODO: create fields for rx name, dosage, description, move dosage calc to helper function