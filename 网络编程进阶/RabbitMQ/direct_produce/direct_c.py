import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_log',
                         exchange_type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
severities = sys.argv[1:]
print(severities)
if not severities:
    sys.stderr.write('Usage: %s [info] [warning] [error]\n' % sys.argv[0])
    sys.exit(1)
for severity in severities:
    channel.queue_bind(exchange='direct_log',
                       queue=queue_name,
                       routing_key=severity)


def callback(ch, method, property, body):
    print(' [x] %r: %r' % (method.routing_key, body))


channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
