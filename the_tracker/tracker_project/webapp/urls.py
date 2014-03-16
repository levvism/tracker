from django.conf.urls import patterns, url
from webapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url( r'^about/', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^newproject/$', views.new_project, name='newproject'),
        url(r'^project/$', views.project, name='project'),
        url(r'^requirements/$', views.requirement, name='requirement'),
        url(r'^add_requirement/$', views.add_task, name='add_task'),
)
        


