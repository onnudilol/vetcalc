from django.core.management.base import BaseCommand

from treatment_sheets.models import TxSheet

from datetime import date, timedelta


class Command(BaseCommand):

    @staticmethod
    def _delete_expired_lists():
        old_days = timedelta(days=3)
        old_date = date.today() - old_days
        old_sheets = TxSheet.objects.filter(date__lte=old_date)
        for sheet in old_sheets:
            sheet.delete()

    def handle(self, *args, **options):
        self._delete_expired_lists()
        print('Expired treatment sheets deleted.')
