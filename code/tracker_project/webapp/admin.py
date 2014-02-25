from django.contrib import admin
from webapp.models import Project,Task,UserProfile,UsersProjects

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(UsersProjects)
