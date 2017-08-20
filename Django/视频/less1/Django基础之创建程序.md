# Django基础之创建程序
- 1 安装Django
```
pip3 install django
```

- 2 创建django项目与app
```
a. 命令：
    django-admin startproject project_name      # 创建Django项目
    cd project_name                             # 进入Djano项目
    python manage.py startapp app0              # 创建app0
    python manage.py startapp app1              # 创建app1
    python manage.py startapp app2              # 创建app2
b. pycharm
    创建django程序
    Windows:
        终端：python manage.py startapp app0              # 创建app0
    MAC：
        options+R
            startapp app0
```

Django里面有project和app的概念
```
project_name
    project_name
    manage.py
    app0
    app1
    app2
    app3
```

比如：
```
django-admin startproject project_name
python manage.py startapp monitor
python manage.py startapp cmdb
python manage.py startapp openstack
```

## 2. 执行django程序
先进入project
```
python manage.py runserver 127.0.0.1:8000
```

## 3.Django依赖数据库
```
python manage.py makemigrations     # 生成配置文件
python manage.py migrate        # 根据配置文件创建数据库相关
```
## 4、admin
```
python manage.py createsuperuser        # 创建超级用户
# 然后访问浏览器：http://127.0.0.1:8000/home/
```

## 5、路由系统
- 1、静态路由
- 2、动态路由
```
    方法一：按照顺序，第n个匹配的数据，交给函数的第n个参数，严格按照顺序执行（nid）
    方法二：模板的方法，将匹配的参数，传给指定的形式参数（^page/(?P<n1>\d+)/(?P<n2>\d+)）
```
- 3、二级路由
```
    先自己创建各个app下的url.py，同时在views中增加函数
        app01
            url.py
    然后将project_name下的路由系统指向app下的urls.py
    即：
    url(r'^app01/', include('app01.urls'))
```

## 6、基本数据库操作
    ORM框架
        code first
            自己写类    -->     数据库表
        db first
            自己命令数据库表和字典     --> 创建类
        
        使用类进行数据操作

- a.创建类。 在models中创建类，比如：
```python
class UserInfo(models.Model):
    username = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    age = models.IntegerField()
```
- b.配置,在settings.py中的INSTALLED_APPS中添加app，比如：
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]
```

- b.使用命令创建表
```
python manage.py makemigrations     # 生成配置文件
python manage.py migrate        # 根据配置文件创建数据库相关
```