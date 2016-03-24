from django.conf.urls import url

from treatment_sheets import views

urlpatterns = [
    url('^$', views.treatment_sheets, name='tx_sheet'),
    url('^new$', views.new_tx_sheet, name='new_tx_sheet'),
    url('^(\d+)/$', views.view_treatment_sheet, name='view_tx_sheet'),
    url('^(\d+)/edit$', views.edit_tx_sheet, name='edit_tx_sheet'),
    url('^(\d+)/del', views.del_tx_sheet, name='del_tx_sheet'),
    url('^(\d+)/(\d+)/del$', views.del_item_tx_sheet, name='del_item_tx_sheet'),
    url('^(\d+)/pdf', views.output_pdf, name='output_pdf')
]
