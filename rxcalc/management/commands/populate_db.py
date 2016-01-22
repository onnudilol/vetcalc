from django.core.management.base import BaseCommand

from rxcalc.models import Medication
from rxcalc.dosage import DOSAGE_INJECTION


class Command(BaseCommand):
    help = 'Populates the db with data'

    def _parse_dict(self):
        for key, value in DOSAGE_INJECTION.items():
            Medication.objects.get_or_create(name=key,
                                             factor=value[0],
                                             concentration=value[1],
                                             category=value[2],
                                             admin=value[3],
                                             desc=value[4])

    def handle(self, *args, **options):
        self._parse_dict()
        print('db populated with rx')
