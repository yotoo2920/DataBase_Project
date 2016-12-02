from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^$', views.home_page, name='set_of_data'),
    url(r'^$', views.home_page, name='queries'),
    url(r'^$', views.home_page, name='about_us'),
]
