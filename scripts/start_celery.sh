echo "Starting Celery worker"
sh worker.sh
sleep 2
echo "Starting Celery Beat"
sh beat.sh
sleep 2
echo "Starting Celery Flower"
sh flower.sh


