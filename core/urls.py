from django.conf.urls import url

from .views import index, contact

urlpatterns = [
    url(r'^$', index),
    url(r'contact/$', contact)
]