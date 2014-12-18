from django.conf.urls import patterns, url

from projects import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^twitter_license', views.twitter_license, name='twitter_license'),
    url(r'^django_license', views.django_license, name='django_license'),
    url(r'^profile_page/(?P<username>\w+)', views.profile_page, name ='profile_page'),
    url(r'^category_page/(?P<category>\w+)', views.category_page, name ='category_page'),
    url(r'^like_project', views.like_project, name='like_project'),
    url(r'^project_viewer/(?P<category>\w+)/(?P<id>[\d-]+)/(?P<slug>[\w-]+)', views.project_viewer, name ='project_viewer')
)