# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class maplist(models.Model):	
	mapName = models.CharField(max_length=60, null=False)
	mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	mapTel = models.CharField(max_length=20, null=False)
	mapAddr = models.CharField(max_length=60, null=False)
	
	def __str__(self):		
		return self.mapName	
class maplist1(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	mapDesc = models.TextField(null=False)	
	mapLat= models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	mapTel = models.CharField(max_length=20, null=False)
	mapAddr = models.CharField(max_length=60, null=False)

	def __str__(self):		
		return self.mapName

