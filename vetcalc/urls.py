"""vetcalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
# from django.contrib import admin

from common import views as common_views

from calc import urls as calc_urls
from calc import views as calc_views

from info import urls as info_urls

from treatment_sheets import urls as tx_sheet_urls

urlpatterns = [
    url(r'^$', common_views.home, name='home'),
    url(r'^calc/', include(calc_urls)),
    url(r'^info/', include(info_urls)),
    url(r'^tx_sheet/', include(tx_sheet_urls)),
    url(r'^disclaimer/', TemplateView.as_view(template_name='disclaimer.html'), name='disclaimer'),
]
