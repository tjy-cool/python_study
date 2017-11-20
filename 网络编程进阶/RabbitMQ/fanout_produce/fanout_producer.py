import pika

#创建socket连接
connection = pika.BlockingConnection(pika.ConnectionParameters
                                     (host='localhost'))
#创建管道
channel = connection.channel()

#声明exchange，且exchange的名字是logs，exchange的类型为fanout
channel.exchange_declare(exchange='logs', exchange_type="fanout")

#发送的消息
message = "info:hello world"

#生产一个消息
channel.basic_publish(
    exchange="logs",
    routing_key='',
    body=message
)
print("[X] Send {0}".format(message))

#关闭连接
connection.close()
