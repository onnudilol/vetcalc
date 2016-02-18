from django.shortcuts import render

from common.models import Injection
from calc.forms import WeightForm

from collections import OrderedDict


def calc(request):
    return render(request, 'calc/calc.html', {'navbar': 'calc'})


def calc_injection(request):
    meds = Injection.objects.all()
    rx = dict()

    for med in meds:
        rx[med] = 0.0

    rx_ordered = OrderedDict(sorted(rx.items(), key=lambda t: t[0].name))

    if request.method == 'GET' and request.is_ajax():
        form = WeightForm(data=request.GET)

        if form.is_valid():
            weight = float(request.GET['weight'])

            for med in meds:
                rx_ordered[med] = round(med.factor * weight, 3)

        else:
            return render(request, 'calc/injection.html', {'rx': rx_ordered,
                                                           'form': WeightForm(),
                                                           'navbar': 'calc',
                                                           'errors': form.errors.values()})

    return render(request, 'calc/injection.html', {'rx': rx_ordered,
                                                   'form': WeightForm(),
                                                   'navbar': 'calc'})


def calc_cri(request):
    return render(request, 'calc/cri.html', {'navbar': 'calc'})


def calc_cri_simple(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_advanced(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_cpr(request):
    return render(request, '404.html', {'navbar': 'calc'})


def calc_cri_metoclopramide(request):
    return render(request, '404.html', {'navbar': 'calc'})
