import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_log', exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'hello world'
channel.basic_publish(exchange='topic_log',
                      routing_key=routing_key,
                      body=message)
print(' [x] sent %r: %r' % (routing_key, message))
connection.close()
