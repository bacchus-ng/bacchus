"""
	VMTools Class

	Author  : Niyazi Elvan
	Date    : 06.03.2017
	Updates : 16.03.2017 - 
"""
import time
import sys
from datetime import datetime, timedelta
from django.utils import timezone
from models import *
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
from django.conf.urls.static import static
from scheduler.mailer import MailTools

class VMTools:

	@staticmethod
	def list_rhevm():
		rhevmlist = Manager.objects.all()
		for rhevm in rhevmlist:
			print "id %d, name = %s" %(rhevm.id, rhevm.name)

	"""
	Connect to Manager with the given name and return connection
	"""
	@staticmethod
	def connect_to_rhevm(manager_name):
		rhevm = Manager.objects.get(name=manager_name)

		connection = sdk.Connection(url=str(rhevm.url), username=str(rhevm.username), password=str(rhevm.password), insecure=True )
		return connection

		
	
	@staticmethod
	def verify_manager_connection(manager):		
		connection = sdk.Connection(url=str(manager.url), username=str(manager.username), password=str(manager.password), insecure=True )
		return connection.test()
		
	"""
	DC discovery function, retrieve all managers from database and query all datacenter information
	"""
	@staticmethod
	def local_now():
		return timezone.localtime(timezone.now())

	@staticmethod
	def run_dc_inv():
		rhevmlist = Manager.objects.all()
		for rhevm in rhevmlist:
			connection = VMTools.connect_to_rhevm(rhevm.name)
			dcs_service = connection.system_service().data_centers_service()
			dcs = dcs_service.list()	
			for dc in dcs:
				dcc = DataCenter.objects.filter(dcid=dc.id).count()
				if (dcc > 0):
					print "%s, already discovered !" % (dc.name)
				else:
					print "%s, found new  DC !!" % (dc.name)
					print "Adding entry to database"
					now = VMTools.local_now()
					mydc = DataCenter(name=dc.name,dcid=dc.id,manager=rhevm,discovered=now,updated=now)
					mydc.save()
			connection.close()
		
		return True
	"""
	Cluster discovery function
	"""
	@staticmethod
	def run_cluster_inv():
		rhevmlist = Manager.objects.all()
		for rhevm in rhevmlist:
			connection = VMTools.connect_to_rhevm(rhevm.name)
			clusters_service = connection.system_service().clusters_service()
			cls = clusters_service.list()
			for cl in cls:
				clc = Cluster.objects.filter(clid=cl.id).count()
				if (clc > 0):
					print "%s, already discovered !" % (cl.name)
				else:
					print "%s, found new  Cluster !!" % (cl.name)
					print "Adding entry to database"
					now = VMTools.local_now()
					mydc = DataCenter.objects.get(dcid=cl.data_center.id)
					mycl = Cluster(name=cl.name,clid=cl.id,dc=mydc,discovered=now,updated=now)
					mycl.save()
			connection.close()
				
		return True

	"""
	VM discovery function, retrieve all managers from database and query all virtual machine information
	"""
	@staticmethod
	def run_host_inv():
		rhevmlist = Manager.objects.all()
		for rhevm in rhevmlist:
			connection = VMTools.connect_to_rhevm(rhevm.name)
			hosts_service = connection.system_service().hosts_service()
			hosts = hosts_service.list()
			for host in hosts:
				hostc = Host.objects.filter(hostid=host.id).count()
				if (hostc > 0):
					print "%s, already discovered !" % (host.name)
				else:
					print "%s, found new  Host !!" % (host.name)
					print "Adding entry to database"
					now = VMTools.local_now()					
					mycl = Cluster.objects.get(clid=host.cluster.id)
					myhost = Host(hostid=host.id,name=host.name,cluster=mycl,discovered=now,updated=now)					
					myhost.save()
			connection.close()
		return True
	
	@staticmethod
	def run_vm_inv():
		rhevmlist = Manager.objects.all()
		for rhevm in rhevmlist:
			connection = VMTools.connect_to_rhevm(rhevm.name)
			vms_service = connection.system_service().vms_service()
			vms = vms_service.list()
			for vm in vms:
				vmc = VM.objects.filter(vmid=vm.id).count()
				if (vmc > 0):
					print "%s, already discovered !" % (vm.name)
					myvm = VM.objects.get(vmid=vm.id)
					myvm.updated = VMTools.local_now()
					myvm.status = vm.status
					myvm.name = vm.name
					myvm.size = VMTools.get_vm_size(myvm.cluster.dc.manager.name,myvm.name)
					myvm.save()
				else:
					if (vm.name.startswith('bacchus_')):
						print "%s, found bacchus VM backup clone. Skipping. " %(vm.name)
					else:
						print "%s, found new  VM !!" % (vm.name)
						now = VMTools.local_now()
						mycl = Cluster.objects.get(clid=vm.cluster.id)
						myvm = VM(cluster=mycl,name=vm.name,vmid=vm.id,status=vm.status.value,discovered=now,updated=now)
						print "Adding entry to database"
						myvm.save()
			connection.close()
		return True
	    
	@staticmethod
	def backup_success_rate():
		
		tot_back = VmBackups.objects.all().filter(start__gte = (datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1))).count()
		suc_back = VmBackups.objects.all().filter(start__gte = (datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)), status=0).count()
		if tot_back > 0:			
			srate = int((float(suc_back)/float(tot_back))*100)
			return srate
		return 0


	@staticmethod
	def get_export_domain(manager):
		connection = VMTools.connect_to_rhevm(manager)
		sds_service = connection.system_service().storage_domains_service()
		sds = sds_service.list()
		i = 0
		while ((sds[i].type.value != 'export')&(i<len(sds))):
			i = i +1
		
		if (i<len(sds)):
			return sds[i]
		else:		
			return None
		
		"""
        Backup the VM on given manager
        """
	@staticmethod
	def get_vm_size(manager,vmname):
		size = 0
		connection = VMTools.connect_to_rhevm(manager)
		vms_service = connection.system_service().vms_service()
		vm = vms_service.list(search='name='+str(vmname))[0]
		vm_service = vms_service.vm_service(vm.id)
		disk_attachments_service = vm_service.disk_attachments_service()
		disk_attachments = disk_attachments_service.list()
		for disk_attachment in disk_attachments:
			disk = connection.follow_link(disk_attachment.disk)
			if type(disk.actual_size) is int:
				size = size + disk.actual_size
		
		connection.close()	
			
		return size
	
	@staticmethod
	def backup_vm(manager,vmname):
		connection = VMTools.connect_to_rhevm(manager)
		vms_service = connection.system_service().vms_service()
		vm = vms_service.list(search='name='+str(vmname))[0]
		snapshots_service = vms_service.vm_service(vm.id).snapshots_service()
		snapshot_name = "bacchus_"+vmname+"_"+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'))
		export_domain = VMTools.get_export_domain(manager)
		if export_domain is None:
			MailTools.notifyUsers("There is an issue with Export Domain on manager [ "+ manager + "]\nBackup aborted for " + vmname)
			exit(1)
		backup_log = "Creating a backup record at database \n"

		myvm = VM.objects.get(vmid=vm.id)
		vm_backups = VmBackups(vmid=myvm, name=snapshot_name,export=export_domain.name,start=VMTools.local_now())
		vm_backups.save()
		"""
		!!!!!! check export domain status !!!!!
		"""
		
		try:
			snap = snapshots_service.add(types.Snapshot(description=snapshot_name,persist_memorystate=False),)
			
		except Exception as e:
			
			backup_log += "Snapshot creation failed on [ "+vmname +" ]with the following error  \n"+str(e)+"\n"
			vm_backups.status = 1
			vm_backups.log = backup_log
			vm_backups.save()
			connection.close()			
			MailTools.notifyUsers(backup_log)
			exit(1)

		backup_log += "[ vmbackup" + str(vm_backups.id) + "] Snapshot creation initiated.\n"

		vm_backups.status = 4
		vm_backups.log = backup_log
		vm_backups.save()
		"""
		Add timeout value for snapshot creation, cloning and exporting. 
		If the process is stuck any of these steps, it will wait forever.
		"""
		snap_service = snapshots_service.snapshot_service(snap.id)
		
		while snap.snapshot_status != types.SnapshotStatus.OK:
			time.sleep(2)
			snap = snap_service.get()
		
		backup_log += "[ vmbackup" + str(vm_backups.id) + "] The snapshot is now complete\n"
		backup_log += "[ vmbackup" + str(vm_backups.id) + "] Cloning VM from snapshot\n"
		vm_backups.status = 5
		vm_backups.log = backup_log
		vm_backups.save()
		
		cloned_vm = vms_service.add( vm=types.Vm(name=snapshot_name, cluster=types.Cluster(id=vm.cluster.id), snapshots=[types.Snapshot(id=snap.id)] ))
		backup_log += "[ vmbackup" + str(vm_backups.id) + "] Cloning initiated\n"		
		cloned_vm_service = vms_service.vm_service(cloned_vm.id)

		while True:
			time.sleep(2)
			cloned_vm = cloned_vm_service.get()
			if cloned_vm.status == types.VmStatus.DOWN:
				break

		backup_log += "[ vmbackup" + str(vm_backups.id) + "] Clone VM completed\n"
		mysize = VMTools.get_vm_size(manager,snapshot_name)
		backup_log +=  "VM backup size is " + str(mysize)
		vm_backups.size = mysize
		vm_backups.log = backup_log
		vm_backups.save()
		
		backup_log += "[ vmbackup" + str(vm_backups.id) + "] Removing snapshot " + snapshot_name
		vm_backups.log = backup_log
		vm_backups.status = 6
		vm_backups.save()

		snap_service.remove()
			
			
		backup_log += "[ vmbackup" +str(vm_backups.id) + "] Exporting cloned VM to export domain : " + export_domain.name
		vm_backups.log = backup_log
		vm_backups.status = 7
		vm_backups.save()

		exported_vm = cloned_vm_service.export(storage_domain=types.StorageDomain(name=export_domain.name))
		
		while True:
			time.sleep(2)
			cloned_vm = cloned_vm_service.get()
			if cloned_vm.status == types.VmStatus.DOWN:
				break
		
		backup_log += "[ vmbackup" + str(vm_backups.id) +"] Export completed\n"
		backup_log += "[ vmbackup" + str(vm_backups.id) +"] Removing cloned VM " + cloned_vm.name	

		vm_backups.status = 8
		vm_backups.log = backup_log
		vm_backups.save()

		cloned_vm_service.remove()
		
		vm_backups.status = 0
		vm_backups.end = VMTools.local_now()
		vm_backups.save()
		connection.close()
		return True
	
	@staticmethod
	def manager_count():
		return Manager.objects.count()
	
	@staticmethod
	def host_count():
		return Host.objects.count()
	
	@staticmethod
	def vm_count():
		return VM.objects.count()
	
	@staticmethod
	def total_backup_size():
		vmbackups = VmBackups.objects.all()
		total_size = 0
		for vmbackup in vmbackups:
			total_size = total_size + vmbackup.size
						
		return float("{0:.2f}".format(total_size/1024.0/1024.0/1024.0/1024.0))

		

	
