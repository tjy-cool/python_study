import pika
#创建一个socket
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost"))
#创建一个管道
channel = connection.channel()
#声明exchange,exchange的名字logs，类型是fanout广播模式
channel.exchange_declare(exchange="logs",
                         exchange_type="fanout")
#不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除，result是queue的对象
result = channel.queue_declare(exclusive=True)  # exclusive=>排他的，唯一的
#获取queue名
queue_name = result.method.queue
#绑定exchange
channel.queue_bind(exchange="logs",
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')
#声明回调函数


def callback(ch, method, properties, body):
    "回调函数"
    print("[X] {0}".format(body))


#消费者消费
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
#启动消费模式
channel.start_consuming()
