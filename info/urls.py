from django.conf.urls import url

from info import views

urlpatterns = [
    url(r'^$', views.info, name='info'),
    url(r'inj/(?P<slug>[\w\-]+)/$', views.info_inj, name='info_inj'),
    url(r'cri/(?P<slug>[\w\-]+)/$', views.info_cri, name='info_cri'),
    url(r'pre/(?P<slug>[\w\-]+)/$', views.info_pre, name='info_pre')
]
