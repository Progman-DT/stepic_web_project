from django.conf.urls import patterns, include, url
from qa.views import *

urlpatterns = patterns('',
    url(r'^$', list_qw, name='list-qw'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^new/', test),
    url(r'^ask/', post_question, name='post_question'),
    url(r'^answer/', post_answer, name='post_answer'),
    url(r'^popular/', list_popular, name='list-popular'),
    url(r'^question/(?P<slug>\w+)/$', show_question, name='show-question'),
)
