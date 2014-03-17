from django.db import models
from django.contrib.auth.models import User


#this may need extended to offer more features/details
class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    collaborators = models.ManyToManyField(User)    
    #Project will also have list of developers represented by another model

    def __unicode__(self):
        return self.name


#this may need extended to offer more features/details
class Task(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    classification = models.CharField(max_length=1) # refers to the MoSCoW priority of the task
    priority = models.IntegerField() # integer priority of task within MoSCoW classification

    def __unicode__(self):
        return self.title
    
class UserProfile(models.Model):
	# pulls a standard user model from django https://docs.djangoproject.com/en/1.5/topics/auth/default/#user-objects
    user = models.OneToOneField(User)
	
	# which we extend
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
    
# class HistoryTask(models.Model):
#     task = models.ForeignKey(Task)
#     date = models.DateField(max_length=12)
#     
#     def __unicode__(self):
#         return self.date
