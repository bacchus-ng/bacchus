SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
HOMEPATH=$(dirname $PARENTPATH)
nohup celery -A bacchus worker -l info --concurrency=16 -b amqp://bacchus:bacchus@localhost:5672/bacchus --workdir ${PARENTPATH}/ >${HOMEPATH}/logs/worker.log 2>&1 &

