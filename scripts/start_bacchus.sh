if [ ! -d logs ]; then
mkdir logs
fi 
./start_celery.sh
./start_server.sh

