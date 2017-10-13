#!/usr/bin/env python
# Funtion:      
# Filename:

import urllib
from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()  # 把当前程序的所有的io操作帮我单独做上标记

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    # with open('aa.html', 'wb', encoding='utf-8') as f:
    #     f.write(data)
    print('%d bytes received from %s.' % (len(data), url))

# 普通爬虫
# f('http://www.cnblogs.com/tjuyuan/p/6796349.html')
# f('https://www.crifan.com/python_urllib2_urlerror_urlopen_error_errno_10060/')


urls = [
'http://www.python.org',
'https://www.taobao.com/',
'http://www.baidu.com'
]

start_time = time.time()
for i in urls:
    f(i)
print('同步cost：%s' %(time.time()- start_time))

async_start_time = time.time()

gevent.joinall([
    gevent.spawn(f, 'http://www.python.org'),
    gevent.spawn(f, 'https://www.taobao.com/'),
    gevent.spawn(f, 'http://www.baidu.com')
])
print('异步cost：%s' %(time.time()- async_start_time))