from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from treatment_sheets.forms import NewTxSheetForm
from common.models import Prescription


def treatment_sheets(request):
    pass


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
