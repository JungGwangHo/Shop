# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
        id = models.CharField(max_length=200, primary_key=True )
        password = models.CharField(max_length=200)
        email = models.TextField()
        phone = models.CharField(max_length=10)
        zip_code = models.CharField(max_length=7)
        address = models.TextField()
        job = models.TextField()
        reg_date = models.DateTimeField(
                default=timezone.now)
        authority = '0'

        def getId(self):
            return self.id
        def getpassword(self):
            return self.password
        def getauthority(self):
            return self.authority