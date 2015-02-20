from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^frame', views.blockly_frame, name='blockly_frame'),
    url(r'^blockly_index', views.blockly_index, name='blockly_index'),
)