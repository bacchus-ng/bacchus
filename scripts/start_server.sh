SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
PARENTPATH=$(dirname $SCRIPTPATH)
echo "Starting Bacchus Web Console"
nohup python ${PARENTPATH}/manage.py runserver 0.0.0.0:8080 >logs/server.log 2>&1 &

