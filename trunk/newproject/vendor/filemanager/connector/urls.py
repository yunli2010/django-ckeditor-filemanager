from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^dirlist/$', 'vendor.filemanager.connector.views.dirlist'),
    (r'^$', 'vendor.filemanager.connector.views.handler'),
)
