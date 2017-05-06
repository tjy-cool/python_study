# 文件操作
# 文件基本操作
```python
f = open(filename, 'r', encording='utf-8')
first_line = f.readline()
rest_data = f.read()  # 读取剩下的所有内容,文件大时不要用
f.write('lastline')
f.close             # 关闭文件

# 其他方法
f.readlines()   # 返回一个列表，列表的元素为每行的字符，包括换行符
f.tell()        # 返回当前光标所在的字符个数（从最前面开始）
f.seek(0)       # “光标” 跳转到文件开头
f.truncate()    # 截断操作
f.fileno()      # 文件标识符
f.read()        # 注意，不一定能全读回来
f.write(str)    # 写入字符串
f.readinto()    # 不要用
f.readall()     

f.readable()    # 是否可读
f.seekable()    # 光标是否可跳转
f.writeable()   # 是否可写

# with 语句，为了避免打开文件后忘记关闭，可以通过管理上下文
with open(filename1, 'r', encoding='utf-8') as f1,
        open(filename2, 'w', encoding='utf-8') as f2,
        pass
...

# 循环文件，低效率，内存需要保留所有数据
for index, line in enumerate(f.readlines()):
    print(index,line)

# 循环文件，高效率, 内存只保留一行数据
for line in f
    print(line)
```
打开文件的模式有：
- r，只读模式（默认）。
- w，只写模式。【不可读；不存在则创建；存在则删除内容；】
- a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件

- r+，可读写文件。【可读；可写；可追加】
- w+，写读
- a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

- rU
- r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

- rb
- wb
- ab