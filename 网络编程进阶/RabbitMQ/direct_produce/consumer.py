import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters
                                     ("localhost"))
channel = connection.channel()
#定义direct类型的exchange
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
#手动输入安全级别
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
#循环遍历绑定消息队列
for severity in severities:
    channel.queue_bind(exchange="direct_logs",
                       queue=queue_name,
                       routing_key=severity)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properites, body):
    "回调函数"
    print(" [x] %r:%r" % (method.routing_key, body))


#消费消息
channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
