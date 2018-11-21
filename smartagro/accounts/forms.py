from django import forms
from django.contrib.auth.forms import UserChangeForm  
from django.contrib.auth.models import User  

class ProfileChangeForm(UserChangeForm):
	"""
		Overriding visible fields.
	"""
	class Meta:
		model = User
		fields = ('username', 'password', 'email', 'first_name', 'last_name',)