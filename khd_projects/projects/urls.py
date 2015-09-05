from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^twitter_license', views.twitter_license, name='twitter_license'),
    url(r'^gfdl_license', views.gfdl_license, name='gfdl_license'),
    url(r'^django_license', views.django_license, name='django_license'),
    url(r'^profile_page/(?P<username>\w+)', views.profile_page, name ='profile_page'),
    url(r'^information_article/(?P<id>\w+)', views.information_article, name ='information_article'),
    url(r'^getting_started', views.getting_started, name ='getting_started'),
    url(r'^faq', views.faq, name ='faq'),
    url(r'^edit_profile', views.edit_profile, name ='edit_profile'),
    url(r'^delete_projects', views.delete_projects, name ='delete_projects'),
    url(r'^add_project', views.add_project, name='add_project'),
    url(r'^edit_projects_page', views.edit_projects_page, name ='edit_projects_page'),
    url(r'^edit_project/(?P<id>[\d-]+)', views.edit_project, name ='edit_project'),
    url(r'^category_page/(?P<category>\w+)', views.category_page, name ='category_page'),
    url(r'^user_login', views.user_login, name='user_login'),
    url(r'^user_logout', views.user_logout, name='user_logout'),
    url(r'^project_viewer/(?P<category>\w+)/(?P<id>[\d-]+)/(?P<slug>[\w-]+)', views.project_viewer, name ='project_viewer')
)