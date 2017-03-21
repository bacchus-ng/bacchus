echo "Restarting Bacchus services."


./stop_server.sh
./stop_celery.sh

sleep 3

./start_celery.sh
./start_server.sh
