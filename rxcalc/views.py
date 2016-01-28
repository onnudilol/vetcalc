from django.shortcuts import render

from rxcalc.models import Medication
from rxcalc.forms import WeightForm

from itertools import zip_longest


def home(request):

    return render(request, 'rxcalc/home.html', {'navbar': 'home'})


def calc_dosage(request):

    meds = Medication.objects.all()

    if request.method == 'POST':

        weight = float(request.POST['weight'])
        dosages = list()

        for med in meds:
            dosages.append(round(weight * med.factor, 3))

        zipped = list(zip(meds, dosages))

        return render(request, 'rxcalc/calc.html', {'rx': zipped,
                                                    'form': WeightForm(),
                                                    'navbar': 'calc'})

    null_dose = []
    zipped = list(zip_longest(meds, null_dose, fillvalue=0.0))

    return render(request, 'rxcalc/calc.html', {'rx': zipped,
                                                'form': WeightForm(),
                                                'navbar': 'calc'})


def rx_info(request):
    return render(request, '404.html', {'navbar': 'info'})


def treatment_sheet(request):
    return render(request, '404.html', {'navbar': 'tx_sheet'})
