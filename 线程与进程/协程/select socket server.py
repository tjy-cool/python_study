#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
import select
import queue
import sys

server = socket.socket()

server.bind(('localhost', 9999))
server.listen(1000)

server.setblocking(False)       # 不阻塞
msg_dict = {}
inputs = [server,]
outputs = []
while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    # 当你把inputs, outputs, exceptional(这里跟inputs共用)传给select()后，
    # 它返回3个新的list，我们上面将他们分别赋值为readable, writable, exceptional,
    # 所有在readable list中的socket连接代表有数据可接收(recv),
    # 所有在writable list中的存放着你可以对其进行发送(send)操作的socket连接，
    # 当连接通信出现error时会把error写到exceptional列表中。
    print(readable, writeable, exceptional)
    for r in readable:
        if r is server:     # 代表来了一个新链接
            conn, addr = server.accept()
            # print('conn: ', conn)
            print('来了个新链接: ', addr)
            # conn.setblocking(False)
            inputs.append(conn)     #是因为这个建立的新连接还没有发数据过来，现在就要接收数据
            # 所以要有实现这个客户端发数据来时server端能知道，就要让server再监听一次
            msg_dict[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据
        else:
            data = r.recv(1024)
            print('收到数据: ', data)
            if data:        # 接收到数据
                print( 'received "%s" from %s' % (data, r.getpeername()))
                # print(sys.stderr, 'received "%s" from %s' % (data, r.getpeername()))
                msg_dict[r].put(data)
                if r not in outputs:
                    outputs.append(r)
            else:
                # print('closing', r, 'after reading no data')
                if r in outputs:#既然客户端都断开了，我就不用再给它返回数据了，
                    # 所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                    outputs.remove(r)
                inputs.remove(r)    #inputs中也删除掉
                r.close()    #把这个连接关闭掉
                del msg_dict[r]

            # r.send(data)  # 可以立刻返回，也可以按照下面的返回
              # 将需要发送的数据传入到队列中

    for w in writeable:         # 要返回给客户端的链接列表
        data_to_client = msg_dict[w].get()  # 从队列中取出需要发送的数据
        w.send(data_to_client)          # 发送数据到客户端
        outputs.remove(w)       # 确保下次循环的时候writeable，不返回这个已经出来完的链接

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dict[e]
        e.close()


