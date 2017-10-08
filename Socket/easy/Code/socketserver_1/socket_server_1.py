#!/usr/bin/env python
# Funtion:      
# Filename:

import socketserver

class MyTCPhandlser(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024)
                print("{} write: ".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('error:', e)
                break

if __name__ == "__main__":
    HOST, PORT = 'localhost', 9999
    # server = socketserver.TCPServer((HOST, PORT), MyTCPhandlser)      #单线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPhandlser)   #多线程

    # 多并发
    # class socketserver.ForkingTCPServer
    # class socketserver.ForkingUDPServer
    # class socketserver.ThreadingTCPServer
    # class socketserver.ThreadingUDPServer

    server.serve_forever()
    server.server_close()

