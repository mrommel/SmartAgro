# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Manufacturer, Model, Fertilizer, Plantprotectant, PlantprotectantCategory, CultureType, Culture, Seed, Machine, Person, Field

# Register your models here.

# general data
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Fertilizer)
admin.site.register(Plantprotectant)
admin.site.register(PlantprotectantCategory)
admin.site.register(CultureType)
admin.site.register(Culture)
admin.site.register(Seed)

# user data
admin.site.register(Machine)
admin.site.register(Person)
admin.site.register(Field)