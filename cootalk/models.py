# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Inventory(models.Model):
    nid = models.AutoField(primary_key=True)
    ip_addr = models.CharField(max_length=64)
    config_dir = models.CharField(max_length=256,default='/usr/local/tomcat/')
    ssh_port = models.IntegerField()
    app = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    is_config = models.BooleanField(default=False)
