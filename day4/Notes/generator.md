# 列表生成式
```python
# 一个列表[0,1,...,9]，要求把列表里的每个数加1，实现方式：
# 最low方式
a = [0,1,2,3,4,5,6,7,8,9]
b = []
for i in a:
    b.append(i+1)
a = b

# 一般方式
a = [0,1,2,3,4,5,6,7,8,9]
for index, value in enumerate(a)
    a[index] += value

# 高级方式
a =  [0,1,2,3,4,5,6,7,8,9]
a = map(lamada x:x+1, a)    # 匿名函数

# 顶级方式
a = [i+1 for i in range(10)]    # 列表生成式
```

# 生成器
通过列表生成式创建的列表是具体的列表，需要占用内存的列表，如果需要创建一个大容量的列表（如1千万数据量），但是我们只需要访问前面的若干元素，这使得后面存储的元素白白占据了内存。

所以，如果列表的元素有一定的规则进行推算，我们只需要存储该规则，而不必创建
完整的列表(list)，从而节省大量的空间。

在python中，这种一边循环，一边计算的机制，成为生成器：generator。

```python
L = [ x**2 for x in range(10) ]     # 列表用中括号 []
g = ( x**2 for x in range(10) )     # 生成器用小括号 ()
```
生成器调用每个元素的方法有两种，__next__()属性   和   next(g)内置函数
```python
# __next__()属性
print( g.__next__() )   # 0
print( next(g) )        # 1
print( next(g) )        # 4
print( next(g) )        # 9
print( next(g) )        # 16
print( next(g) )        # 25
print( next(g) )        # 36
print( next(g) )        # 49
print( next(g) )        # 64
print( next(g) )        # 81
print( next(g) )        # 出现 Stopiteration 错误
```
generator是可迭代对象，正确的使用方法是用for循环取值。所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
```python
g = ( x**2 for x in range(10) )
for n in g:
    print(n)
```

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
```python
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        yield  b
        a,b = b,a+b
        n += 1
    return 'done'

f = fib(10)
print(f)    # <generator object fib at 0x013D9B10>
```
这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。

> generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

换句话说 yeild相当于另一个return语句。

```python


```