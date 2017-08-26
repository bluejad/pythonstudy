
from django.conf.urls import include, url
from django.contrib import admin

from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'resourcedownload'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dynamic_table_html$', views.dynamic_table_html, name='dynamic_table_html'),
    url(r'^querystation_html$', views.querystation_html, name='querystation_html'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

