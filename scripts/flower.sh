SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
HOMEPATH=$(dirname $PARENTPATH)
nohup celery -A bacchus flower --broker=amqp://bacchus:bacchus@localhost:5672/bacchus --basic_auth=admin:Passw0rd --workdir ${PARENTPATH}/ >${HOMEPATH}/logs/flower.log 2>&1 &
