# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Machine
from .forms import MachineForm

def index(request):
	
	return render(request, 'core/index.html', {
		'data': 'data',
	})
	
def machines(request):
	if request.method == 'POST':
		form = MachineForm(request.POST)
		if form.is_valid():
			machine = form.save(commit=False)
			machine.owner = request.user
			machine.save()
	else:
		form = MachineForm()
		
	machines = Machine.objects.all
	
	return render(request, 'core/machines.html', {
		'form': form,
		'machines': machines
	})