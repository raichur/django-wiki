from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
)
