docker run -d --name rabbitmq --restart=always -p 5671:5671 -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:management
setup.bat

# 3 workers, 3 messages
start python receive_log_direct.py error
start python receive_log_direct.py error warning
start python receive_log_direct.py error warning info
python send.py error "Error message 1"
python send.py warning "Warning message 1"
python send.py info "Info message 1"
