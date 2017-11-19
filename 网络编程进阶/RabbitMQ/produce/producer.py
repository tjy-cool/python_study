import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()  # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!'
                          )
    print("[X] send 'Hello World'")
    connection.close()
