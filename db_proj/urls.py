from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^set_of_data/$', views.set_of_data, name='set_of_data'),
    url(r'^$', views.queries, name='queries'),
    url(r'^$', views.about_us, name='about_us'),
]
# ^students/$
