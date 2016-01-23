from django.shortcuts import render

from rxcalc.models import Medication
from rxcalc.forms import WeightForm

from itertools import zip_longest


def calc_dosage(request):

    meds = Medication.objects.all()

    if request.method == 'POST':

        weight = float(request.POST['weight'])
        dosages = list()

        for med in meds:
            dosages.append(round(weight * med.factor, 3))

        zipped = list(zip(meds, dosages))

        return render(request, 'rxcalc/home.html', {'rx': zipped,
                                                    'form': WeightForm()})

    null_dose = []
    zipped = list(zip_longest(meds, null_dose, fillvalue=0.0))

    return render(request, 'rxcalc/home.html', {'rx': zipped,
                                                'form': WeightForm()})
