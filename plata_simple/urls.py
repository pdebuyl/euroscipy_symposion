import os

from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.shortcuts import redirect

from plata_simple.views import shop


admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include(shop.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', lambda request: redirect('plata_product_list'), name='plata_root'),
    url(r'^products/$', 'plata_simple.views.product_list',
        name='plata_product_list'),
    url(r'^products/(?P<object_id>\d+)/$', 'plata_simple.views.product_detail',
        name='plata_product_detail'),

    url(r'^reporting/', include('plata.reporting.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'media/')}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
