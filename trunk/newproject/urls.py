from django.conf.urls.defaults import *
import settings
import os.path

from django.contrib import admin
admin.autodiscover()

from common.models import Page
from django.contrib.sitemaps import GenericSitemap

#---------------------------------------

info_dict = {
    'queryset': Page.objects.all()
}

sitemaps = {
    'pages': GenericSitemap(info_dict, priority=0.7)
}

urlpatterns = patterns('',
    (r'^filemanager_connectors/', include('vendor.filemanager.connector.urls')),
    (r'^admin/(.*)', admin.site.root),
)

urlpatterns += patterns('common.views',
    url(r'^$', 'home', name="home"),

    url(r'^gallery/$', 'gallery', name="gallery"),

    url(r'^contact-us/$', 'contact', name="contact"),

    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', 'page', name="page_item"),
)

urlpatterns += patterns('',
#    (r'^fckeditor_connector/', include('vendor.fckeditor.connector.urls')),
    (r'^robots.txt$', 'django.views.static.serve', { 'path' : "/static/robots.txt", 'document_root': settings.PROJECT_DIR, 'show_indexes': False } ),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^favicon.ico$', 'django.views.static.serve', { 'path' : "/static/icons/favicon.ico", 'document_root': settings.PROJECT_DIR, 'show_indexes': False } ),
)


if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': os.path.join(os.path.dirname(__file__), 'static'), 'show_indexes': True } ),
    )