nohup celery -A bacchus beat -l info -S django --workdir ../ >logs/beat.log 2>&1 &
