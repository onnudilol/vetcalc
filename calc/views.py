from django.shortcuts import render

from common.models import Injection, CRI
from calc.forms import CalcInjForm, CRISimpleForm, CRIAdvancedForm, CRIInsulinForm, CRICPRForm, CRIMetoclopramideForm

from collections import OrderedDict


def calc_injection(request):
    """Calculates injection dosages based on weight.

    GET parameters:
        weight: weight in lbs

    Contxt:
        calculated dose rounded to 3 decimal places

    """

    meds = Injection.objects.all()
    rx = dict()

    # default displayed dosage of 0.0 mLs
    for med in meds:
        rx[med] = 0.0

    rx_ordered = OrderedDict(sorted(rx.items(), key=lambda t: t[0].name))

    if request.method == 'GET' and request.is_ajax():
        form = CalcInjForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])

            for med in meds:
                rx_ordered[med] = round(med.factor * weight, 3)

    return render(request, 'calc/injection.html', {'rx': rx_ordered,
                                                   'form': CalcInjForm(),
                                                   'navbar': 'calc'})


def calc_cri_simple(request):
    """Calculates simple CRI dosages based on weight.

    GET parameters:
        weight: weight in kgs

    Context:
        rx: calculated dosages rounded to 3 decimal places

    """

    meds = CRI.objects.filter(calc_type='ez')
    form = CRISimpleForm()
    rx = dict()
    bolus = dict()

    # zipped list of rates to dosage with default displayed dosages of 0.0 mL
    for med in meds:
        rx[med] = list(zip([rate for rate in med.rates],
                           [0.0 * rate for rate in med.rates]))

    if request.method == 'GET' and request.is_ajax():
        form = CRISimpleForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])

            for med in meds:
                rx[med] = list(zip([rate for rate in med.rates],
                                   [round(weight * med.factor * rate, 3) for rate in med.rates]))

            # bolus is calculated for diltiazem
            bolus = {'mg': round(weight * 0.25, 3), 'mL': round(weight * 0.05, 3)}

    return render(request, 'calc/cri_simple.html', {'navbar': 'calc',
                                                    'form': form,
                                                    'rx': rx,
                                                    'bolus': bolus})


def calc_cri_advanced(request):
    """Calculates complex CRI dosages based on multiple inputs.

    GET parameters:
        weight: weight in kgs
        rate: current cri rate
        volume: current iv volume in mL
        infusion: target infusion rate

    Context:
        rx: calculated dosages rounded to 3 decimal places

    """

    meds = CRI.objects.filter(calc_type='adv')
    form = CRIAdvancedForm()
    rx = dict()

    for med in meds:
        rx[med] = dict()

    if request.method == 'GET' and request.is_ajax():
        form = CRIAdvancedForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])
            rate = float(request.GET['rate'])
            volume = float(request.GET['volume'])
            infusion = float(request.GET['infusion'])

            for med in meds:
                rx[med] = {'maint': round((weight * 30 * 2.2)/24, 3),
                           'maint_plus': round((weight * 30 + 70)/24, 3),
                           'add': round(((weight * infusion * med.factor) / (rate/60)) * volume, 3)}

    return render(request, 'calc/cri_advanced.html', {'navbar': 'calc',
                                                      'form': form,
                                                      'rx': rx})


def calc_cri_insulin(request):
    """Calculates CRI dosages for insulin

    GET parameters:
        weight: weight in kgs
        rate: current rate
        volume: current iv vol in mLs
        replacement: target replacement rate

    Context:
        rx: calculated dosages rounded to 3 decimal places

    """
    form = CRIInsulinForm()
    rx = dict()

    if request.method == 'GET' and request.is_ajax():
        form = CRIInsulinForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])
            rate = float(request.GET['rate'])
            volume = float(request.GET['volume'])
            replacement = float(request.GET['replacement'])

            phosphorus = ((weight * replacement/3) * volume)/rate

            rx = {'maint': round((weight * 2.2 * 30)/24, 3),
                  'maint_plus': round((weight * 30 + 70)/24, 3),
                  'units_dog': round(((weight * 2.2) / (rate * 24)) * volume, 3),
                  'units_cat': round((weight * 1.1) / (rate * 24) * volume, 3),
                  'phosphorus': round(phosphorus, 3),
                  'phosphorus_excess': round(phosphorus * 4.4 * 1000 / volume, 3)}

    return render(request, 'calc/cri_insulin.html', {'navbar': 'calc',
                                                     'form': form,
                                                     'rx': rx})


def calc_cri_cpr(request):
    """Calculates CRI dosages for post CPR maintenance

    GET parameters:
        weight: weight in kg
        rate: current rate
        volume: current iv vol in mL
        dobutamine: target dobutamine rate
        dopamine: target dopamine rate
        lidocaine: target lidocaine rate

    Context:
        rx: calculated cri dosages rounded to 3 decimal places

    """

    form = CRICPRForm()
    rx = dict()

    if request.method == 'GET' and request.is_ajax():
        form = CRICPRForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])
            rate = float(request.GET['rate'])
            volume = float(request.GET['volume'])
            dobutamine = float(request.GET['dobutamine'])
            dopamine = float(request.GET['dopamine'])
            lidocaine = float(request.GET['lidocaine'])

            rx = {'maint': round((weight * 2.2 * 30)/24, 3),
                  'maint_plus': round((weight * 30 + 70)/24, 3),
                  'dose_dobutamine': round(((weight * dobutamine) / 12500)/(rate/60) * volume, 3),
                  'dose_dopamine': round((weight * dopamine / 40000)/(rate/60) * volume, 3),
                  'dose_lidocaine': round((weight * lidocaine / 20000)/(rate/60) * volume, 3),
                  'dose_epinephrine': round((weight/1000)/(rate/60) * volume, 3),
                  'dose_mannitol': round(weight * 4, 3),
                  'dose_solumedrol': round(weight * 30, 3)}

    return render(request, 'calc/cri_cpr.html', {'navbar': 'calc',
                                                 'form': form,
                                                 'rx': rx})


def calc_cri_metoclopramide(request):
    """Calculates CRI dosages for metoclopramide

    GET parameters:
        weight: weight in kg
        rate: current rate
        volume: current iv volume in mLs
        infusion: target infusion rate

    Context:
        rx: calculated cri dosages rounded to 3 decimal places

    """
    form = CRIMetoclopramideForm()
    rx = dict()

    if request.method == 'GET' and request.is_ajax():
        form = CRIMetoclopramideForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])
            rate = float(request.GET['rate'])
            volume = float(request.GET['volume'])
            infusion = float(request.GET['infusion'])
            dose = (weight * infusion / 5)/(rate * 24) * volume

            rx = {'maint': round((weight * 2.2 * 30)/24, 3),
                  'maint_plus': round((weight * 30 + 70)/24, 3),
                  'dose': round(dose, 3),
                  'concentration': round(dose * 5 / volume, 3)}

            if request.GET['inc_infusion'] and request.GET['inc_volume']:
                inc_volume = float(request.GET['inc_volume'])
                inc_infusion = float(request.GET['inc_infusion'])
                dose_inc_infusion = inc_infusion + infusion

                rx['inc_infusion'] = round(dose_inc_infusion, 3)
                rx['inc_dose'] = round(((dose_inc_infusion * weight / (rate * 24)) - (dose * 5 / volume)) * inc_volume / 5, 3)
                rx['inc_rate'] = round((dose_inc_infusion * weight)/((dose * 5)/volume)/24, 3)

    return render(request, 'calc/cri_metoclopramide.html', {'navbar': 'calc',
                                                            'form': form,
                                                            'rx': rx})
