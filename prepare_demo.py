import datetime
from manager.models import *

ovirt1 = Manager(name='ovirt1',fqdn='ovirt1.bacchus.co',url='https://ovirt1.bacchus.co/ovirt-engine/api',username='admin@internal',password='12345678',version='4.0',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
ovirt1.save()

rhevm = Manager(name='rhevm1',fqdn='rhevm1.bacchus.co',url='https://rhevm1.bacchus.co/ovirt-engine/api',username='admin@internal',password='12345678',version='4.0',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
rhevm.save()


dc1 = DataCenter(dcid='sdaa-asdas-as23-sds342',name='MyDC1',manager=ovirt1,discovered=datetime.datetime.now(),updated=datetime.datetime.now())
dc1.save()

dc2 = DataCenter(dcid='sdaa-asdas-as23-sds342',name='MyDC2',manager=rhevm,discovered=datetime.datetime.now(),updated=datetime.datetime.now())
dc2.save()

cl1 = Cluster(clid='adsa-342a-as34a-asda3',name='cls-prod1',dc=dc1,discovered=datetime.datetime.now(),updated=datetime.datetime.now())
cl1.save()

cl2 = Cluster(clid='adsa-342a-asd5a-asda3',name='cls-prod2',dc=dc2,discovered=datetime.datetime.now(),updated=datetime.datetime.now())
cl2.save()

vm1 = VM(cluster=cl1,name='vm1',vmid='2342-234sdf23-2342sd-2718fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm1.save()

vm2 = VM(cluster=cl1,name='vm2',vmid='2342-234sdf23-2342sd-2728fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm2.save()

vm3 = VM(cluster=cl1,name='vm3',vmid='2342-234sdf23-2342sd-2783fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm3.save()

vm4 = VM(cluster=cl1,name='vm4',vmid='2342-234sdf23-2342sd-278f4gh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm4.save()

vm5 = VM(cluster=cl2,name='vm5',vmid='2342-234sdf23-2342sd-278fg5h',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm5.save()

vm6 = VM(cluster=cl2,name='vm6',vmid='2342-234sdf23-2342sd-278fg7h',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm6.save()

vm7 = VM(cluster=cl2,name='vm7',vmid='2342-234sdf23-2342sd-278fgh8',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm7.save()

vm8 = VM(cluster=cl2,name='vm8',vmid='2342-234sdf23-2342sd-278fg9h',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm8.save()


vm11 = VM(cluster=cl1,name='vm11',vmid='23142-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm11.save()

vm12 = VM(cluster=cl1,name='vm12',vmid='23422-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm12.save()

vm13 = VM(cluster=cl1,name='vm13',vmid='2342-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm13.save()

vm14 = VM(cluster=cl1,name='vm14',vmid='23e42-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm14.save()

vm15 = VM(cluster=cl2,name='vm15',vmid='23425-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm15.save()

vm16 = VM(cluster=cl2,name='vm16',vmid='23642-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm16.save()

vm17 = VM(cluster=cl2,name='vm17',vmid='23472-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm17.save()

vm18 = VM(cluster=cl1,name='vm18',vmid='23842-234sdf23-2342sd-278fgh',status='up',discovered=datetime.datetime.now(),updated=datetime.datetime.now())
vm18.save()


mybackup = VmBackups(vmid=vm1,name='bacchus_vm1_XXX',export='ExportDomain',status=0,start=datetime.datetime.now(),end=datetime.datetime.now(),updated=datetime.datetime.now(),size=2334234242342)

mybackup.save()


mybackup = VmBackups(vmid=vm18,name='bacchus_vm18_XXX',export='ExportDomain',status=0,start=datetime.datetime.now(),end=datetime.datetime.now(),updated=datetime.datetime.now(),size=1334234242342)

mybackup.save()














