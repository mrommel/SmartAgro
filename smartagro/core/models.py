# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from operator import attrgetter
from django.core.urlresolvers import reverse

"""
 	Links
	* https://wsvincent.com/django-referencing-the-user-model/
"""

"""
--------------------------------------------------------------
	user related data
--------------------------------------------------------------
"""

class Manufacturer(models.Model):
	name = models.CharField(max_length=64)
	description = models.CharField(max_length=512, null=True, blank=True)
	
	def __unicode__(self):
		return '%s' % (self.name)

MACHINE_TYPES = (('T', _('Tractor')), ('I', _('Implement')), ('H', _('Harvester')))

class Model(models.Model):
	name = models.CharField(max_length=64)
	manufacturer = models.ForeignKey(Manufacturer)
	
	# used as preset
	type = models.CharField(max_length=1, choices=MACHINE_TYPES)
	horsepower = models.IntegerField(null=True, blank=True)
	volume = models.IntegerField(null=True, blank=True)
	width = models.IntegerField(null=True, blank=True)
	
	def __unicode__(self):
		return '%s' % (self.name)

FERTILIZER_TYPES = (('O', _('Organic')), ('M', _('Mineralic')))

class Fertilizer(models.Model):
	name = models.CharField(max_length=64)
	type = models.CharField(max_length=1, choices=FERTILIZER_TYPES)
	
	def __unicode__(self):
		return '%s' % (self.name)

class CultureType(models.Model):
	name = models.CharField(max_length=64)
	abbreviation = models.CharField(max_length=2)
	
	def __unicode__(self):
		return '%s' % (self.name)
		
class Culture(models.Model):
	name = models.CharField(max_length=64)
	type = models.ForeignKey(CultureType)
	
	def __unicode__(self):
		return '%s - %s' % (self.name, self.type.name)

class Seed(models.Model):
	name = models.CharField(max_length=64)
	culture = models.ForeignKey(Culture)
	
	def __unicode__(self):
		return '%s - %s' % (self.name, self.culture.name)

class PlantProtectantCategory(models.Model):
	name = models.CharField(max_length=64)
	
	def __unicode__(self):
		return '%s' % (self.name)
	
class PlantProtectant(models.Model):
	name = models.CharField(max_length=64)
	category = models.ForeignKey(PlantProtectantCategory)
	valid_cultures = models.ManyToManyField(Culture)
	
	def __unicode__(self):
		return '%s - %s' % (self.name, self.category.name)

"""
--------------------------------------------------------------
	user related data
--------------------------------------------------------------
"""

class Machine(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to='media/machines', blank=True, null=True)
	
	# preset from model (can be changed)
	type = models.CharField(max_length=1, choices=MACHINE_TYPES)
	horsepower = models.IntegerField(null=True, blank=True)
	volume = models.IntegerField(null=True, blank=True)
	width = models.IntegerField(null=True, blank=True)
	
	def thumbnail(self):
		"""
			Returns an extendable version of the 'image' of this machine as html or a default image
		"""
		if self.image.name is not None and self.image.name <> '':
			return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>' % ((self.image.name, self.image.name))
		else:
			return '<img border="0" alt="" src="/static/core/images/machine-icon-grey.JPG" height="40" />'
	thumbnail.allow_tags = True
	
	def get_absolute_url(self):
		"""
			Returns the url to access a particular machine instance.
		"""
		return reverse('machine_detail', args=[str(self.id)])
	
	def __unicode__(self):
		return '%s' % (self.name)
	
class Person(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	image = models.ImageField(upload_to='media/persons', blank=True, null=True)
	
	def thumbnail(self):
		"""
			Returns an extendable version of the 'image' of this person as html or a default image
		"""
		if self.image.name is not None and self.image.name <> '':
			return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>' % ((self.image.name, self.image.name))
		else:
			return '<img border="0" alt="" src="/static/core/images/person-icon-grey.JPG" height="40" />'
	thumbnail.allow_tags = True
	
	def get_absolute_url(self):
		"""
			Returns the url to access a particular person instance.
		"""
		return reverse('person_detail', args=[str(self.id)])
	
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)
		
class Field(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	area = models.IntegerField()
	
	def documentations(self):
		"""
			Returns the documentations that happend on that field
			- ordered by date
		"""
		documentationArray = []
		
		for fieldRelation in DocumentationFieldRelation.objects.filter(field = self):
			documentationArray.append(fieldRelation.documentation)
		
		documentationArray = sorted(documentationArray, key=attrgetter('date'), reverse=False)
		
		return documentationArray
	
	def get_absolute_url(self):
		"""
			Returns the url to access a particular field instance.
		"""
		return reverse('field_detail', args=[str(self.id)])
	
	def __unicode__(self):
		return '%s - %d ha' % (self.name, self.area)
	
class FertilizerRelation(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	fertilizer = models.ForeignKey(Fertilizer)
	active = models.NullBooleanField(default=False)
	
	def __unicode__(self):
		return '%s - %s' % (self.fertilizer.name, self.active)
		
class SeedRelation(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	seed = models.ForeignKey(Seed)
	active = models.NullBooleanField(default=False)
	
	def __unicode__(self):
		return '%s - %s' % (self.seed.name, self.active)
		
class PlantProtectantRelation(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	plant_protectant = models.ForeignKey(PlantProtectant)
	active = models.NullBooleanField(default=False)
	
	def __unicode__(self):
		return '%s - %s' % (self.plant_protectant.name, self.active)
	
DOCUMENTATION_TYPES = (('W', _('Plowing')), ('S', _('Sowing')), ('H', _('Harvesting')), ('F', _('Fertilization')), ('C', _('Cropcare')), ('P', _('Plantprotect')), )
DOCUMENTATION_STATUS = (('P', _('Planned')), ('S', _('Saved')), ('B', _('Booked')))

class Documentation(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	duration = models.IntegerField() # in minutes
	type = models.CharField(max_length=1, choices=DOCUMENTATION_TYPES)
	status = models.CharField(max_length=1, choices=DOCUMENTATION_STATUS)
	comments = models.CharField(max_length=64)
	
	def get_absolute_url(self):
		"""
			Returns the url to access a particular documentation instance.
		"""
		return reverse('documentation_detail', args=[str(self.id)])
	
	def fields(self):
		fieldArray = []
	
		for fieldRelation in DocumentationFieldRelation.objects.filter(documentation = self):
			fieldArray.append(fieldRelation.field)
		
		return fieldArray
		
	def machines(self):
		machineArray = []
		
		for machineRelation in DocumentationMachineRelation.objects.filter(documentation = self):
			machineArray.append(machineRelation.machine)
		
		return machineArray
		
	def persons(self):
		personArray = []
		
		for personRelation in DocumentationPersonRelation.objects.filter(documentation = self):
			personArray.append(personRelation.person)
		
		return personArray
		
	def fertilizers(self):
		fertilizerArray = []
		
		for fertilizerRelation in DocumentationFertilizerRelation.objects.filter(documentation = self):
			fertilizerArray.append(fertilizerRelation.fertilizer)
		
		return fertilizerArray
	
	def __unicode__(self):
		return '%s - %s' % (self.date, self.type)
		
class DocumentationFieldRelation(models.Model):
	documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
	field = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True, null=True)
	
	def __unicode__(self):
		return '%s - %s' % (self.documentation, self.field)
	
class DocumentationMachineRelation(models.Model):
	documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
	machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
	
	def __unicode__(self):
		return '%s - %s' % (self.documentation, self.machine)
	
class DocumentationPersonRelation(models.Model):
	documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	
	def __unicode__(self):
		return '%s - %s' % (self.documentation, self.person)
		
class DocumentationFertilizerRelation(models.Model):
	documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
	fertilizer = models.ForeignKey(FertilizerRelation, on_delete=models.CASCADE)
	amount = models.IntegerField()
	
	def __unicode__(self):
		return '%s - %s' % (self.documentation, self.fertilizer)