from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import FieldWithButtons, StrictButton


INVALID_INPUT_ERROR = 'Input must be a number'


class WeightForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-inline navbar-form navbar-right'
        self.helper.form_show_labels = False
        glyph = '<span class="glyphicon glyphicon-play"></span>'

        self.helper.layout = Layout(
                FieldWithButtons(Field('weight', css_class='input-sm'),
                                 StrictButton(content=glyph, type='submit', css_class='btn-primary btn-sm')))

    weight = forms.FloatField(required=False, label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight'}))
