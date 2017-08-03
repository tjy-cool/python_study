#!/usr/bin/env python
# Funtion:      
# Filename:

name = ['23', '34']
try :
    name(1)
    open('aa.txt')
    # print('11')   # 针对else进行测试
except IndexError as e: # 尝试列表索引错误
    print('list出错, ',e)
except KeyError as e:   # 尝试字典key错误
    print('字典出错, ', e)
except Exception as e:  # 如果以上尝试都没检测到错误，又不想继续尝试，则抛出未知错误
    print('未知错误，',e)

else:   # 如果
    print("一切正常")
finally:
    print("不管有没有错误，都执行")


n = 1
if n==1:
    n2 = 1
print(n2)