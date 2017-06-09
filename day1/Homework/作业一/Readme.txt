login.py        为显示密码登陆
login_getpass.py   为隐藏密码登陆

login.py         能在pycharm ide中运行
login_getpass.py 只能在CMD终端运行

该程序的用户名与密码信息保存在 username_passwd.txt 中，用户名输入错误信息保存在 err.txt 中，

随意输入一个用户名，先判断是否存在，存在提示输入密码，不存在则提示创建新用户及密码

当用户输入密码错误数达到三次，保存错误信息，强行退出程序，且下次无法登陆

当用户名和密码正确时，显示欢迎信息，并退出程序