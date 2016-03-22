from django.contrib import admin
from treatment_sheets.models import TxSheet, TxItem

admin.site.register(TxSheet)
admin.site.register(TxItem)