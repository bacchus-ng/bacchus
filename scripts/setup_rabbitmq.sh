# this script adds bacchus user to rabbitmq-server
# run with root permission
rabbitmqctl add_user bacchus bacchus
rabbitmqctl add_vhost bacchus
rabbitmqctl set_user_tags bacchus Administrator
rabbitmqctl set_permissions -p bacchus bacchus ".*" ".*" ".*"

