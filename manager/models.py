from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.

class Manager(models.Model):
	id          = models.AutoField(primary_key=True)
	name        = models.CharField(max_length=256)
	fqdn        = models.CharField(max_length=256)
	url         = models.CharField(max_length=512)
	username    = models.CharField(max_length=64)
	password    = models.CharField(max_length=64)
	version     = models.CharField(max_length=16)
	discovered  = models.DateTimeField(editable=False)
	updated     = models.DateTimeField()

class DataCenter(models.Model):
	id          = models.AutoField(primary_key=True)
	dcid        = models.CharField(max_length=128,null=True)
	name        = models.CharField(max_length=256)
	manager     = models.ForeignKey('Manager')
	discovered  = models.DateTimeField(editable=False)
	updated     = models.DateTimeField()

class Cluster(models.Model):
	id          = models.AutoField(primary_key=True)
	clid        = models.CharField(max_length=128,null=True)
	name        = models.CharField(max_length=256)
	dc          = models.ForeignKey('DataCenter')	
	discovered  = models.DateTimeField(editable=False)
	updated     = models.DateTimeField()

class VM(models.Model):
	id          = models.AutoField(primary_key=True)
	cluster     = models.ForeignKey('Cluster')
	name        = models.CharField(max_length=256)
	vmid        = models.CharField(max_length=128)
	discovered  = models.DateTimeField(editable=False)
	updated     = models.DateTimeField()
	status      = models.CharField(max_length=16)
	protected   = models.BooleanField(default=False)
	size        = models.BigIntegerField(default=0)
	

class StorageDomain(models.Model):
	id          = models.AutoField(primary_key=True)
	sdid        = models.CharField(max_length=128)
	name        = models.CharField(max_length=256)
	type        = models.CharField(max_length=16)
	status      = models.CharField(max_length=16)
	
class VmBackups(models.Model):
	id          = models.AutoField(primary_key=True)
	vmid        = models.ForeignKey('VM')
	name        = models.CharField(max_length=256)
	export      = models.CharField(max_length=64)
	status      = models.IntegerField(default=3)
	start       = models.DateTimeField(null=True)
	end         = models.DateTimeField(null=True)
	updated     = models.DateTimeField(auto_now=True)
	size        = models.BigIntegerField(default=0)
	log         = models.TextField(null=True)

	
	  
"""
	VmBackups.status :
	0) Successful
	1) Failed
	2) Aborted
	3) Initiated  *default
	4) Create Snapshot
	5) Cloning Snapshot
	6) Removing Snapshot
	7) Exporting VM
	8) Removing Clone
	

"""
	
