import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)  # 队列持久化


def callback(ch, method, properites, body):
    print("--->", ch, method, properites)
    print("[x] received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动确定


channel.basic_consume(callback,
                      queue='hello',
                      # no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
