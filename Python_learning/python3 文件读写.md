# python3 文件读写
## open函数
```python
f = open('filename','r') # 读模式
f = open('filename','w') # 写模式
f = open('filename','a') # 追加模式
 
注：rb 是以二进制读取
现在你觉得没用对吧，我也这么觉得。。。
but
在以后用到socket的时候，传输文件，读取和写入用的都是二进制形式
rb和wb可以更快速的进行文件的传输
```

