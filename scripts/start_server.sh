echo "Starting Bacchus Web Console"
nohup python ../manage.py runserver 0.0.0.0:8080 >logs/server.log 2>&1 &

