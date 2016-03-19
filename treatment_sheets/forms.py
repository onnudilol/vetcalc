from django.forms import ModelForm

from crispy_forms.helper import FormHelper

from common.models import Prescription
from treatment_sheets.models import TxItem, TxSheet


class NewTxSheetForm(ModelForm):
    pass


class EditTxSheetForm(ModelForm):
    pass
