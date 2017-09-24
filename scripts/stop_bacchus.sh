SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
${SCRIPTPATH}/stop_server.sh
${SCRIPTPATH}/stop_celery.sh


