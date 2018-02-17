from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
	''' Attributes '''
	name = models.CharField(max_length=128) 
	project_title = models.CharField(max_length=128) 
	project_description = models.CharField(max_length=4096) 
	hackers = models.CharField(max_length=256)
	
