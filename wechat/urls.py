
from django.conf.urls import include, url
from django.contrib import admin

from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'wechat'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.weixin_main, name='weixin_main'),
]

