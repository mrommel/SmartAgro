# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.db import transaction
from .models import Machine, Person, Field, Documentation, DocumentationFieldRelation
from .forms import MachineForm, PersonForm, FieldForm, DocumentationForm, DocumentationFieldRelationFormset
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

def index(request):
	
	return render(request, 'core/index.html', {
		'data': 'data',
	})
	
def data(request):
	
	machines = Machine.objects.all
	
	return render(request, 'core/data/data.html', {
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
	
	return render(request, 'core/data/machines.html', {
		'form': form,
		'machines': machines
	})
	
def machine_detail(request, machine_id):
	
	try:
		machine = Machine.objects.get(pk=machine_id)
	except Machine.DoesNotExist:
		raise Http404("Machine does not exist")
	
	return render(request, 'core/data/machine_detail.html', {
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
	
	return render(request, 'core/data/machine_edit.html', {
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
	
	return render(request, 'core/data/persons.html', {
		'form': form,
		'persons': persons
	})

def person_detail(request, person_id):
	
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		raise Http404("Person does not exist")
	
	return render(request, 'core/data/person_detail.html', {
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
	
	return render(request, 'core/data/person_edit.html', {
		'form': form
	})

def fields(request):
	
	if request.method == 'POST':
		form = FieldForm(request.POST, request.FILES)
		if form.is_valid():
			field = form.save(commit=False)
			field.owner = request.user
			field.save()
	else:
		form = FieldForm()
		
	fields = Field.objects.all
	
	return render(request, 'core/data/fields.html', {
		'form': form,
		'fields': fields
	})

class DocumentationList(ListView):
	model = Documentation
	template_name = 'core/documentations/documentation_list.html'

class DocumentationFieldCreate(CreateView):
	model = Documentation
	fields = ['date', 'duration', 'type']
	template_name = 'core/documentations/documentation_form.html'
	success_url = reverse_lazy('documentation-list')
	
	def get_context_data(self, **kwargs):
		data = super(DocumentationFieldCreate, self).get_context_data(**kwargs)
		if self.request.POST:
			data['fields'] = DocumentationFieldRelationFormset(self.request.POST)
		else:
			data['fields'] = DocumentationFieldRelationFormset()
		return data
	
	def form_valid(self, form):
		context = self.get_context_data()
		fields = context['fields']
		with transaction.atomic():
			documentation = form.save(commit=False)
			documentation.owner = self.request.user
			documentation.save()
			self.object = documentation
			
			if fields.is_valid():
				fields.instance = self.object
				fields.save()
		return super(DocumentationFieldCreate, self).form_valid(form)
