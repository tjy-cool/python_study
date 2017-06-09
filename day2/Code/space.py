# str1 = "   xyz   "
# str1.strip()        # "xyz"
# str1.lstrip()       # "xyz   "
# str1.rstrip()       # "   xyz"

# str2 = "   x y z   "
# print(str2.replace(" ",""))    # 

# print("x\ny\nz\n".replace("\n",''))
# str3 = "   x,y,z   "
# print(str3.strip().split(","))

# str3 = "x\ny\nz"
# str3.split("\n")        # ['x', 'y', 'z']


str4 = "x,y\nz,w"       # 需要将该字符串变为2维列表
aa = str4.split("\n")   # 先以换行符为分割符
str4_list = []          # 空列表保存最终结果
for i in aa:            # 依次取出aa中的内容，即['x,y']和['z,w']
    _str = i.split(",") # 以逗号为分隔符，分别为['x', 'y']和['z', 'w']
    str4_list.append(_str)     # 追加方法生成二维列表,  [['x', 'y'], ['z', 'w']]
str4_dict = dict(str4_list)    # 二维列表转换为字典，   {'z': 'w', 'x': 'y'}


print(str4_list)
print(str4_dict)
