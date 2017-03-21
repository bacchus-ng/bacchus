echo "Stopping Bacchus Web Console"
ps -ef |grep runserver|grep -v grep |awk '{print $2}'|xargs -i kill {}

