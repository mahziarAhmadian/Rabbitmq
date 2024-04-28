import pika

# Specify the host address and port of the RabbitMQ server running on the remote host
host = 'server_ip'
port = 5672  # Default port for RabbitMQ

# Specify the credentials for authentication
credentials = pika.PlainCredentials('rabituser', 'rabituser1234')

# Establish a connection to the RabbitMQ server with the specified credentials
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

# Publish a message to the queue
channel.basic_publish(exchange='', routing_key='hello', body='message from clinet')
print(" [x] Sent 'Hello, World!'")

# Close the connection
connection.close()
