# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Manufacturer, Model, Machine, Person, Field

# Register your models here.

# general data
admin.site.register(Manufacturer)
admin.site.register(Model)

# user data
admin.site.register(Machine)
admin.site.register(Person)
admin.site.register(Field)