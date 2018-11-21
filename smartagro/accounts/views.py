# -*- coding: utf-8 -*-
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProfileChangeForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
		
	return render(request, 'accounts/signup.html', {'form': form})
	
@login_required 
def profile(request):

	if request.method == 'POST':
		form = ProfileChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	else:
		form = ProfileChangeForm(instance=request.user)
	
	return render(request, 'accounts/profile.html', {
		'form': form
	})