# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Machine, Person
from .forms import MachineForm, PersonForm

def index(request):
	
	return render(request, 'core/index.html', {
		'data': 'data',
	})
	
def data(request):
	
	machines = Machine.objects.all
	
	return render(request, 'core/data.html', {
		'machines': 'machines',
	})

def machines(request):
	
	if request.method == 'POST':
		form = MachineForm(request.POST, request.FILES)
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
		form = MachineForm(request.POST, request.FILES, instance=machine)
		if form.is_valid():
			machine = form.save(commit=False)
			machine.owner = request.user
			# do something
			machine.save()
			return redirect('machine_detail', machine_id=machine.id)
	else:
		form = MachineForm(instance=machine)
	
	return render(request, 'core/machine_edit.html', {
		'form': form
	})
	
def persons(request):
	
	if request.method == 'POST':
		form = PersonForm(request.POST, request.FILES)
		if form.is_valid():
			person = form.save(commit=False)
			person.owner = request.user
			person.save()
	else:
		form = PersonForm()
		
	persons = Person.objects.all
	
	return render(request, 'core/persons.html', {
		'form': form,
		'persons': persons
	})

def person_detail(request, person_id):
	
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		raise Http404("Person does not exist")
	
	return render(request, 'core/person_detail.html', {
		'person': person
	})

def person_edit(request, person_id):
	
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		raise Http404("Person does not exist")
	
	if request.method == "POST":
		form = PersonForm(request.POST, request.FILES, instance=person)
		if form.is_valid():
			person = form.save(commit=False)
			person.owner = request.user
			# do something
			person.save()
			return redirect('person_detail', person_id=person.id)
	else:
		form = PersonForm(instance=person)
	
	return render(request, 'core/person_edit.html', {
		'form': form
	})