# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.db import transaction
from .models import Machine, Person, Field, Documentation, DocumentationFieldRelation
from .forms import MachineForm, PersonForm, FieldForm, DocumentationForm, DocumentationFieldRelationFormset
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator

def index(request):
	
	return render(request, 'core/index.html', {
		'data': 'data',
	})
	
def data(request):
	
	machines = Machine.objects.all
	
	return render(request, 'core/data/data.html', {
		'machines': 'machines',
	})

"""
	--------------------------------------------
	
	machines
	
	--------------------------------------------
"""

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

"""
	--------------------------------------------
	
	persons
	
	--------------------------------------------
"""

@method_decorator(login_required, name='dispatch')
class PersonList(ListView):
	"""
		view that displays a list of persons
	"""
	model = Person
	template_name = 'core/data/person_list.html'

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

"""
	--------------------------------------------
	
	fields
	
	--------------------------------------------
"""

@method_decorator(login_required, name='dispatch')
class FieldList(ListView):
	"""
		view that displays a list of fields
	"""
	model = Field
	template_name = 'core/data/field_list.html'

@method_decorator(login_required, name='dispatch')
class FieldCreate(CreateView):
	"""
		view that displays a create new field form
		- can be used in templates as {% url 'field_add' %}
	"""
	model = Field
	fields = ['name', 'area']
	template_name = 'core/data/field_form.html'
	success_url = reverse_lazy('field_list')
	
	def get_context_data(self, **kwargs):
		data = super(FieldCreate, self).get_context_data(**kwargs)
		return data
	
	def form_valid(self, form):
		with transaction.atomic():
			field = form.save(commit=False)
			field.owner = self.request.user
			field.save()
			self.object = field

		return super(FieldCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class FieldDetail(DetailView):
	"""
		view that displays a field 
		- can be used in templates as {% url 'field_detail' field.pk %}
	"""
	model = Field
	pk_url_kwarg = 'field_id'
	template_name = 'core/data/field_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(FieldDetail, self).get_context_data(**kwargs)
		#context['documentations'] = self.object.documentations()
		return context

@method_decorator(login_required, name='dispatch')
class FieldUpdate(UpdateView):
	"""
		view that displays an existing field form
		- can be used in templates as {% url 'field_edit' field.pk %}
	"""
	model = Field
	pk_url_kwarg = 'field_id'
	fields = ['name', 'area']
	template_name = 'core/data/field_form.html'
	success_url = reverse_lazy('field_list')
	
	def get_context_data(self, **kwargs):
		data = super(FieldUpdate, self).get_context_data(**kwargs)
		return data
	
	def form_valid(self, form):
		with transaction.atomic():
			field = form.save(commit=False)
			field.owner = self.request.user
			field.save()
			self.object = documentation
		return super(FieldUpdate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class FieldDelete(DeleteView):
	"""
		view that displays a delete confirmation
	"""
	model = Field
	pk_url_kwarg = 'field_id'
	template_name = 'core/data/field_confirm_delete.html'
	success_url = reverse_lazy('field_list')

"""
	--------------------------------------------
	
	documentations
	
	--------------------------------------------
"""

@method_decorator(login_required, name='dispatch')
class DocumentationList(ListView):
	"""
		view that displays a list of documentations
	"""
	model = Documentation
	template_name = 'core/documentations/documentation_list.html'

@method_decorator(login_required, name='dispatch')
class DocumentationCreate(CreateView):
	"""
		view that displays a create new documentation form
		- can be used in templates as {% url 'documentation_add' %}
	"""
	model = Documentation
	fields = ['date', 'duration', 'type']
	template_name = 'core/documentations/documentation_form.html'
	success_url = reverse_lazy('documentation_list')
	
	def get_context_data(self, **kwargs):
		data = super(DocumentationCreate, self).get_context_data(**kwargs)
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
		return super(DocumentationCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class DocumentationDetail(DetailView):
	"""
		view that displays a documentation 
		- can be used in templates as {% url 'documentation_detail' documentation.pk %}
	"""
	model = Documentation
	pk_url_kwarg = 'documentation_id'
	template_name = 'core/documentations/documentation_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(DocumentationDetail, self).get_context_data(**kwargs)
		#context['now'] = timezone.now()
		return context
	
@method_decorator(login_required, name='dispatch')
class DocumentationUpdate(UpdateView):
	"""
		view that displays an existing documentation form
		- can be used in templates as {% url 'documentation_edit' documentation.pk %}
	"""
	model = Documentation
	pk_url_kwarg = 'documentation_id'
	fields = ['date', 'duration', 'type']
	template_name = 'core/documentations/documentation_form.html'
	success_url = reverse_lazy('documentation_list')
	
	def get_context_data(self, **kwargs):
		data = super(DocumentationUpdate, self).get_context_data(**kwargs)
		if self.request.POST:
			data['fields'] = DocumentationFieldRelationFormset(self.request.POST, instance=self.object)
		else:
			data['fields'] = DocumentationFieldRelationFormset(instance=self.object)
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
		return super(DocumentationUpdate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class DocumentationDelete(DeleteView):
	"""
		view that displays a delete confirmation
	"""
	model = Documentation
	pk_url_kwarg = 'documentation_id'
	template_name = 'core/documentations/documentation_confirm_delete.html'
	success_url = reverse_lazy('documentation_list')
	

