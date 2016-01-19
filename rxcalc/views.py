from django.shortcuts import render

WEIGHT = int()


def home_page(request):
    return render(request, 'rxcalc/home.html')
