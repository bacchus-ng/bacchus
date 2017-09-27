SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
HOMEPATH=$(dirname $PARENTPATH)
echo "Starting Bacchus Web Console"
nohup python ${PARENTPATH}/manage.py runserver 0.0.0.0:8080 >${HOMEPATH}/logs/server.log 2>&1 &

