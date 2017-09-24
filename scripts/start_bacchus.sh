SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
if [ ! -d logs ]; then
mkdir logs
fi 
${SCRIPTPATH}/start_celery.sh
${SCRIPTPATH}/start_server.sh

