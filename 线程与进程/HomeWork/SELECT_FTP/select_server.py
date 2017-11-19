#!/usr/bin/env python
# Funtion:      
# Filename:

import select, socket, queue

class Slectors_server(object):
    def __init__(self, HOST):
        self.server = socket.socket()
        self.server.bind(HOST)
        self.server.listen(1000)
        self.server.setblocking(False)

    def push(self, Recv_dict):
        pass

    def pull(self, Recv_dict):
        pass
