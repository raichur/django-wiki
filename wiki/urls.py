from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^articles/', include('article.urls')),
)
