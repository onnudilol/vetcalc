from django.shortcuts import render

from rxcalc.models import Medication
from rxcalc.forms import WeightForm


WEIGHT = int()


def home_page(request):
    context_dict = dict()
    context_dict['rx'] = Medication.objects.all()
    context_dict['form'] = WeightForm()
    return render(request, 'rxcalc/home.html', context_dict)

# TODO: render rx in table
