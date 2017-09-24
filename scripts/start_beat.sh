SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
nohup celery -A bacchus beat -l info -S django --workdir $PARENTPATH >logs/beat.log 2>&1 &
