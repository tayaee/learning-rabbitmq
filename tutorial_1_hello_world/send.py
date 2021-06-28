# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
import pika

# connection
parameters = pika.ConnectionParameters(host='192.168.99.101', port=32774)
connection = pika.BlockingConnection(parameters)

# channel
channel = connection.channel()

# queue
channel.queue_declare(queue='hello')

# send message
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# close connection
connection.close()
