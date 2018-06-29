from django.conf.urls import url
from .views import CreateCartItemView, CartItemView


urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', CreateCartItemView.as_view(), name='create-cartitem'),
    url(r'^carrinho/$', CartItemView.as_view(), name='cart_item')
]