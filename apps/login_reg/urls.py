from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login_reg/login$', views.login),
	url(r'^login_reg/registration$', views.registration),
	url(r'^success$', views.success)

]