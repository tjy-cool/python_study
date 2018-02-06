import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters
                                     ("localhost"))
channel = connection.channel()
#定义direct类型的exchange
channel.exchange_declare(exchange="direct_logs",
                         exchange_type="direct")
#定义重要程度，定义什么级别的日志
severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = ' '.join(sys.argv[2:]) or "hello world"
#发送消息
channel.basic_publish(exchange="direct_logs",
                      routing_key=severity,
                      body=message
                      )
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
