from django.shortcuts import render

from common.models import Injection, CRI


def info(request):
    inj = Injection.objects.all()
    cri = CRI.objects.all()
    return render(request, 'info/info.html', {'navbar': 'info',
                                              'inj': inj,
                                              'cri': cri})


def info_inj(request, slug):
    inj = Injection.objects.get(slug=slug)
    return render(request, 'info/rx.html', {'navbar': 'info',
                                            'rx': inj})


def info_cri(request, slug):
    cri = CRI.objects.get(slug=slug)
    return render(request, 'info/rx.html', {'navbar': 'info',
                                            'rx': cri})
