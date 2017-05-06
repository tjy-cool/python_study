# dict方法
```python
#%%
dict[key] = value       # 增加
dict[key] = new_value   # 修改

# 删除
dict.pop[key]
del dict[key]
dict.popitem[key]  # 随机删除

# 查找
key in dict        # 返回True/False
dict.get[key]      # 没有找到返回 None ,否则返回value
dict[key]          # 不存在会报错，存在返回value

dict.values()   # 取value
dict.keys()     # 取key
dict.setdefault(key,value)  # key不存在时增加新项，存在时不做任何修改
dict.update(dict1) # dict变为两个的交集

dict.items()    # 列表形式

#通过一个列表生成默认dict,有个没办法解释的坑，少用吧这个
dict.fromkeys([1,2,3], 'test')  # {1: 'testd', 2: 'testd', 3: 'testd'}

# 循环dict方法1
for key in info:
    print(key,info[key])

# 循环dict方法2
for k,v in info.items(): #会先把dict转成list,数据里大时莫用
    print(k,v)
```

