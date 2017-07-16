#!/usr/bin/env python
# Funtion:      
# Filename:

# 自定义异常，与系统定义异常不同名
class AlexException(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):      # 基类已经写了，可以不定义该函数
        return self.message
        # return 'dfjdkj'
try :
    raise AlexException('数据库连不上')
except AlexException as e:
    print(e)


# 不应该尝试下面的情况
# 自定义的异常与系统异常同名，会使得系统异常抓不到
class IndexError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):      # 基类已经写了，可以不定义该函数
        return self.message
        # return 'dfjdkj'
try :
    name = []
    print(name[3])
    raise IndexError('数据库连不上')
except IndexError as e:
    print(e)
