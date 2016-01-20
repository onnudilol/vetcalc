from django import forms

from rxcalc.models import Medication


INVALID_INPUT_ERROR = 'Input must be a number'


class WeightForm(forms.Form):
    weight = forms.FloatField(required=False, label='Weight', help_text='Input weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 0.0}))
