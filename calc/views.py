from django.shortcuts import render

from common.models import Injection, CRI
from calc.forms import CalcInjForm, CRISimpleForm

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

        else:
            return render(request, 'calc/cri_simple.html', {'form': form,
                                                            'navbar': 'calc',
                                                            'rx': rx})

    return render(request, 'calc/cri_simple.html', {'navbar': 'calc',
                                                    'form': form,
                                                    'rx': rx})


def calc_cri_advanced(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_cpr(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_metoclopramide(request):
    return render(request, '404.html', {'navbar': 'calc'})
