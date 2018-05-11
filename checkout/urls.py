from django.conf.urls import url
from .views import CreateCartItemView


urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', CreateCartItemView.as_view(), name='create-cartitem'),
]