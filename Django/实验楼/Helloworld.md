# Hello Django
## 一、实验简介

### 1.1 实验内容

通过对 Django 的简单文字介绍，了解 Django 这个 web framework 的发展情况以及优势。并通过实验楼自带的 Django 环境制作 HelloWorld web 服务器。

## 1.2 实验知识点

- Django 框架发展情况
### 1.3 实验环境

- Xfce终端
- Python 3.x.x
- django 1.8.13
### 1.4 适合人群

本课程难度属于一般，属于初级级别课程，适合具有 Python 基础的用户，熟悉 Python 基础知识加深巩固。

### 1.5 代码下载

本章节代码可以通过下列命令进行下载：
```sh
$ wget http://labfile.oss.aliyuncs.com/courses/774/Django-1.zip
$ unzip Django-1.zip
```

## 二、Django 的特点

Django 是由 Python 开发的一个免费的开源网站框架，可以用于快速搭建高性能，优雅的网站！何为优雅，请看 Django 的以下特点：

### 2.1 强大的数据库功能

用 Python 的类继承，几行代码就可以拥有一个丰富、动态的数据库操作接口（API），如果需要你也能执行 SQL 语句进行数据库的增、删、查、改操作。

### 2.2 自带的强大后台功能

几行简单的代码就能让你的网站拥有一个强大的后台，轻松管理你的内容！

### 2.3 优雅的链接路由

用正则匹配方式匹配链接，传递到对应的函数，随意定义，如你所愿。

### 2.4 Model(模板)系统

易于扩展的 Model 系统，设计简易。易于代码解耦。

### 2.5 缓存系统

与 memcached 或其他的缓存系统联用，更出色的表现，更快的加载速度。

### 2.6 国际化

支持多语言英语，允许自定义翻译的字符，轻松翻译成多国语言。

## 三、Hello World

关于 Django 的环境搭建我们将在下一节中详细介绍，下面部分为初学 Django 的初体验，让读者感受 Django 搭建 Web 服务端的快捷。
在用户根目录下，新建一个 django 目录，用于保存本课程的所有试验代码文件。我们可以执行以下命令进行目录创建：
```sh
$ shiyanlou:~/ $ mkdir django
$ shiyanlou:~/ $ cd django
```
在 django 目录中，我们创建第一个 Django 项目：
```sh
$ shiyanlou:django/ $ django-admin startproject HelloWorld
$ shiyanlou:django/ $ cd HelloWorld
$ shiyanlou:HelloWorld/ $ ls
HelloWorld  manage.py
```
在 HelloWorld 项目目录中，使用 Django 的基本命令创建一个新的 app，名为 Hello：

```sh
$ shiyanlou:HelloWorld/ $ python3 manage.py startapp Hello
$ shiyanlou:HelloWorld/ $ ls
Hello  HelloWorld  manage.py
```
此时，我们项目的目录结构如下所示：
```sh
.
├── Hello
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── HelloWorld
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   └── settings.cpython-34.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
请编辑 Hello 目录中的 views.py 文件如下：
```python
#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'Hello World')
```
这样我们就编辑好了一个视图。由于我们新建立了一个 app，则需要在默认配置中添加这个 app。编辑 ./HelloWorld/settings.py，在 INSTALLED_APPS 这个数组中加入我们的 app：
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Hello',
)
```
最后，我们为刚刚的页面配置 URL 路由即可完成，要编辑的文件为 ./HelloWorld/urls.py：
```python
from django.conf.urls import include, url
from django.contrib import admin
from Hello import views as Hello_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Hello_views.index)
]
```
大功告成，来运行我们的 Web 服务器：
```sh
$ python3 manage.py runserver 8080
```
看到服务器搭建成功的反馈：
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 03, 2017 - 08:23:54
Django version 1.8.13, using settings 'HelloWorld.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
```
打开实验楼环境中的 Firefox 浏览器测试一下。如果成功，则结果如下图：

效果图

四、实验总结

了解 Django 的历史及特点。编写第一个 Django Web 端服务器。

五、课程作业

在 Hello 这个 app 中，在 views.py 增加一个界面，返回字符串 Hello Django，当客户端启动后，请在 http://127.0.0.1:8080/django 显示 Hello Django。
