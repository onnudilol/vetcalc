from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from common.models import Prescription


class TxSheet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=140, default='')
    comment = models.TextField(
        default='')
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('view_tx_sheet', args=[self.id])

    def __str__(self):
        return self.name + ': ' + ((self.comment[:75] + '...') if len(self.comment) > 75 else self.comment)


class TxItem(models.Model):

    FREQ_CHOICES = (
        ('SID', 'SID'),
        ('BID', 'BID')
    )

    UNIT_CHOICES = (
        ('mL', 'mLs'),
        ('C', 'capsules'),
        ('T', 'tablets')
    )

    sheet = models.ForeignKey(TxSheet, on_delete=None, default=None)
    med = models.ForeignKey(Prescription, on_delete=None, default=None)
    dose = models.IntegerField(default=0)
    freq = models.CharField(max_length=5, choices=FREQ_CHOICES, default='')
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES, default='')
    instruction = models.TextField(default='')

    def output_instruction(self):
        frequency = ''

        if self.freq == 'SID':
            frequency = 'once a day'
        elif self.freq == 'BID':
            frequency = 'twice a day'

        self.instruction = 'Take {} {} of {} {}.'.format(self.dose, self.get_unit_display(), self.med, frequency)

    def get_absolute_url(self):
        return reverse('view_tx_sheet', args=[self.sheet.id])

    def save(self, *args, **kwargs):
        self.output_instruction()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.med.name
