echo "Starting worker"
sh worker.sh
sleep 2
echo "Starting Beat"
sh beat.sh
sleep 2
echo "Starting Flower"
sh flower.sh


