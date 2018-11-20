# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Manufacturer, Model, Fertilizer, PlantProtectant, PlantProtectantCategory, CultureType, Culture, Seed, Machine, Person, Field, FertilizerRelation

# Register your models here.

# general data
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Fertilizer)
admin.site.register(PlantProtectant)
admin.site.register(PlantProtectantCategory)
admin.site.register(CultureType)
admin.site.register(Culture)
admin.site.register(Seed)

# user data
admin.site.register(Machine)
admin.site.register(Person)
admin.site.register(Field)
admin.site.register(FertilizerRelation)