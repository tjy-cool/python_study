
导入模块
import random

random.random()         # 0-1之间的小数
random.randint(a,b)     # 随机返回[a,b]直接的任意一个数
random.randrange(start, stop=None, step=1)      # 随机返回start到stop，但是不包括stop值
random.sample(population, k)        # 从population中随机获取k个值，以列表的形式返回