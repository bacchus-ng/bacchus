ps -ef |grep celery|grep bacchus|grep beat|grep -v grep |awk '{print $2}'|xargs -i kill {}
