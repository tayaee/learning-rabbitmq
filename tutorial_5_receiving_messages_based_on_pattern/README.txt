docker run -d --name rabbitmq --restart=always -p 5671:5671 -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:management
setup.bat

start python receive_logs_topic.py "#"
start python receive_logs_topic.py "kern.*"
start python receive_logs_topic.py "*.critical"
start python receive_logs_topic.py "kern.*" "*.critical"

python emit_log_topic.py "kern.critical" "A critical kernel error"
python emit_log_topic.py "kern.critical" "A critical kernel error"
