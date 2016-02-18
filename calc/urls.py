from django.conf.urls import url

from calc import views

urlpatterns = [
    url(r'^$', views.calc, name='calc'),
    url(r'^injection/$', views.calc_injection, name='injection'),
    url(r'^cri/$', views.calc_cri, name='cri'),
    url(r'^cri/simple/$', views.calc_cri_simple, name='cri_simple'),
    url(r'^cri/advanced/$', views.calc_cri_advanced, name='cri_advanced'),
    url(r'^cri/cpr/$', views.calc_cri_cpr, name='cri_cpr'),
    url(r'^cri/metoclopramide/', views.calc_cri_metoclopramide, name='cri_metoclopramide'),
]
