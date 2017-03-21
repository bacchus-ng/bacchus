echo "Stopping Celery services"
ps -ef |grep celery|grep -v grep |awk '{print $2}'|xargs -i kill {}

