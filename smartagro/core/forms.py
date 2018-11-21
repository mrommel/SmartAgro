from django.db import models
from django.forms import inlineformset_factory
from django.forms import ModelForm
from django.contrib import admin
from django import forms
import re # regular expression library

from core.models import Machine, Person, Field, Documentation, DocumentationFieldRelation, DocumentationMachineRelation, DocumentationPersonRelation, DocumentationFertilizerRelation

# https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/

class FertilizerActivationForm(forms.Form):
	fertilizer_id = forms.CharField(max_length=10, required=True)
	activated = forms.CharField(max_length=255, required=True)

class PlantProtectantActivationForm(forms.Form):
	plant_protectant_id = forms.CharField(max_length=10, required=True)
	activated = forms.CharField(max_length=255, required=True)

class SeedActivationForm(forms.Form):
	seed_id = forms.CharField(max_length=10, required=True)
	activated = forms.CharField(max_length=255, required=True)

class DocumentationFieldRelationForm(ModelForm):
	class Meta:
		model = DocumentationFieldRelation
		exclude = ()
		
class DocumentationMachineRelationForm(ModelForm):
	class Meta:
		model = DocumentationMachineRelation
		exclude = ()
		
class DocumentationPersonRelationForm(ModelForm):
	class Meta:
		model = DocumentationPersonRelation
		exclude = ()
		
class DocumentationFertilizerRelationForm(ModelForm):
	class Meta:
		model = DocumentationFertilizerRelation
		exclude = ()

DocumentationFieldRelationFormset = inlineformset_factory(Documentation, DocumentationFieldRelation, form=DocumentationFieldRelationForm, extra=1)
DocumentationMachineRelationFormset = inlineformset_factory(Documentation, DocumentationMachineRelation, form=DocumentationMachineRelationForm, extra=1)
DocumentationPersonRelationFormset = inlineformset_factory(Documentation, DocumentationPersonRelation, form=DocumentationPersonRelationForm, extra=1)
DocumentationFertilizerRelationFormset = inlineformset_factory(Documentation, DocumentationFertilizerRelation, form=DocumentationFertilizerRelationForm, extra=1)