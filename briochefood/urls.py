from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^product/$', get_product, name='product'),
    url(r'^order/$', get_order, name='order')
]
