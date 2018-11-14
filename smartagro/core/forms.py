from django.db import models
from django.forms import modelformset_factory
from django.forms import ModelForm
from django.contrib import admin

from core.models import Machine, Person, Field, Documentation, DocumentationFieldRelation

# https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/

class MachineForm(ModelForm):
	class Meta:
		model = Machine
		fields = ['name', 'model', 'image']
		
class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['first_name', 'last_name', 'image']
		
class FieldForm(ModelForm):
	class Meta:
		model = Field
		fields = ['name', 'area']

DocumentationFieldFormset = modelformset_factory(DocumentationFieldRelation, fields=('field', ), extra=1,)

class DocumentationForm(ModelForm):
	class Meta:
		model = Documentation
		fields = ['date', 'duration', 'type']
		