import pika

# Specify the host address and port of the RabbitMQ server running on the remote host
host = 'localhost'
port = 5672  # Default port for RabbitMQ

# Specify the credentials for authentication
# credentials = pika.PlainCredentials('user', 'password')

# Establish a connection to the RabbitMQ server with the specified credentials
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

# Publish a message to the queue
message = 'we send this from local pc to rabbitmq that run in docker 4!!! '
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent {message}")

# Close the connection
connection.close()
