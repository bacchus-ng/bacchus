SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
echo "Restarting Bacchus services."

${SCRIPTPATH}/stop_server.sh
${SCRIPTPATH}/stop_celery.sh

sleep 3

${SCRIPTPATH}/start_celery.sh
${SCRIPTPATH}/start_server.sh
