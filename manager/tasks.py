from __future__ import absolute_import 
from celery import shared_task
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
from django.utils import timezone
from datetime import datetime
from manager.vmtools import *
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def runVmInventory():
	logger.info("Running VM inventory" )
	return VMTools.run_vm_inv()

@shared_task
def backup_vm(rhevmname,vmname):
	return VMTools.backup_vm(rhevmname,vmname)

