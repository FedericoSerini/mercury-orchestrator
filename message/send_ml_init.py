import pika


def send():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='ml-command-init')

    channel.basic_publish(exchange='', routing_key='ml-command-init', body='')
    print(" [x] Sent 'Hello World!'")
    connection.close()
