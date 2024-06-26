FROM rabbitmq:3-management

# Enable the RabbitMQ management plugin
RUN rabbitmq-plugins enable rabbitmq_management
ENV  RABBITMQ_DEFAULT_USER=user
ENV  RABBITMQ_DEFAULT_PASS=password
# Set up a new user and password for RabbitMQ
#RUN rabbitmqctl add_user rabituser rabituser1234
#RUN rabbitmqctl set_user_tags rabituser administrator
#RUN rabbitmqctl set_permissions -p / rabituser ".*" ".*" ".*"
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY receive.py ./

#CMD [ "python", "receive.py" ]