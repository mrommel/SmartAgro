# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.db import transaction
from .models import Machine, Person, Field, FertilizerRelation, Documentation, DocumentationFieldRelation, DocumentationMachineRelation, DocumentationPersonRelation
from .forms import DocumentationFieldRelationFormset, DocumentationMachineRelationFormset, DocumentationPersonRelationFormset, FertilizerActivationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.http import JsonResponse

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

@method_decorator(login_required, name='dispatch')
class MachineList(ListView):
	"""
		view that displays a list of machines
		- can be used in templates as {% url 'machine_list' %}
	"""
	model = Machine
	template_name = 'core/data/machine_list.html'

@method_decorator(login_required, name='dispatch')
class MachineCreate(CreateView):
	"""
		view that displays a create new machine form
		- can be used in templates as {% url 'machine_add' %}
	"""
	model = Machine
	fields = ['name', 'model']
	template_name = 'core/data/machine_form.html'
	success_url = reverse_lazy('machine_list')
	
	def get_context_data(self, **kwargs):
		data = super(MachineCreate, self).get_context_data(**kwargs)
		return data
	
	def form_valid(self, form):
		with transaction.atomic():
			machine = form.save(commit=False)
			machine.owner = self.request.user
			machine.save()
			self.object = machine

		return super(MachineCreate, self).form_valid(form)
		
@method_decorator(login_required, name='dispatch')
class MachineDetail(DetailView):
	"""
		view that displays a machine 
		- can be used in templates as {% url 'machine_detail' person.pk %}
	"""
	model = Machine
	pk_url_kwarg = 'machine_id'
	template_name = 'core/data/machine_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(MachineDetail, self).get_context_data(**kwargs)
		#context['documentations'] = self.object.documentations()
		return context

@method_decorator(login_required, name='dispatch')
class MachineUpdate(UpdateView):
	"""
		view that displays an existing machine form
		- can be used in templates as {% url 'machine_edit' machine.pk %}
	"""
	model = Machine
	pk_url_kwarg = 'machine_id'
	fields = ['name', 'model']
	template_name = 'core/data/machine_form.html'
	success_url = reverse_lazy('machine_list')
	
	def get_context_data(self, **kwargs):
		data = super(MachineUpdate, self).get_context_data(**kwargs)
		return data
	
	def form_valid(self, form):
		with transaction.atomic():
			machine = form.save(commit=False)
			machine.owner = self.request.user
			machine.save()
			self.object = machine
		return super(MachineUpdate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class MachineDelete(DeleteView):
	"""
		view that displays a delete confirmation
	"""
	model = Machine
	pk_url_kwarg = 'machine_id'
	template_name = 'core/data/machine_confirm_delete.html'
	success_url = reverse_lazy('machine_list')

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

@method_decorator(login_required, name='dispatch')
class PersonCreate(CreateView):
	"""
		view that displays a create new person form
		- can be used in templates as {% url 'person_add' %}
	"""
	model = Person
	fields = ['first_name', 'last_name', 'image']
	template_name = 'core/data/person_form.html'
	success_url = reverse_lazy('person_list')
	
	def get_context_data(self, **kwargs):
		data = super(PersonCreate, self).get_context_data(**kwargs)
		return data
	
	def form_valid(self, form):
		with transaction.atomic():
			field = form.save(commit=False)
			field.owner = self.request.user
			field.save()
			self.object = field

		return super(PersonCreate, self).form_valid(form)
		
@method_decorator(login_required, name='dispatch')
class PersonDetail(DetailView):
	"""
		view that displays a person 
		- can be used in templates as {% url 'person_detail' person.pk %}
	"""
	model = Person
	pk_url_kwarg = 'person_id'
	template_name = 'core/data/person_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(PersonDetail, self).get_context_data(**kwargs)
		#context['documentations'] = self.object.documentations()
		return context

@method_decorator(login_required, name='dispatch')
class PersonUpdate(UpdateView):
	"""
		view that displays an existing field form
		- can be used in templates as {% url 'person_edit' person.pk %}
	"""
	model = Person
	pk_url_kwarg = 'person_id'
	fields = ['first_name', 'last_name', 'image']
	template_name = 'core/data/person_form.html'
	success_url = reverse_lazy('person_list')
	
	def get_context_data(self, **kwargs):
		data = super(PersonUpdate, self).get_context_data(**kwargs)
		return data
	
	def form_valid(self, form):
		with transaction.atomic():
			person = form.save(commit=False)
			person.owner = self.request.user
			person.save()
			self.object = person
		return super(PersonUpdate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class PersonDelete(DeleteView):
	"""
		view that displays a delete confirmation
	"""
	model = Person
	pk_url_kwarg = 'person_id'
	template_name = 'core/data/person_confirm_delete.html'
	success_url = reverse_lazy('person_list')

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
			self.object = field
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
	
	fertilizer
	
	--------------------------------------------
"""

@method_decorator(login_required, name='dispatch')
class FertilizerList(ListView):
	"""
		view that displays a list of fertilizer relations
	"""
	model = FertilizerRelation
	template_name = 'core/data/fertilizerrelation_list.html'

@require_http_methods(['POST'])
def fertilizer_activate(request):
		
	form = FertilizerActivationForm(request.POST)
	if form.is_valid():
		fertilizer_id = form.cleaned_data.get('fertilizer_id')
		activated = form.cleaned_data.get('activated')
		user = request.user
		
		try:
			fertilizerRelation = FertilizerRelation.objects.get(pk=fertilizer_id, owner=user)
			fertilizerRelation.active = activated
			fertilizerRelation.save()
		except FertilizerRelation.DoesNotExist:
			raise Http404("FertilizerRelation does not exist")
		
		return JsonResponse({"message": "form: %s - %s" % (fertilizerRelation.fertilizer.id, activated)}, status=201)
		#return JsonResponse({"message": "form is submitted: %s - %s" % (fertilizer_id, activated)}, status=201)
	
	return JsonResponse({"error": "invalid input"}, status=400)
	#user = request.user
	#	
	#try:
	#	fertilizerRelation = FertilizerRelation.objects.get(pk=fertilizer_id, owner=user)
	#except FertilizerRelation.DoesNotExist:
	#	raise Http404("FertilizerRelation does not exist")
	
	#if request.POST:
	#	fertilizerRelation.active = active
	#	fertilizerRelation.save()
	
	#return HttpResponse('')

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
			data['machines'] = DocumentationMachineRelationFormset(self.request.POST, instance=self.object)
			data['persons'] = DocumentationPersonRelationFormset(self.request.POST, instance=self.object)
		else:
			data['fields'] = DocumentationFieldRelationFormset()
			data['machines'] = DocumentationMachineRelationFormset(instance=self.object)
			data['persons'] = DocumentationPersonRelationFormset(instance=self.object)
			
		return data
	
	def form_valid(self, form):
		context = self.get_context_data()
		fields = context['fields']
		machines = context['machines']
		persons = context['persons']
		
		with transaction.atomic():
			documentation = form.save(commit=False)
			documentation.owner = self.request.user
			documentation.save()
			self.object = documentation
			
			if fields.is_valid():
				fields.instance = self.object
				fields.save()
			
			if machines.is_valid():
				machines.instance = self.object
				machines.save()
				
			if persons.is_valid():
				persons.instance = self.object
				persons.save()
				
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
			data['machines'] = DocumentationMachineRelationFormset(self.request.POST, instance=self.object)
			data['persons'] = DocumentationPersonRelationFormset(self.request.POST, instance=self.object)
		else:
			data['fields'] = DocumentationFieldRelationFormset(instance=self.object)
			data['machines'] = DocumentationMachineRelationFormset(instance=self.object)
			data['persons'] = DocumentationPersonRelationFormset(instance=self.object)
			
		return data
	
	def form_valid(self, form):
		context = self.get_context_data()
		fields = context['fields']
		machines = context['machines']
		persons = context['persons']
		
		with transaction.atomic():
			documentation = form.save(commit=False)
			documentation.owner = self.request.user
			documentation.save()
			self.object = documentation
			
			if fields.is_valid():
				fields.instance = self.object
				fields.save()
			
			if machines.is_valid():
				machines.instance = self.object
				machines.save()
				
			if persons.is_valid():
				persons.instance = self.object
				persons.save()
				
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
	

