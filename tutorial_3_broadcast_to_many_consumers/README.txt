docker run -d --name rabbitmq --restart=always -p 5671:5671 -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:management
setup.bat

# 2 workers, 3 messages
start python receive_logs.py
start python receive_logs.py
python send.py one
python send.py two
python send.py three
