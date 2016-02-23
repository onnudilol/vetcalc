from django.shortcuts import render

from common.models import Injection, CRI
from calc.forms import CalcInjForm, CRISimpleForm, CRIAdvancedForm

from collections import OrderedDict


def calc_injection(request):
    meds = Injection.objects.all()
    rx = dict()

    for med in meds:
        rx[med] = 0.0

    rx_ordered = OrderedDict(sorted(rx.items(), key=lambda t: t[0].name))

    if request.method == 'GET' and request.is_ajax():
        form = CalcInjForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])

            for med in meds:
                rx_ordered[med] = round(med.factor * weight, 3)

        else:
            return render(request, 'calc/injection.html', {'rx': rx_ordered,
                                                           'form': CalcInjForm(),
                                                           'navbar': 'calc',
                                                           'errors': form.errors.values()})

    return render(request, 'calc/injection.html', {'rx': rx_ordered,
                                                   'form': CalcInjForm(),
                                                   'navbar': 'calc'})


def calc_cri_simple(request):
    meds = CRI.objects.filter(calc_type='ez')
    form = CRISimpleForm()
    rx = dict()
    bolus = dict()

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

            bolus = {'mg': round(weight * 0.25, 3), 'mL': round(weight * 0.05, 3)}

        else:
            return render(request, 'calc/cri_simple.html', {'form': form,
                                                            'navbar': 'calc',
                                                            'rx': rx,
                                                            'bolus': bolus})

    return render(request, 'calc/cri_simple.html', {'navbar': 'calc',
                                                    'form': form,
                                                    'rx': rx,
                                                    'bolus': bolus})


def calc_cri_advanced(request):
    meds = CRI.objects.filter(calc_type='adv')
    form = CRIAdvancedForm()
    rx = dict()
    dogs = 'WHAT'

    for med in meds:
        rx[med] = dict()

    if request.method == 'GET' and request.is_ajax():
        form = CRIAdvancedForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])
            rate = float(request.GET['rate'])
            volume = float(request.GET['volume'])
            infusion = float(request.GET['infusion'])
            dogs = 'doge'

            for med in meds:
                rx[med] = {'maint': round((weight * 30 * 2.2)/24, 3),
                           'maint_plus': round(((weight * 30) + 70)/24, 3),
                           'add': round((((weight * infusion) * med.factor) / (rate/60)) * volume, 3)}

        else:
            dogs = 'NOPE'
            return render(request, 'calc/cri_advanced.html', {'form': form,
                                                              'navbar': 'calc',
                                                              'rx': rx,
                                                              'dogs': dogs})

    return render(request, 'calc/cri_advanced.html', {'navbar': 'calc',
                                                      'form': form,
                                                      'rx': rx,
                                                      'dogs': dogs})


def calc_cri_insulin(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_cpr(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_metoclopramide(request):
    return render(request, '404.html', {'navbar': 'calc'})
