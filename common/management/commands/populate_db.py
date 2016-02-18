from django.core.management.base import BaseCommand

from common.models import Injection
from common.dosage import DOSAGE_INJECTION


class Command(BaseCommand):
    help = 'Populates the db with data'

    def _parse_dict(self):
        for key, value in DOSAGE_INJECTION.items():
            med, created = Injection.objects.get_or_create(name=key,
                                                           factor=value[0],
                                                           concentration=value[1],
                                                           category=value[2],
                                                           admin=value[3],
                                                           desc=value[4])
            med.save()

    def handle(self, *args, **options):
        self._parse_dict()
        print('db populated with rx')
