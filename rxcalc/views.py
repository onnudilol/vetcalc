from django.shortcuts import render
from rxcalc.models import Injection
from rxcalc.forms import WeightForm

from collections import OrderedDict


def home(request):
    return render(request, 'rxcalc/home.html', {'navbar': 'home'})


def calc_dosage(request):
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
            return render(request, 'rxcalc/calc.html', {'rx': rx_ordered,
                                                        'form': WeightForm(),
                                                        'navbar': 'calc',
                                                        'errors': form.errors.values()})

    return render(request, 'rxcalc/calc.html', {'rx': rx_ordered,
                                                'form': WeightForm(),
                                                'navbar': 'calc'})


def info(request):
    inj = Injection.objects.all()
    return render(request, 'rxcalc/info.html', {'navbar': 'info',
                                                'inj': inj})


def inj_info(request, slug):
    inj = Injection.objects.get(slug=slug)
    return render(request, 'rxcalc/rx.html', {'navbar': 'info',
                                              'rx': inj})


def treatment_sheet(request):
    return render(request, '404.html', {'navbar': 'tx_sheet'})
