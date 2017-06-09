
    类---》实例化--》实例对象
    __init__ 构造函数
    __del__ 析构函数
    self.name = name    # 属性，成员变量，字段

    def sayhi()     # 方法，动态属性

共有属性
    nationlity = 'Japan'

私有属性
    __private_attr_name = value

    def get_heart(self):    #对外部提供只读访问接口
        return self.__heart # 相当于c++里面的private

    r1._Role__heart     # 强制访问私有属性, 格式：对象名._类名__属性名

    析构方法：
    def __del__(self):
        print('del...function...')

继承
    要实现继承，可以通过“继承”(Inheritance)和“组合”(Composition)来实现
    在某些OOP语言中，一个子类可以继承多个基类，但是一般情况下， 一个子类只能有一个基类，要实现多重继承，可以通过多级继承来实现。
    继承概念的实现方式主要有2类： 实现继承、接口继承
    1. 实现继承是指使用基类的属性和方法而无需额外编码的能力
    2. 接口继承是指使用属性和方法的名称、但是子类必须提供实现的能力（子类重构父类方法）

    抽象类仅定义由子类创建的一般属性和方法。

    OO开发范式大致为： 划分对象--> 抽象类 --> 将类组织成为类层次化结构（继承和合成）--> 用类与实例进行设计和实现几个阶段。

经典类 VS 新式类
    SchoolMember.__init__(self, name, age, sex)   # 经典类写法: 父类.__init(self,arg1,arg2,...)
    super(Teacher, self).__init__(name, age, sex)   # 新式类写法: super(子类,self).__init__(arg1,arg2,...)

    class Person(object):   # new style
        super()
    class Person:   # classical style
        Person.__init__()

    多继承时 继承顺序的区别:
    python3 查找顺序  广度查询
    python2  新式类：广度查询，   经典类：深度查询


多态

类的特殊方法：
    # class A   # A为类
    # a = A()   # a为对象

    # A.__doc__       返回描述信息
    # a.__doc__       同上 ,如 '该类是Dog类'

    # a.__module__    返回当前操作的对象在哪个模块
    # A.__module__     同上，如lib.aa

    # A.__dict__    返回类里的所有属性，不包括实例属性
    # a.__dict__    返回实例的所有属性，不包括类属性

    # A.__class__   返回类名（包含包名），如lib.aa.C

静态方法
    @staticmethod   为静态方法
    只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
    作用：取消与类的关联，具体表现为不用必须传入参数self了，但是如果传了self，会把self当成普通的位置参数
    应用场景：一般情况下我们需要使用工具包的一些个类的封装，可以用静态方法，比如os模块


类方法
    @classmethod
    只能访问类变量，不能访问实例变量


属性方法
    @property
    把一个方法变成一个静态属性

反射
    hasattr(obj, name_str), 判断一个对象obj里是否有对应的name_str字符串的方法
    getattr(obj, name_str), 根据字符串去获取对象obj里的对应的方法的内存地址
    setattr(obj, 'y', v),   相当于 obj.y = v
    delattr