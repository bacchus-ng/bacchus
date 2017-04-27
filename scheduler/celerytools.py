import os
from bacchus import settings


class CeleryTools:
    @staticmethod
    def restart_beat():
        return os.system('cd '+settings.SCRIPTS_DIR+';./'+settings.BEAT_RESTART_SCRIPT)
