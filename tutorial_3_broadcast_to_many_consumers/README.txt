docker-rabbitmq.bat
setup.bat

# 2 workers, 3 messages
start python receive_logs.py
start python receive_logs.py
python send.py one
python send.py two
python send.py three
