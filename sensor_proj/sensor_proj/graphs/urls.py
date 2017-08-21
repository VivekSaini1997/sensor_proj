"""sensor_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^graph/$', views.something),
    url(r'^bptt/$', views.get_minute_data),
    url(r'^latest/$', views.get_second_data),
    url(r'^test/$', views.something_else),
    url(r'^tq/$', views.get_alt),
    url(r'^bptt/(?P<count>\d+)$', views.get_x_data),
    url(r'^tql/$', views.get_latest_alt),
]
