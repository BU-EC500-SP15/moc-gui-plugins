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
    url(r'^projects/details/freenodes/(?P<name>.+)', allocNodes),    
    url(r'^projects/details/(?P<name>.+)', projectDetails),
    url(r'^projects/create', createProject),
    url(r'^projects/delete', deleteProject),
    url(r'^projects/', projects),
    url(r'^nodes/', allNodes),
    url(r'^networks/', allNetworks),
    url(r'^$', projects),
  
)
