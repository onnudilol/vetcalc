from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from treatment_sheets.forms import TxSheetForm, TxItemForm
from treatment_sheets.models import TxSheet, TxItem
from common.models import Prescription

User = get_user_model()


def treatment_sheets(request):
    return render(request, 'tx_sheet/tx_sheet.html', {'navbar': 'tx_sheet'})


@login_required()
def view_treatment_sheet(request, sheet_id):
    sheet = TxSheet.objects.get(pk=sheet_id)
    form = TxItemForm()

    if request.method == 'POST' and request.user == sheet.owner:
        form = TxItemForm(data=request.POST)

        if form.is_valid():
            tx_sheet = form.save(sheet=sheet)
            return redirect(tx_sheet)

    if request.user == sheet.owner:
        return render(request, 'tx_sheet/tx_sheet_view.html', {'navbar': 'tx_sheet', 'sheet': sheet, 'form': form})

    else:
        raise PermissionDenied


@login_required()
def new_tx_sheet(request):
    sheet_form = TxSheetForm()
    item_form = TxItemForm()

    if request.method == 'POST':
        sheet_form = TxSheetForm(data=request.POST)
        item_form = TxItemForm(data=request.POST)

        if sheet_form.is_valid() and item_form.is_valid():
            tx_sheet = sheet_form.save(owner=request.user)
            item_form.save(sheet=tx_sheet)
            return redirect(tx_sheet)

    return render(request, 'tx_sheet/tx_sheet_new.html', {'navbar': 'tx_sheet',
                                                          'sheet_form': sheet_form, 'item_form': item_form})


@login_required()
def del_item_tx_sheet(request, sheet_id, item_id):
    tx_sheet = TxSheet.objects.get(id=sheet_id)

    if request.user == tx_sheet.owner:
        TxItem.objects.get(id=item_id).delete()
        return redirect(tx_sheet)

    else:
        raise PermissionDenied
