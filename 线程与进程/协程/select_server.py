#!/usr/bin/env python
# Funtion:      
# Filename:

import select, socket, queue

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1000)
server.setblocking(False)

msg_dict = {}
inputs = [server,]
outputs = []

while True:
    readable, writeable, exectional = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is server:
            conn, addr = server.accept()
            print('来了个新链接: ', addr)
            inputs.append(conn)
            msg_dict[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            msg_dict[r].put(data)
            # r.send(data)

    for w in writeable:
        w.send(msg_dict[w].get())
        outputs.remove(w)

    for e in exectional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dict[e]