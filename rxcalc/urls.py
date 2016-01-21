from django.conf.urls import url

from rxcalc import views

urlpatterns = [
    url(r'^calc$', views.calc_dosage, name='calc_dosage'),
]
