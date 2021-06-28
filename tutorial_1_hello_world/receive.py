# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
import sys

import pika


def main():
    # connection
    parameters = pika.ConnectionParameters(host='192.168.99.101', port=32774)
    connection = pika.BlockingConnection(parameters)

    # channel
    channel = connection.channel()

    # queue
    channel.queue_declare(queue='hello')

    # subscribe
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
