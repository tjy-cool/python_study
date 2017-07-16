#!/usr/bin/env python
# Funtion:      
# Filename:

class City(object):
    def __setitem__(self, key, value):
        if key == "city":
            self.city = value
            print("新建城市 %s 成功！"% (self.city))

    def __getitem__(self, item):
        if item == "city":
            return self.city

class Myclass(object):
    def __setitem__(self, key, value):
        if key == "myclass":
            self.myclass = value
            print("新建课程 %s 成功！" % (self.myclass))
        if key == "city":
            try:
                self.city = value["city"]
                print("绑定课程成功！课程是 %s, 绑定的城市是 %s" % (self.myclass, self.city))
            except Exception:
                print("输入的城市名称不对！")
    def __getitem__(self, item):
        if item == "city":
            try:
                return self.city
            except Exception:
                print("此课程还没有绑定城市！")
        if item == "class":
            return self.myclass
#
# cityname = "Beijing"
cityname = "Shanghai"
cityobj = City()
cityobj['city'] = cityname

classname = "Python"
classobj = Myclass()
classobj["myclass"] = classname

classobj["city"] = cityobj

print("验证%s课程对象 所在的城市是%s" % (classobj["myclass"], classobj["city"]))


