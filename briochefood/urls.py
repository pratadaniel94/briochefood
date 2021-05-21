from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name="index"),
]
