python的强大之处在于有丰富的实现各种功能的标准库和第三方库，另外还允许用户自己建立库文件，下面将介绍两个常用的库（又称模块）：

- sys模块

```python
#!/usr/bin/env python
# file_name: test_sys.py

import sys          # 导入模块
print(sys.path)     # 输出模块搜索路径

print(sys.argv)     # sys.argv 实现接收外部传递的参数，包括文件名
print(sys.argv[0])  # 脚本的名称总是sys.argv列表的第一个参数，即为argv[0]                     
print(sys.argv[1])  # 其他参数依次为argv[1]
print(sys.argv[2])  # argv[2],...
print(sys.argv[3])  # argv[3],...

#终端执行
python test_sys.py I love python

>>> 
['e:\\vscode_pragram\\Python3\\Python基础\\day2\\代码', 'C:\\software\\Python\\Python35-32\\python35.zip', 'C:\\software\\Python\\Python35-32\\DLLs', 'C:\\software\\Python\\Python35-32\\lib', 'C:\\software\\Python\\Python35-32', 'C:\\software\\Python\\Python35-32\\lib\\site-packages']
['sys_test.py', 'i', 'love', 'python']
sys_test.py
i
love
python

```

- os 模块

```python
#!/usr/bin/env python
# file_name: os_test.py

import os

os.system("dir")    # 列出当前文件夹下的文件名称
                    # 该方法不能利用变量保存下来，及调用时立即打印

# 打算利用dir_req保存列出的文件名称信息，但是结果并不是那么回事，请看
dir_req = os.system("dir")
print("--->", dir_req)

>>> 
 驱动器 E 中的卷没有标签。
 卷的序列号是 000D-4517

 e:\vscode_pragram\Python3\Python基础\day2\代码 的目录

2017/04/15  09:51    <DIR>          .
2017/04/15  09:51    <DIR>          ..
2017/04/15  09:58               184 os_test.py
2017/04/15  09:44               180 sys_test.py
               2 个文件            364 字节
               2 个目录 60,183,629,824 可用字节
---> 0

```


最后输出了 --->0 ,说明dir_req为0，也就是说当os.system("dir")运行成功返回0，不成功返回错误代码

如果需要保存信息，将利用 popen 方法，如下
```python
#!/usr/bin/env python
# file_name: os_test2.py
dir_req = os.popen("dir")   # dir_req 返回一个文件描述符号为fd的打开的文件对象
print(dir_req)              # 将该文件描述符打印到屏幕
print("\n")                 
print(dir_req.read())       # 利用read方法读取该文件描述符的内容


>>>
<os._wrap_close object at 0x01B1B7B0>


 驱动器 E 中的卷没有标签。
 卷的序列号是 000D-4517

 e:\vscode_pragram\mine\Python3\Python基础\day2\代码 的目录

2017/04/15  09:51    <DIR>          .
2017/04/15  09:51    <DIR>          ..
2017/04/15  10:03               269 os_test.py
2017/04/15  09:44               180 sys_test.py
               2 个文件            449 字节
               2 个目录 60,183,629,824 可用字节

```