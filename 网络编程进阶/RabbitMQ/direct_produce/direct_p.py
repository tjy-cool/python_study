import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_log',
                         exchange_type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'hello world'
print('----', sys.argv[0])
channel.basic_publish(exchange='direct_log',
                      routing_key=severity,
                      body=message)
print(' send %r: %r' % (severity, message))
connection.close()
