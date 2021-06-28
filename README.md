# learning-rabbitmq
* A personal repo to learn RabbitMQ.

# run a docker with rabbitmq
* docker run -d --name rabbitmq --restart=always -p 5671:5671 -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:management

# set up venv and install requirements
* setup.bat