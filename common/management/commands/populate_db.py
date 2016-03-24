from django.core.management.base import BaseCommand

from common.models import Injection, CRI
from common.dosage import DOSAGE_INJECTION, DOSAGE_CRI_SIMPLE, DOSAGE_CRI_ADVANCED, DOSAGE_CRI_OTHER


class Command(BaseCommand):
    help = 'Populates the db with data'

    @staticmethod
    def _parse_dict():
        for key, value in DOSAGE_INJECTION.items():
            inj, created = Injection.objects.update_or_create(name=key,
                                                              defaults={
                                                                  'factor': value[0],
                                                                  'concentration': value[1],
                                                                  'category': value[2],
                                                                  'admin': value[3],
                                                                  'desc': value[4]
                                                              })
            inj.save()

        for key, value in DOSAGE_CRI_SIMPLE.items():
            cri, created = CRI.objects.update_or_create(name=key,
                                                        defaults={
                                                            'rates': value[0],
                                                            'factor': value[1],
                                                            'concentration': value[2],
                                                            'category': value[3],
                                                            'calc_type': value[4],
                                                            'units': value[5],
                                                            'time': value[6],
                                                            'desc': value[7]
                                                        })
            cri.save()

        for key, value in DOSAGE_CRI_ADVANCED.items():
            cri_adv, created = CRI.objects.update_or_create(name=key,
                                                            defaults={
                                                                'recommended_rates': value[0],
                                                                'factor': value[1],
                                                                'concentration': value[2],
                                                                'category': value[3],
                                                                'calc_type': value[4],
                                                                'desc': value[5]
                                                            })

        CRI.objects.update_or_create(name='Insulin',
                                     defaults={
                                         'recommended_rates': DOSAGE_CRI_OTHER['Insulin'][0],
                                         'category': DOSAGE_CRI_OTHER['Insulin'][1],
                                         'desc': DOSAGE_CRI_OTHER['Insulin'][2]
                                     })

        CRI.objects.update_or_create(name='Metoclopramide',
                                     defaults={
                                         'recommended_rates': DOSAGE_CRI_OTHER['Metoclopramide'][0],
                                         'concentration': DOSAGE_CRI_OTHER['Metoclopramide'][1],
                                         'category': DOSAGE_CRI_OTHER['Metoclopramide'][2],
                                         'desc': DOSAGE_CRI_OTHER['Metoclopramide'][3]
                                     })

    def handle(self, *args, **options):
        self._parse_dict()
        print('db populated with rx')
