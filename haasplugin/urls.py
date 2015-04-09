"""
Definition of urls for haasplugin.
"""

from django.conf.urls import patterns, include, url
from haasplugin.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haasplugin.views.home', name='home'),
    # url(r'^haasplugin/', include('haasplugin.haasplugin.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'(?:.*?/)?(?P<path>(images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    url(r'^projects/details/freenodes/(?P<name>.+)', allocate_node),    
    url(r'^projects/details/(?P<name>.+)', project_details),
    url(r'^projects/(?P<name>.+)/detach_node', detach_node),
    url(r'^projects/create', project_create),
    url(r'^projects/delete', project_delete),
    url(r'^projects/', projects),
    url(r'^nodes/', nodes),
    url(r'^node/(?P<name>.+)', node_details),
    url(r'^networks/', networks),
    #url(r'^headnode/', headnode),
    url(r'^headnode/create', headnode_create),
    url(r'^$', projects),
  
)
