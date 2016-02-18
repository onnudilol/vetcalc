from django.conf.urls import url

from info import views

urlpatterns = [
    url(r'^$', views.info, name='info'),
    url(r'(?P<slug>[\w\-]+)/$', views.info_inj, name='info_inj'),
]
