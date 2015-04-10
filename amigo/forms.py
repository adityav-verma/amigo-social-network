from django import forms
from amigo.models import UserProfile, Status
from django.contrib.auth.models import User

#form for updating the user profile after registration
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('dor', 'user', 'dob',)

#form for status update of a user
class StatusForm(forms.ModelForm):
	class Meta:
		model = Status
		exclude = ('like', 'disLike', 'user', 'pubDate', 'comments')
