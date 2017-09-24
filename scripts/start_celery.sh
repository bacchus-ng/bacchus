SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
echo "Starting Celery worker"
sh ${SCRIPTPATH}/worker.sh
sleep 2
echo "Starting Celery Beat"
sh ${SCRIPTPATH}/start_beat.sh
sleep 2
echo "Starting Celery Flower"
sh ${SCRIPTPATH}/flower.sh

