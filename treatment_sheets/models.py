from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from common.models import Prescription


class TxSheet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=140)
    comment = models.TextField(max_length=300)

    def get_absolute_url(self):
        return reverse('view_tx_sheet', args=[self.id])

    @property
    def description(self):
        return self.name + ': ' + self.comment


class TxItem(models.Model):

    FREQ_CHOICES = (
        ('SID', 'SID'),
        ('BID', 'BID')
    )

    UNIT_CHOICES = (
        ('mL', 'mLs'),
        ('C', 'Capsules'),
        ('T', 'Tablets')
    )

    sheet = models.ForeignKey(TxSheet, on_delete=None)
    med = models.ForeignKey(Prescription)
    dose = models.IntegerField()
    freq = models.CharField(max_length=5, choices=FREQ_CHOICES)
    unit = models.CharField(max_length=5, choice=UNIT_CHOICES)
    instruction = models.TextField(default='')

    def output_instruction(self):
        frequency = ''

        if self.freq == 'SID':
            frequency = 'once a day'
        elif self.freq == 'BID':
            frequency = 'twice a day'

        self.instruction = 'Take {} of {} {}.'.format(self.dose, self.med, frequency)

    def save(self, *args, **kwargs):
        self.output_instruction()
        super().save(*args, **kwargs)
