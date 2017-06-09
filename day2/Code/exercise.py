#!/usr/bin/env python
# Author:tjy
import copy
# names = ['Tom', 'Jick', 'Alex', 'TJY']
# names.sort(key=len,reverse=False)
# names.reverse()

# if 'TJY' in names and 'tjy' not in names:
#     names.remove('TJY')
#     names.append('tjy')

# names.pop(1)
# names.extend(['aa.xml', 'bb', 12])
# names.insert(2, 'aa.xml')
# print(names.index('Jick'))
# names.append('kitty')
# names1 = names.copy()
# names1[-2][0] = 'jick'
# names1[0] = 'tom'
# print(names1)

# names2 = copy.copy(names)
# names2[-1][0] = 'jack'
# print(names2)
# names3 = copy.deepcopy(names)
# names3[-1][1] = 'cc'
# print(names3)
# num = names.count('tom')
# print(num)
# print(names)

str1 = 'i love python'
# print(str1.count('1'))
# print(str1.center(50,'='))
# print(str1.count('i'))
# print(str1.encode())
# print(str1.expandtabs(50))
# print(str1.endswith('on'))
# print(str1.startswith('i '))
# print(str1.find('w'))      #没有找到返回-1，找了了返回索引值
# print(str1.index('l'))
# print('   '.isspace())
# print('00'.isnumeric())       # 是否为纯数字
# print('a1b2'.isalnum())
# print('1E23'.isdecimal())
# print('00'.isdigit())     # 是否为整数，包含0
# print('a12'.isidentifier()) # 是否为合法的标识符，即是否为合法的变量名
# print('a \t\ns'.islower())        # 是否为大写字母，自动忽略空格,制表符，换行符
# print('\t\nSA \t'.isupper())        # 同上
# print('df'.isprintable())           # 主要用于设备文件和驱动文件
# print('I Am A Goodmen'.istitle())
# print('|'.join(['12','23','34']))     # 列表中必须是字符串
# print('\n'.join(('a', 'b')))          # 也可以是tuple
# print('\n'.join('hello'))             # 字符串
# print('\n'.join({'name':"tjy", 'age':18}))  #字典只取key值
#
# b = 'a'.rjust(50,'=')
# print(b)
# print(len(b))
# print(str)

# print('djsk  fsd\r\nfdfd'.split('\n'))
# print('djsk  fsd\r\nfdfd'.splitlines())    # \r\n 和 \n 都可以作为分隔符
# print('djsk  fsd\nfdfd'.splitlines())
# b = '\nfjdk\t\n\r'.strip()
# print(b)
# print(len(b))

# print('faS dfs1'.swapcase())     # 大小写交互，数字不变
# print('i am a boy'.title())      # 变为标题

# b = str.maketrans('abcd1234','hijklmn0')
# print('aa123fd'.translate(b))

# print('i am a boy'.partition('a'))
# print('is is '.replace('is','are'))
# print('is a good boy,is'.rindex('is'))

