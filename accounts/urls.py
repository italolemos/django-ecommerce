from django.conf.urls import url

from .views import RegisterView, IndexView, UpdateUserView, UpdatePasswordView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^registro/$', RegisterView.as_view(), name='register'),
    url(r'^alterar-dados/$', UpdateUserView.as_view(), name='update_user'),
    url(r'^alterar-senha/$', UpdatePasswordView.as_view(), name='update_password'),
]