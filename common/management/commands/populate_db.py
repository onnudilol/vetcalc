from django.core.management.base import BaseCommand

from common.models import Injection, CRI
from common.dosage import DOSAGE_INJECTION, DOSAGE_CRI_SIMPLE, DOSAGE_CRI_ADVANCED


class Command(BaseCommand):
    help = 'Populates the db with data'

    def _parse_dict(self):
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
            cri, created = CRI.objects.update_or_create(name=key,
                                                        defaults={
                                                            'recommended_rates': value[0],
                                                            'factor': value[1],
                                                            'concentration': value[2],
                                                            'category': value[3],
                                                            'calc_type': value[4],
                                                            'desc': value[5]
                                                        })

    def handle(self, *args, **options):
        self._parse_dict()
        print('db populated with rx')