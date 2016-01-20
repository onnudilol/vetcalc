from django.shortcuts import render

from rxcalc.models import Medication

WEIGHT = int()


def home_page(request):
    context_dic = dict()
    context_dic['rx'] = Medication.objects.all()
    return render(request, 'rxcalc/home.html', context_dic)

# TODO: render rx in table
