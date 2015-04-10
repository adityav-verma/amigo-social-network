from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
#user details:
class UserProfile(models.Model):
	 user = models.ForeignKey(User, unique=True)
	 fname = models.CharField(max_length = 120, null = False)
	 lname = models.CharField(max_length = 120, null = False)

	 dor = models.DateTimeField(auto_now_add = True, null=True)
	 dob = models.DateField(auto_now_add = False, auto_now = False, null = True)
	 genderChoice = (('male', 'male'), ('fmale', 'female'))
	 gender = models.CharField(max_length = 5, choices = genderChoice, default = 'male')

	 profilePic = models.ImageField(upload_to='profilePic', blank = True)


	 def __unicode__(self):
	 	return self.user.username

#model for a status update
class Status(models.Model):
	user = models.ForeignKey(User, unique=False)	#a user can have many status
	subject = models.CharField(max_length=60, null=True, blank=True	)
	body = models.TextField(null = False)
	pubDate = models.DateTimeField(auto_now_add=True, null=True)
	statusImage = models.ImageField(upload_to='statusImages', blank=True)
	like = models.IntegerField(default=0, null=False)
	disLike = models.IntegerField(default=0, null=False)
	comments = models.IntegerField(default=0, null=False)

	def __unicode__(self):
		return self.user.username


#model for friends
class Friends(models.Model):
	user1 = models.ForeignKey(User, related_name = "user1", null = True)
	user2 = models.ForeignKey(User, related_name = "user2", null = True)
	active = models.BooleanField(default=False)
	timeStamp = models.DateTimeField(auto_now_add=True, null=True)
