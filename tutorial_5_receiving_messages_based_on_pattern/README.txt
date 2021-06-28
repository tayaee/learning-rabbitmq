docker-rabbitmq.bat
setup.bat

start python receive_logs_topic.py "#"
start python receive_logs_topic.py "kern.*"
start python receive_logs_topic.py "*.critical"
start python receive_logs_topic.py "kern.*" "*.critical"

python emit_log_topic.py "kern.critical" "A critical kernel error"
python emit_log_topic.py "kern.critical" "A critical kernel error"
