import os
from bacchus import settings
from models import *
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class CeleryTools:
    @staticmethod
    def restart_beat():
        return os.system(settings.BEAT_RESTART_SCRIPT)
    
    @staticmethod
    def schedule_exists(name):        
        try:
            sched = Schedule.objects.get(name=name)
            return True
        except Exception as e:
            return False
        
    @staticmethod
    def define_inventory_sched(interval):
        inv_sched, created = IntervalSchedule.objects.get_or_create( every=interval, period=IntervalSchedule.MINUTES)
        PeriodicTask.objects.create(interval=inv_sched, name="Bacchus_Inventory_Schedule",task='manager.tasks.runInventory()')
        return True
        
        
