from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from treatment_sheets.forms import NewTxSheetForm
from treatment_sheets.models import TxSheet, TxItem
from common.models import Prescription


def treatment_sheets(request):
    if request.user.is_authenticated():
        sheets = TxSheet.objects.get(owner=request.user)
        return render(request, 'tx_sheet/tx_sheet.html', {'sheets': sheets})

    return render(request, 'tx_sheet/tx_sheet.html')


@login_required()
def view_treatment_sheet(request):
    return render(request, '404.html', {'navbar': 'tx_sheet'})


@login_required()
def new_tx_sheet(request):
    pass


@login_required()
def add_item_tx_sheet(request):
    pass


@login_required()
def del_item_tx_sheet(request):
    pass
