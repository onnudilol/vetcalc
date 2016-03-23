from django import forms
from django.forms.utils import ErrorList

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit, HTML
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
        self.helper.form_id = 'id_calc_inj_form'
        self.helper.form_show_labels = False

        glyph = '<span class="glyphicon glyphicon-play"></span>'

        self.helper.layout = Layout(
                FieldWithButtons(Field('weight'),
                                 StrictButton(content=glyph, type='submit', css_class='btn-primary')))

    weight = forms.FloatField(label='Weight',
                              error_messages={'invalid': INVALID_INPUT_ERROR},
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter weight (lb)'}))


class CRISimpleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_cri_simple_form'
        self.helper.form_show_labels = False

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
            Fieldset(
                'Advanced CRI Calculator',
                'weight',
                'rate',
                'volume',
                'infusion',
                FormActions(Submit('submit', 'Submit')),
            )
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
            Fieldset(
                'Insulin CRI Calculator',
                'weight',
                'rate',
                'volume',
                'replacement',
                FormActions(Submit('submit', 'Submit')),
            )
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
                                   help_text='Recommended rates: 0.03 to 0.12 mmol/kg/hour',
                                   error_messages={'invalid': INVALID_INPUT_ERROR},
                                   widget=forms.NumberInput(attrs={'placeholder': 'Enter desired replacement rate'}))


class CRICPRForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_cri_cpr_form'

        self.helper.layout = Layout(
            Fieldset(
                'Post CPR CRI Calculator',
                'weight',
                'rate',
                'volume',
                'dobutamine',
                'dopamine',
                'lidocaine',
                FormActions(Submit('submit', 'Submit'))
            )

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

    dobutamine = forms.FloatField(label='Dobutamine',
                                  help_text='Recommended rates: 2 to 20 µg/kg/min',
                                  error_messages={'invalid': INVALID_INPUT_ERROR},
                                  widget=forms.NumberInput(attrs={'placeholder': 'Enter desired dobutamine rate'}))

    dopamine = forms.FloatField(label='Dopamine',
                                help_text='Recommended rates: 2 to 20 µg/kg/min',
                                error_messages={'invalid': INVALID_INPUT_ERROR},
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter desired dopamine rate'}))

    lidocaine = forms.FloatField(label='Lidocaine',
                                 help_text='Recommended rates: 50 to 100 µg/kg/min',
                                 error_messages={'invalid': INVALID_INPUT_ERROR},
                                 widget=forms.NumberInput(attrs={'placeholder': 'Enter desired lidocaine rate'}))


class CRIMetoclopramideForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_cri_metoclopramide_form'

        self.helper.layout = Layout(
            Fieldset(
                'Metoclopramide CRI Calculator',
                'weight',
                'rate',
                'volume',
                'infusion',
                HTML('<hr class="separator">'),
                HTML('<p><b>To increase the dose of metoclopramide, fill out the following fields:</b></p>'),
                'inc_volume',
                'inc_infusion',
                FormActions(Submit('submit', 'Submit'))
            )
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
                                help_text='Recommended rates: 1 to 2 mg/kg/day',
                                error_messages={'invalid': INVALID_INPUT_ERROR},
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter desired infusion rate'}))

    inc_infusion = forms.FloatField(label='Increase infusion rate',
                                    required=False,
                                    help_text='Recommended rates: 0.5, 1, or 2 mg/kg/day',
                                    error_messages={'invalid': INVALID_INPUT_ERROR},
                                    widget=forms.NumberInput(attrs={'placeholder': 'Enter desired infusion rate'}))

    inc_volume = forms.FloatField(label='Remaining volume',
                                  required=False,
                                  error_messages={'invalid': INVALID_INPUT_ERROR},
                                  widget=forms.NumberInput(attrs={'placeholder': 'Enter remaining volume (mL)'}))
