from django.forms.models import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from treatment_sheets.models import TxItem, TxSheet


class TxSheetForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

    class Meta:
        model = TxSheet
        fields = ['name', 'comment']

    def save(self, owner):
        return TxSheet.objects.create(owner=owner, name=self.cleaned_data['name'], comment=self.cleaned_data['comment'])


class TxItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit("submit", "Save"))

    class Meta:
        model = TxItem
        fields = ['med', 'dose', 'freq', 'unit']

    def save(self, sheet):
        return TxItem.objects.create(sheet=sheet, med=self.cleaned_data['med'], dose=self.cleaned_data['dose'],
                                     freq=self.cleaned_data['freq'], unit=self.cleaned_data['unit'])
