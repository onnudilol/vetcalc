from django.shortcuts import render
from rxcalc.models import Medication
from rxcalc.forms import WeightForm

from itertools import zip_longest


def home(request):
    return render(request, 'rxcalc/home.html', {'navbar': 'home'})


def calc_dosage(request):
    meds = Medication.objects.all()
    null_dose = []
    zipped = list(zip_longest(meds, null_dose, fillvalue=0.0))

    if request.method == 'POST':

        # Weird bug with how buttons rendered by crispy forms ignores validation.
        # This is a hacky check to prevent 500 errors.
        if request.POST['weight'] == '':

            return render(request, 'rxcalc/calc.html', {'rx': zipped,
                                                        'form': WeightForm(),
                                                        'navbar': 'calc'})

        weight = float(request.POST['weight'])
        dosages = list()

        for med in meds:
            dosages.append(round(weight * med.factor, 3))

        zipped = list(zip(meds, dosages))
        return render(request, 'rxcalc/calc.html', {'rx': zipped,
                                                    'form': WeightForm(),
                                                    'navbar': 'calc'})

    return render(request, 'rxcalc/calc.html', {'rx': zipped,
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
