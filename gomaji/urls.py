"""
gomaji url
"""
from django.conf.urls import include, url
from django.contrib import admin
from myshop import views

urlpatterns = [
    url(r'^myshop/', include('myshop.urls', namespace="myshop")),
    url(r'^admin/', include(admin.site.urls)),
]
