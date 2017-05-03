# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer
# Register your models here.
class ResourceAdmin(admin.ModelAdmin):
  list_display = ('id', 'password')

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(Customer, ResourceAdmin)
