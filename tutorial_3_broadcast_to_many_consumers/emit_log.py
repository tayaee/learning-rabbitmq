# https://www.rabbitmq.com/tutorials/tutorial-three-python.html
import pika
import sys

parameters = pika.ConnectionParameters(host='192.168.99.101', port=32774)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
