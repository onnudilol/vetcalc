from django import forms
from django.forms.utils import ErrorList

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import FieldWithButtons, StrictButton, FormActions


INVALID_INPUT_ERROR = 'Input must be a number'


class NoBulletErrorList(ErrorList):

    def __str__(self):
        return self.as_text()

    def as_text(self):
        return '\n'.join('%s' % e for e in self)


class CalcInjForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = NoBulletErrorList
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_class = 'navbar-form'
        self.helper.form_id = 'id_calc_inj_form'
        self.helper.form_show_labels = False

        glyph = '<span class="glyphicon glyphicon-play"></span>'

        self.helper.layout = Layout(
                FieldWithButtons(Field('weight', css_class='input-sm'),
                                 StrictButton(content=glyph, type='submit', css_class='btn-primary btn-sm')))

    weight = forms.FloatField(label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight'}))


class CRISimpleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_cri_simple_form'

        glyph = '<span class="glyphicon glyphicon-play"></span>'

        self.helper.layout = Layout(
            FieldWithButtons(Field('weight'),
                             StrictButton(content=glyph, type='submit', css_class='btn-primary'))
        )

    weight = forms.FloatField(label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight (kg)'}))


class CRIAdvancedForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_cri_advanced_form'

        self.helper.layout = Layout(
            Field('weight'),
            Field('rate'),
            Field('volume'),
            Field('infusion'),
            FormActions(Submit('submit', 'Submit'))
        )

    weight = forms.FloatField(label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight (kg)'}))

    rate = forms.FloatField(label='Fluid rate',
                            error_messages={'invalid': INVALID_INPUT_ERROR},
                            widget=forms.NumberInput(attrs={'placeholder': 'Enter rate (mL/hr)'}))

    volume = forms.FloatField(label='Remaining volume',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter remaining volume (mL)'}))

    infusion = forms.FloatField(label='Desired infusion rate',
                                error_messages={'invalid': INVALID_INPUT_ERROR},
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter desired infusion rate'}))


class CRIInsulinForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_cri_insulin_form'

        self.helper.layout = Layout(
            Field('weight'),
            Field('rate'),
            Field('volume'),
            Field('replacement'),
            FormActions(Submit('submit', 'Submit'))
        )

    weight = forms.FloatField(label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight (kg)'}))

    rate = forms.FloatField(label='Fluid rate',
                            error_messages={'invalid': INVALID_INPUT_ERROR},
                            widget=forms.NumberInput(attrs={'placeholder': 'Enter rate (mL/hr)'}))

    volume = forms.FloatField(label='Remaining volume',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter remaining volume (mL)'}))

    replacement = forms.FloatField(label='Desired replacement rate',
                                   error_messages={'invalid': INVALID_INPUT_ERROR},
                                   widget=forms.NumberInput(attrs={'placeholder': 'Enter desired replacement rate'}))
