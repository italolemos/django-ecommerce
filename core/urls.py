from django.conf.urls import url, include

from .views import IndexView, contact, RegisterView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^registro/$', RegisterView.as_view(), name='registro'),
    url(r'contact/$', contact, name='contact'),
    url(r'catalogo/', include('catalog.urls', namespace='catalog')),
]