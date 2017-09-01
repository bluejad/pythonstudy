
from django.conf.urls import include, url
from django.contrib import admin

from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'archievement'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index, name='index'),
    url(r'^achievement$', views.achievement, name='achievement'),
    url(r'^set_new_purpose$', views.set_new_purpose, name='set_new_purpose'),
    url(r'^(?P<id>[0-9]+)/$', views.changestate, name='changestate'),
    url(r'^viewcontent/(?P<id>[0-9]+)/$', views.viewcontent, name='viewcontent'),
    url(r'^deleteone/(?P<id>[0-9]+)/$', views.deleteone, name='deleteone'),
    url(r'^yearcontent/(?P<year>[0-9]+)/$', views.yearcontent, name='yearcontent'),
    url(r'^set_year_summary$', views.set_year_summary, name='set_year_summary'),
]

