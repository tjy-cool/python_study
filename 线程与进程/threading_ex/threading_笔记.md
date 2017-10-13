## threading 多线程
通过使用线程，程序可以在用一个进程空间并发地运行多个操作，threading模块建立在thread的底层特性基础之上，可以更容易地完成线程处理。
### 1.所有方法
    为了更加全面深入的了解多线程的知识，我们根据threading.py文件中提供的__all__的所有属性和功能来讲解。
```python
    __all__ = ['get_ident', 'active_count', 'Condition', 'current_thread',
           'enumerate', 'main_thread', 'TIMEOUT_MAX',
           'Event', 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
           'Barrier', 'BrokenBarrierError', 'Timer', 'ThreadError',
           'setprofile', 'settrace', 'local', 'stack_size']

# 类   
threading.Condition()
threading.Semaphore()
threading.BoundedSemaphore()
threading.Event()
threading.Barrier()
threading.BorkenbarrieError()
threading.Thread()
threading.Timer()
threading.Lock()
threading.RLock()

函数  setprofile()
      settrace()
      current_thread()
      active_count()
      enumerate()
      main_thread()
      get_ident()

属性  TIMEOUT_MAX = 4294967.0
```

## 2.创建线程 threading.Thread()
创建线程最简单的是创建Thread对象，Thread对象拥有多种方法和属性，假设t为Thread对象。
```python
t.start()     # 启动线程
t.join()      # 等待线程结束
```


```python
def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
```
    一般只需要设置target和args， target为执行函数名，args是执行函数的参数。
    在源码里面发现下面几个好玩的东西：
    1. 
     
    name


```python
import threading
import time
def func1(num):
    print('Hello World!------',num)
    time.sleep(5)
    
def func2(name, age):
    print('My name is %s, and my age is %s' %(name, age))

print('five thread goning to run! and wait 5 minuts will stop')
th_list = []
for i in range(5):
    th1 = threading.Thread(target=func1, args=(i,))
    th1.start()
    th_list.append(th1)

for t in th_list:
    t.join()

print('It is my turn, I will tell my name and age')
th2 = threading.Thread(target=func2, args=('Tom',20))
th2.start()
```

