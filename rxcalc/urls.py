from django.conf.urls import url

from rxcalc import views

urlpatterns = [
    url(r'^$', views.calc_dosage, name='calc')
]
