from django.shortcuts import render
from rxcalc.models import Medication
from rxcalc.forms import WeightForm

from collections import OrderedDict


def home(request):
    return render(request, 'rxcalc/home.html', {'navbar': 'home'})


def calc_dosage(request):
    meds = Medication.objects.all()
    rx = dict()

    for med in meds:
        rx[med] = 0.0

    rx_ordered = OrderedDict(sorted(rx.items(), key=lambda t: t[0].name))

    if request.method == 'POST':
        form = WeightForm(data=request.POST)

        if form.is_valid():
            weight = float(request.POST['weight'])

            for med in meds:
                rx_ordered[med] = round(med.factor * weight, 3)

            return render(request, 'rxcalc/calc.html', {'rx': rx_ordered,
                                                        'form': WeightForm(),
                                                        'navbar': 'calc'})

        else:
            return render(request, 'rxcalc/calc.html', {'rx': rx_ordered,
                                                        'form': WeightForm(),
                                                        'navbar': 'calc',
                                                        'errors': form.errors.values()})

    return render(request, 'rxcalc/calc.html', {'rx': rx_ordered,
                                                'form': WeightForm(),
                                                'navbar': 'calc'})


def info(request):
    meds = Medication.objects.all()
    return render(request, 'rxcalc/info.html', {'navbar': 'info',
                                                'meds': meds})


def rx_info(request, slug):
    med = Medication.objects.get(slug=slug)
    return render(request, 'rxcalc/rx.html', {'navbar': 'info',
                                              'med': med})


def treatment_sheet(request):
    return render(request, '404.html', {'navbar': 'tx_sheet'})
