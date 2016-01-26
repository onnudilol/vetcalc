from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import FormActions


INVALID_INPUT_ERROR = 'Input must be a number'


class WeightForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-inline navbar-form navbar-right'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(Field('weight', css_class='input-sm'),
                                    FormActions(Submit('submit', 'Submit', css_class='btn-sm')))

    weight = forms.FloatField(required=False, label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight'}))
