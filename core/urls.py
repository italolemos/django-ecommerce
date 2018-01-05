from django.conf.urls import url, include

from .views import IndexView, contact

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'contact/$', contact, name='contact'),
    url(r'catalogo/', include('catalog.urls', namespace='catalog')),
]