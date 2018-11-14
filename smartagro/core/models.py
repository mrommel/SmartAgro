# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

"""
 Links
 https://wsvincent.com/django-referencing-the-user-model/
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
	
class Machine(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to='media/machines', blank=True, null=True)
	
	# preset from model
	type = models.CharField(max_length=1, choices=MACHINE_TYPES)
	horsepower = models.IntegerField(null=True, blank=True)
	volume = models.IntegerField(null=True, blank=True)
	width = models.IntegerField(null=True, blank=True)
	
	def thumbnail(self):
		if self.image.name is not None and self.image.name <> '':
			return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>' % ((self.image.name, self.image.name))
		else:
			return '<img border="0" alt="" src="/static/data/images/Person-icon-grey.JPG" height="40" />'
	thumbnail.allow_tags = True
	
	def __unicode__(self):
		return '%s' % (self.name)
	
class Person(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	image = models.ImageField(upload_to='media/persons', blank=True, null=True)
	
	def thumbnail(self):
		if self.image.name is not None and self.image.name <> '':
			return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>' % ((self.image.name, self.image.name))
		else:
			return '<img border="0" alt="" src="/static/data/images/Person-icon-grey.JPG" height="40" />'
	thumbnail.allow_tags = True
	
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)