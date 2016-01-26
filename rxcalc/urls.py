from django.conf.urls import url

from rxcalc import views

urlpatterns = [
    url(r'^$', views.calc_dosage, name='calc'),
    url(r'^info/$', views.rx_info, name='info'),
    url(r'^tx_sheet/$', views.treatment_sheet, name='tx_sheet'),
]
