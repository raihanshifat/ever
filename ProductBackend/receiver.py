import pika, os, signal, sys

def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

connection = pika.BlockingConnection(pika.URLParameters('amqps://agedtxxh:pet45m8MD5j8iYRKGBtGuV13jdCdUnvO@puffin.rmq2.cloudamqp.com/agedtxxh'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
connection.close()