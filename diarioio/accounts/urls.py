from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import custom_login, register, edit, edit_password, password_reset, password_reset_confirm, dashboard


urlpatterns = [
    url(r'^login/$', custom_login, name='login'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': 'home'}),
    url(r'^join/$', register, name='register'),
    url(r'^account/edit/$', edit, name='edit'),
    url(r'^account/edit/password$', edit_password, name='edit_password'),
    url(r'^account/password_reset$', password_reset, name='password_reset'),
    url(r'^account/password_reset_confirm/(?P<key>\w+)$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^account/$', dashboard, name='dashboard'),
]
