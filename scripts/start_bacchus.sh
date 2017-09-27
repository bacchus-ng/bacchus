SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
HOMEPATH=$(dirname $PARENTPATH)
if [ ! -d ${HOMEPATH}/logs ]; then
mkdir ${HOMEPATH}/logs
fi 
${SCRIPTPATH}/start_celery.sh
${SCRIPTPATH}/start_server.sh

