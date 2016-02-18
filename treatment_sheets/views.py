from django.shortcuts import render


def treatment_sheet(request):
    return render(request, '404.html', {'navbar': 'tx_sheet'})
