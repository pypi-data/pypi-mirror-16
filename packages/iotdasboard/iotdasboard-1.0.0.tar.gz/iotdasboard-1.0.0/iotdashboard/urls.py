#-*- coding: utf-8 -*-
"""
URLs for iotdashboard project.
Django 1.9.7.
Python 2.7.12

https://iothook.com/
"""

from django.conf.urls import patterns, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView

from panels import views as panels
from devices import views as devices
from channels import views as channels
from elements import views as elements

urlpatterns = i18n_patterns(
    # backoffice panels index page
    url(r'^$', panels.index, name='panels_index'),

    # add devices
    url(r'^device/add/$', devices.device_add, name='device_add'),
    url(r'^device/list/$', devices.device_list, name='device_list'),
    url(r'^device/edit/(?P<id>[^/]*)/$', devices.device_edit, name='device_edit'),
    url(r'^device/delete/(?P<id>[^/]*)/$', devices.device_delete, name='device_delete'),

    # add channel
    url(r'^channel/add/$', channels.channel_add, name='channel_add'),
    url(r'^channel/list/$', channels.channel_list, name='channel_list'),
    url(r'^channel/edit/(?P<id>[^/]*)/$', channels.channel_edit, name='channel_edit'),
    url(r'^channel/delete/(?P<id>[^/]*)/$', channels.channel_delete, name='channel_delete'),

    # channel api key
    url(r'^key/list/$', channels.key_list, name='key_list'),
    url(r'^key/generate/(?P<id>[^/]*)/$', channels.generate_key, name='generate_key'),

    # add element
    url(r'^element/add/$', elements.element_add, name='element_add'),
    url(r'^element/list/$', elements.element_list, name='element_list'),
    url(r'^element/edit/(?P<id>[^/]*)/$', elements.element_edit, name='element_edit'),
    url(r'^element/delete/(?P<id>[^/]*)/$', elements.element_delete, name='element_delete'),

    # django admin page
    url(r'^admin/', admin.site.urls),
)

urlpatterns += [
    # favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

if settings.DEBUG == True:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]

if settings.DEBUG == False:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

