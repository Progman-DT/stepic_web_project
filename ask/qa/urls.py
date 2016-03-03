from django.conf.urls import patterns, include, url
from django.contrib import admin
from qa.views import test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(admin.site.urls)),
    url(r'^login/', include(admin.site.urls)),
    url(r'^signup/', include(admin.site.urls)),
    url(r'^question/\d+/', test, name='test'),
    url(r'^ask/', include(admin.site.urls)),
    url(r'^popular/', include(admin.site.urls)),
    url(r'^new/', include(admin.site.urls)),
)
