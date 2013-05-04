from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fundstrap.views.home', name='home'),
    # url(r'^fundstrap/', include('fundstrap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
