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
    url(r'^projects/(?P<name>.+)/attach_node', allocate_node), #change allocate_node to attach_node and modify it in views.py  
    url(r'^projects/(?P<name>.+)/assign_headnode', allocate_node),  #change allocate_node to attach_headnode and modify it in views.py  
    url(r'^projects/(?P<name>.+)/detach_node', detach_node),
    url(r'^projects/(?P<name>.+)/detach_headnode', detach_node),  #change detach_node to detach_headnode and create it in views.py
    url(r'^project_create', project_create),
    url(r'^project_delete', project_delete),
    url(r'^node_create', node_create), #change project_create to node_create here and create it in views.py
    url(r'^node_delete', node_delete), #change project_delete to node_delete here and create it in views.py
    #url(r'^network_create', network_create), #change project_create to network_create here and create it in views.py
    #url(r'^network_delete', network_delete), #change project_delete to network_delete here and create it in views.py
    url(r'^projects/(?P<name>.+)', project_details),
    url(r'^nodes/(?P<name>.+)/node_register_nic', node_register_nic),
    url(r'^nodes/(?P<name>.+)/power_cycle', node_powercycle),
    url(r'^nodes/(?P<name>.+)', node_details), 
    #url(r'^networks/(?P<name>.+)', network_details), #change project_details to network_details here and create it in views.py
    url(r'^projects/', projects),
    url(r'^nodes/', nodes),
    url(r'^networks/', networks),
    url(r'^headnode/create', headnode_create), # remove this and fix projects/assign
    url(r'^$', projects),
  
)
