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
        url(r'^project/view_tasks$', views.view_tasks, name='all_task'),
        url(r'^project/add_task$', views.add_task, name='add_task'),
        url(r'^project/task$', views.task, name='task'),
        url(r'^project/edit_task$', views.edit_task, name='edit_task'),
        url(r'^project/history_task/$', views.history_task, name='history_task'),
)
        


