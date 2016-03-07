from django.conf.urls import patterns, include, url
from qa.view import test

urlpatterns = patterns('',
    url(r'^$', list_qw, name='list-qw'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    url(r'^popular/', list_popular, name='list-popular'),
    url(r'^new/', test),
    url(r'^question/(?P<slug>\d+)/', show_question, name='show-question'),
)
