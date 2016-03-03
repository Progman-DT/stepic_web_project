from django.conf.urls import patterns, include, url
#from django.contrib import admin
from qa.views import test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', test, name='test'),
    url(r'^login/', test, name='test'),
    url(r'^signup/', test, name='test'),
    url(r'^question/\d+/', test, name='test'),
    url(r'^ask/', test, name='test'),
    url(r'^popular/', test, name='test'),
    url(r'^new/', test, name='test'),
)
