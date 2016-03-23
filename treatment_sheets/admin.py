from django.contrib import admin
from treatment_sheets.models import TxSheet, TxItem


class TxItemInline(admin.TabularInline):
    model = TxItem
    extra = 3


class TxSheetAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'date')

    fields = [
        'owner', 'name', 'comment'
    ]

    inlines = [TxItemInline]

admin.site.register(TxSheet, TxSheetAdmin)
