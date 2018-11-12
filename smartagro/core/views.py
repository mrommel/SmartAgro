# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
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
	
def machine_detail(request, machine_id):
	
	try:
		machine = Machine.objects.get(pk=machine_id)
	except Machine.DoesNotExist:
		raise Http404("Machine does not exist")
	
	return render(request, 'core/machine_detail.html', {
		'machine': machine
	})
	
def machine_edit(request, machine_id):
	
	try:
		machine = Machine.objects.get(pk=machine_id)
	except Machine.DoesNotExist:
		raise Http404("Machine does not exist")
	
	if request.method == "POST":
		form = MachineForm(request.POST, instance=machine)
		if form.is_valid():
			machine = form.save(commit=False)
			# do something
			machine.save()
			return redirect('machine_detail', machine_id=machine.id)
	else:
		form = MachineForm(instance=machine)
	
	return render(request, 'core/machine_edit.html', {
		'form': form
	})
	

