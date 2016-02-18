from django.shortcuts import render

from common.models import Injection


def info(request):
    inj = Injection.objects.all()
    return render(request, 'info/info.html', {'navbar': 'info',
                                              'inj': inj})


def info_inj(request, slug):
    inj = Injection.objects.get(slug=slug)
    return render(request, 'info/rx.html', {'navbar': 'info',
                                            'rx': inj})
