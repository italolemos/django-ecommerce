from django.conf.urls import url

from .views import RegisterView


urlpatterns = [
    url(r'^registro/$', RegisterView.as_view(), name='register'),
]