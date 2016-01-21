from django.shortcuts import render

from rxcalc.models import Medication
from rxcalc.forms import WeightForm


def home_page(request):
    return render(request, 'rxcalc/home.html', {'rx': Medication.objects.all(),
                                                'form': WeightForm()})


def calc_dosage(request):

    if request.method == 'POST':

        form = WeightForm(data=request.POST)

        if form.is_valid():
            weight = float(request.POST['weight'])
            meds = Medication.objects.all()
            dosages = list()

            for med in meds:
                dosages.append(weight * med.factor)

            return render(request, 'rxcalc/home.html', {'rx': Medication.objects.all(),
                                                        'form': WeightForm(),
                                                        'dosages': dosages})

    return render(request, 'rxcalc/home.html', {'rx': Medication.objects.all(),
                                                'form': WeightForm()})
