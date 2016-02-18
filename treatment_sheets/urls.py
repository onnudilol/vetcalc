from django.conf.urls import url

from treatment_sheets import views

urlpatterns = [
    url('^$', views.treatment_sheet, name='tx_sheet'),
]
