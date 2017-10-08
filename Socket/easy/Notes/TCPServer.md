步骤：
1. 自己创建一个请求类，并且这个类要继承BaseRequestHandler,并且还要重写handler()函数

2. 实例化TCPServer，传递server ip 和创建的请求处理类，给这个TCPServer

3. server.handler_request()     # 只处理一个请求
   server.request_forever()     # 处理多个请求，永远执行

4. 调用server_close() 关闭socket.