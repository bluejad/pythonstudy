
from django.conf.urls import include, url
from django.contrib import admin

from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'pythonnav'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),

    url(r'^SIGN_IN_NOW$', views.SIGN_IN_NOW, name='SIGN_IN_NOW'),
    url(r'^register_html$', views.register_html, name='register_html'),
    url(r'^buttons.html$', views.buttons_html, name='buttons_html'),
    url(r'^blogindex.html$', views.blogindex_html, name='blogindex_html'),
    url(r'^studyguide$', views.calendar_html, name='calendar_html'),
    url(r'^profile$', views.profile_html, name='profile_html'),
    url(r'^(?P<detail_question_id>[0-9]+)/$', views.questioncontents, name='questioncontent'),
    url(r'^form_component_html$', views.form_component_html, name='form_component_html'),

    url(r'^ajax_list/$', views.ajax_list, name='ajax_list'),

    url(r'^sendemail$', views.sendemail, name='sendemail'),

    url(r'^user_register$', views.user_register, name='user_register'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'^user_logout$', views.user_logout, name='user_logout'),
    url(r'^ask_question$', views.ask_question, name='ask_question'),
    url(r'^reply_question$', views.reply_question, name='reply_question'),
    url(r'^uploadImg$', views.uploadImg, name='uploadImg'),
    url(r'^changepersonalprofile$', views.changepersonalprofile, name='changepersonalprofile'),
    url(r'^studyrecoder$', views.studyrecoder, name='studyrecoder'),

    url(r'^test$', views.test, name='test'),
    url(r'^test1$', views.test1, name='test1'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

