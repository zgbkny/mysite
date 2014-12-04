# coding=utf-8
from django.conf.urls import patterns, url
from ticketx.views import *

urlpatterns = patterns('',
    url(r'^login', index),
    url(r'^register', register),
    #url(r'^loginVerify', loginVerify),
    url(r'^static/(?P<path>.*)$','static'),
    url(r'^$', index),
)
