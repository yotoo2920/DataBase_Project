from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^set_of_data/$', views.set_of_data, name='set_of_data'),
    url(r'^queries/$', views.queries, name='queries'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^queries/query1$', views.query1, name='query1'),
    url(r'^queries/query2$', views.query2, name='query2'),
    url(r'^queries/query3$', views.query3, name='query3'),
    url(r'^queries/query4$', views.query4, name='query4'),
    url(r'^queries/query5$', views.query5, name='query5'),
]
