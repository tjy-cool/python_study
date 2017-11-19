#!/usr/bin/env python
# Funtion:      
# Filename:

import socket, sys

messages = [b'This is the message. ',
            b'It will be sent ',
            b'in parts.',
            ]
server_address = ('localhost', 9999)

# Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(50)]

# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message))
        s.send(message)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print('%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname())
            s.close()