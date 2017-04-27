nohup celery -A bacchus worker -l info --concurrency=16 -b amqp://bacchus:bacchus@localhost:5672/bacchus --workdir ../ >logs/worker.log 2>&1 &

