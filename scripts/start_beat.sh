SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
HOMEPATH=$(dirname $PARENTPATH)
nohup celery -A bacchus beat -l info -S django --workdir $PARENTPATH >${HOMEPATH}/logs/beat.log 2>&1 &
