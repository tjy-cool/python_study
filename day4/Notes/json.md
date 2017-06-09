# json & picle 模块
- json，用于字符串 和 python数据类型间进行转换
- pickle，用于python特有的类型 和 python的数据类型间进行转换

Json模块提供了四个功能：dumps、dump、loads、load

pickle模块提供了四个功能：dumps、dump、loads、load

import json

json.dumps():序列化数据类型为字符串

json.loads():反序列化成数据类型
```python
import json

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) 
```
