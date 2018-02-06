__author__ = "zhangqigao"

import pika
import uuid
import time


class FibonacciRpcClient(object):
    "斐波那契数列rpc客户端"

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters
                                                  (host="localhost"))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        print("---->", method, props)
        if self.corr_id == props.correlation_id:  # 我发过去的结果就是我想要的结果，保持数据的一致性
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.publish(exchange="",
                             routing_key="rpc_queue",
                             properties=pika.BasicProperties(
                                 reply_to=self.callback_queue,
                                 correlation_id=self.corr_id),
                             body=str(n))
        while self.response is None:
            self.connection.process_data_events()  # 非阻塞版的start_consumer()
            print("no msg....")
            time.sleep(0.5)
        return int(self.response)


if __name__ == "__main__":
    fibonacci_rpc = FibonacciRpcClient()
    # print(" [x] Requesting fib(30)")
    num = input('请输入：').strip()
    print(" [x] Requesting fib(%s)" % int(num))
    response = fibonacci_rpc.call(int(num))
    print(" [.] Got %r" % response)
