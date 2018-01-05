from django.conf.urls import url

from .views import ProductListView, CategoryListView, product

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', CategoryListView.as_view(), name='category'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', product, name='product'),
]