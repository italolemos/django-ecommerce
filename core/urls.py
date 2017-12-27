from django.conf.urls import url, include

from .views import index, contact

urlpatterns = [
    url(r'^$', index),
    url(r'contact/$', contact),
    url(r'catalogo/', include('catalog.urls', namespace='catalog')),
]