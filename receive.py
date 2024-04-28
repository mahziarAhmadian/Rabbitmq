#!/usr/bin/env python
import pika, sys, os


def main():
    host = 'server_ip'
    port = 5672  # Default port for RabbitMQ

    # Specify the credentials for authentication
    credentials = pika.PlainCredentials('rabituser', 'rabituser1234')

    # Establish a connection to the RabbitMQ server with the specified credentials
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
