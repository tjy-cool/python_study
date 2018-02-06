import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()  # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello', durable=True)     # 队列持久化

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!'
                      # make message persistent=>使消息持久化
                      #   properties=pika.BasicProperties(delivery_mode=2,)
                      )
print("[X] send 'Hello World'")
connection.close()
