import os
from bacchus import settings
from models import *

class CeleryTools:
    @staticmethod
    def restart_beat():
        return os.system('cd '+settings.SCRIPTS_DIR+';./'+settings.BEAT_RESTART_SCRIPT)
    
    @staticmethod
    def schedule_exists(name):        
        try:
            sched = Schedule.objects.get(name=name)
            return True
        except Exception as e:
            return False
        
        
