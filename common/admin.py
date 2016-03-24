from django.contrib import admin
from common.models import Injection, CRI, Prescription

admin.site.register(Injection)
admin.site.register(CRI)
admin.site.register(Prescription)
