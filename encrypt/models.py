# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User_conf(models.Model):
    pass

class Hash(models.Model):
    user = models.ForeignKey(User_conf)
    data = models.TextField()
