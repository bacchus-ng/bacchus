SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
nohup celery -A bacchus worker -l info --concurrency=16 -b amqp://bacchus:bacchus@localhost:5672/bacchus --workdir ${PARENTPATH}/ >logs/worker.log 2>&1 &

