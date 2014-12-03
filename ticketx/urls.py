# coding=utf-8
from django.conf.urls import patterns, url
from ticketx.views import *

urlpatterns = patterns('',
    url(r'^login', login),
    url(r'^register', register),
    #url(r'^loginVerify', loginVerify),
    url(r'^$', login),
)
