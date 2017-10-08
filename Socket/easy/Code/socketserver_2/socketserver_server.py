#!/usr/bin/env python
# Funtion:      
# Filename:

import socketserver

class MyTCPHandlers(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try :
                self.data = self.request.recv(1024)
                print("{} write: ".format(self.client_address))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('error:', e)
                break


if __name__ == '__main__':
    HOST, PORT = 'localhost', 8888
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandlers)
    server.serve_forever()
    server.server_close()