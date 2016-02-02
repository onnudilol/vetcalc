from django.conf.urls import url

from rxcalc import views

urlpatterns = [
    url(r'^calc/$', views.calc_dosage, name='calc'),
    url(r'^info/$', views.info, name='info'),
    url(r'info/(?P<slug>[\w\-]+)', views.rx_info, name='rx'),
    url(r'^tx_sheet/$', views.treatment_sheet, name='tx_sheet'),
]
