SCRIPTPATH=$(cd $(dirname $0) ; pwd -P)
${SCRIPTPATH}/stop_beat.sh
sleep 1
${SCRIPTPATH}/start_beat.sh

