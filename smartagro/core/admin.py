# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Manufacturer, Model, Machine

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Machine)