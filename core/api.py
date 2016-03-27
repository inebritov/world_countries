from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'countries/$', views.CountryList.as_view()),
    url(r'countries/(?P<pk>[0-9]+)/$', views.CountryDetail.as_view()),
]
